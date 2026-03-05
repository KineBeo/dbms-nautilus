/*
 * sqlite_harness.c — Persistent-mode AFL harness for SQLite fuzzing
 *
 * Fixed schema pre-loaded before __AFL_INIT() so schema setup cost
 * is paid once per fork, not once per execution.
 *
 * Compile (per-version):
 *   make SQLITE=path/to/sqlite3.c TARGET=sqlite_harness_<version>
 *
 * Oracle:
 *   ASan crash  → exitcode 223  (ASAN_OPTIONS=exitcode=223)
 *   UBSan crash → exitcode 1    (UBSAN_OPTIONS=halt_on_error=1,exitcode=1)
 *   Signal      → detected by Nautilus forksrv
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* SQLite amalgamation — path set by Makefile */
#include SQLITE_HEADER

/* When compiled without afl-clang-fast, stub out AFL macros so the
 * same source can be used for standalone oracle testing. */
#ifndef __AFL_HAVE_MANUAL_CONTROL
#  define __AFL_INIT()       do {} while (0)
#  define __AFL_LOOP(n)      ((__afl_standalone_once--) > 0)
static volatile int __afl_standalone_once = 1;
#endif

/* ------------------------------------------------------------------ */
/* Fixed schema                                                         */
/* ------------------------------------------------------------------ */
static const char *SCHEMA_SQL =
    "CREATE TABLE t1(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL);"
    "CREATE TABLE t2(c1 INTEGER, c2 TEXT, c3 REAL);"
    "CREATE TABLE t3(c1 INTEGER, c2 TEXT NOT NULL, c3 REAL DEFAULT 0.0);"
    "INSERT INTO t1 VALUES(1,'hello',1.5),(2,'world',2.5),"
    "  (-1,'neg',-1.0),(0,'zero',0.0),"
    "  (9223372036854775807,'max',1e308);"
    "INSERT INTO t2 VALUES(1,'a',1.0),(2,'b',2.0),(3,'c',3.0);"
    "INSERT INTO t3(c1,c2,c3) VALUES(1,'x',0.1),(2,'y',0.2);"
    /* fts5 init crashes on older versions (e.g. 3.32.2 CVE-2020-13434) during
     * tokenizer setup — keep fts3 only for schema pre-load safety. The fuzzer
     * grammar still generates FTS5 queries; those are fine to hit at exec time. */
    "CREATE VIRTUAL TABLE fts_t1 USING fts3(c1, c2);"
    "INSERT INTO fts_t1 VALUES('1','hello world');"
    "INSERT INTO fts_t1 VALUES('2','foo bar baz');"
    "CREATE VIRTUAL TABLE fts_t2 USING fts3(c1, c2, c3);"
    "INSERT INTO fts_t2 VALUES('1','hello','1.5');"
    "INSERT INTO fts_t2 VALUES('2','world','2.5');"
    "CREATE INDEX idx_t1_c2 ON t1(c2);"
    "CREATE INDEX idx_t2_c1 ON t2(c1);"
    "CREATE VIEW v1 AS SELECT t1.c1, t1.c2, t2.c3 FROM t1 JOIN t2 ON t1.c1=t2.c1;";

static sqlite3 *db = NULL;

/* Called once before __AFL_INIT() — schema setup paid once per fork */
__attribute__((constructor))
static void setup_db(void) {
    int rc = sqlite3_open(":memory:", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "sqlite3_open failed: %s\n", sqlite3_errmsg(db));
        exit(1);
    }
    char *errmsg = NULL;
    rc = sqlite3_exec(db, SCHEMA_SQL, NULL, NULL, &errmsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "schema setup failed: %s\n", errmsg);
        sqlite3_free(errmsg);
        exit(1);
    }
}

/* ------------------------------------------------------------------ */
/* Input reader                                                         */
/* ------------------------------------------------------------------ */
static char *read_input(const char *path, size_t *out_len) {
    FILE *f = fopen(path, "rb");
    if (!f) return NULL;
    fseek(f, 0, SEEK_END);
    long sz = ftell(f);
    fseek(f, 0, SEEK_SET);
    if (sz <= 0 || sz > 1024 * 1024) { fclose(f); return NULL; }
    char *buf = malloc(sz + 1);
    if (!buf) { fclose(f); return NULL; }
    size_t n = fread(buf, 1, sz, f);
    fclose(f);
    buf[n] = '\0';
    *out_len = n;
    return buf;
}

/* ------------------------------------------------------------------ */
/* Main                                                                 */
/* ------------------------------------------------------------------ */
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    __AFL_INIT();

    while (__AFL_LOOP(1000)) {
        size_t sql_len = 0;
        char *sql = read_input(argv[1], &sql_len);
        if (!sql) continue;

        /* Execute all statements; ignore semantic errors (table not found, etc.)
         * We only care about memory-safety crashes caught by ASan/UBSan. */
        char *errmsg = NULL;
        sqlite3_exec(db, sql, NULL, NULL, &errmsg);
        if (errmsg) sqlite3_free(errmsg);

        free(sql);
    }

    sqlite3_close(db);
    return 0;
}
