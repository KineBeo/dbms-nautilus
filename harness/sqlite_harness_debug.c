/*
 * sqlite_harness_debug.c — Debug version of the harness with result logging
 *
 * Same as sqlite_harness.c but prints every query result row to stdout
 * and every SQL error to stderr. Use this for manual testing only —
 * never for actual fuzzing campaigns.
 *
 * Build:
 *   make test-build SQLITE=../cve_builds/sqlite-<ver>/sqlite3.c \
 *                   TARGET=sqlite_harness_debug_<ver> \
 *                   HARNESS=sqlite_harness_debug.c
 *
 * Or directly:
 *   clang -O1 -g -fsanitize=address -fsanitize=undefined \
 *         -fno-sanitize-recover=all \
 *         -DSQLITE_HEADER=\"../cve_builds/sqlite-3.32.2/sqlite3.c\" \
 *         -DSQLITE_ENABLE_FTS3 -DSQLITE_ENABLE_FTS5 \
 *         -DSQLITE_ENABLE_RTREE -DSQLITE_ENABLE_JSON1 \
 *         -DHAVE_MREMAP=0 \
 *         -o sqlite_harness_debug_3322 sqlite_harness_debug.c \
 *         -ldl -lpthread -lm
 *
 * Run:
 *   echo "SELECT * FROM t1;" > /tmp/test.sql
 *   ./sqlite_harness_debug_3322 /tmp/test.sql
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* SQLite amalgamation — path set at compile time via -DSQLITE_HEADER=... */
#include SQLITE_HEADER

/* Stub out AFL macros — this file is always compiled with plain clang */
#define __AFL_INIT()       do {} while (0)
#define __AFL_LOOP(n)      ((__afl_standalone_once--) > 0)
static volatile int __afl_standalone_once = 1;

/* ------------------------------------------------------------------ */
/* Fixed schema (same as production harness)                           */
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
    /* fts5 init crashes on older versions (e.g. 3.32.2) during tokenizer
     * setup — keep fts3 only for schema pre-load safety. */
    "CREATE VIRTUAL TABLE fts_t1 USING fts3(c1, c2);"
    "INSERT INTO fts_t1 VALUES('1','hello world');"
    "INSERT INTO fts_t1 VALUES('2','foo bar baz');"
    "CREATE INDEX idx_t1_c2 ON t1(c2);"
    "CREATE INDEX idx_t2_c1 ON t2(c1);"
    "CREATE VIEW v1 AS SELECT t1.c1, t1.c2, t2.c3 FROM t1 JOIN t2 ON t1.c1=t2.c1;";

static sqlite3 *db = NULL;
static int query_count = 0;

__attribute__((constructor))
static void setup_db(void) {
    int rc = sqlite3_open(":memory:", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "[setup] sqlite3_open failed: %s\n", sqlite3_errmsg(db));
        exit(1);
    }
    char *errmsg = NULL;
    rc = sqlite3_exec(db, SCHEMA_SQL, NULL, NULL, &errmsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "[setup] schema failed: %s\n", errmsg);
        sqlite3_free(errmsg);
        exit(1);
    }
    fprintf(stderr, "[setup] schema loaded ok\n");
}

/* ------------------------------------------------------------------ */
/* Row logger callback                                                  */
/* ------------------------------------------------------------------ */
static int log_row(void *unused, int ncols, char **vals, char **cols) {
    (void)unused;
    for (int i = 0; i < ncols; i++)
        printf("  %-20s = %s\n", cols[i], vals[i] ? vals[i] : "NULL");
    printf("  ---\n");
    return 0;
}

/* ------------------------------------------------------------------ */
/* Input reader                                                         */
/* ------------------------------------------------------------------ */
static char *read_input(const char *path, size_t *out_len) {
    FILE *f = fopen(path, "rb");
    if (!f) { fprintf(stderr, "[error] cannot open: %s\n", path); return NULL; }
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
        fprintf(stderr, "usage: %s <input.sql>\n", argv[0]);
        fprintf(stderr, "\nPre-loaded tables: t1, t2, t3, fts_t1 (fts3), v1\n");
        fprintf(stderr, "Example: echo \"SELECT * FROM t1;\" > /tmp/q.sql && ./%s /tmp/q.sql\n", argv[0]);
        return 1;
    }

    __AFL_INIT();

    while (__AFL_LOOP(1000)) {
        size_t sql_len = 0;
        char *sql = read_input(argv[1], &sql_len);
        if (!sql) continue;

        query_count++;
        printf("\n[query #%d] %s\n", query_count, sql);

        char *errmsg = NULL;
        int rc = sqlite3_exec(db, sql, log_row, NULL, &errmsg);
        if (rc != SQLITE_OK) {
            fprintf(stderr, "[error] %s\n", errmsg);
            sqlite3_free(errmsg);
        } else {
            printf("[ok] exit code will be 0\n");
        }

        free(sql);
    }

    sqlite3_close(db);
    return 0;
}
