/*
 * sqlite_harness.c — AFL fork-server harness for Nautilus SQLite fuzzing
 *
 * Opens an empty :memory: database. The grammar generates self-contained
 * multi-statement SQL (DDL + INSERT + SELECT), so no pre-loaded schema.
 *
 * Oracle:
 *   - ASan crash  → exitcode 223  (ASAN_OPTIONS=exitcode=223)
 *   - UBSan crash → exitcode 1    (UBSAN_OPTIONS=halt_on_error=1,exitcode=1)
 *   - Signal      → detected by Nautilus forksrv (SQLITE_DEBUG asserts → SIGTRAP)
 *
 * Compile:
 *   make SQLITE=../cve_builds/sqlite-3.31.1/sqlite3.c \
 *        TARGET=sqlite_harness_sqlite-3.31.1
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

static sqlite3 *db = NULL;

/* Called once before __AFL_INIT() — open blank DB.
 * The grammar creates its own tables via Schema-Setup, so the DB starts empty. */
__attribute__((constructor))
static void setup_db(void) {
    int rc = sqlite3_open(":memory:", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "sqlite3_open failed: %s\n", sqlite3_errmsg(db));
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
