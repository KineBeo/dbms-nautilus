# Harness Makefile (lives in harness/src/, outputs to harness/{afl,test,nosanit}/)
# Usage:
#   make SQLITE=../../cve_builds/sqlite-3.31.1/sqlite3.c TARGET=sqlite_harness_sqlite-3.31.1
#   make SQLITE=... TARGET=... AFL_CC=/path/to/afl-clang-fast
#
# Environment variables:
#   SQLITE      path to sqlite3.c amalgamation (required)
#   TARGET      output binary name (default: sqlite_harness)
#   AFL_CC      AFL compiler (default: afl-clang-fast)
#   EXTRA_CFLAGS  additional flags

AFL_CC    ?= afl-clang-fast
TARGET    ?= sqlite_harness
SQLITE    ?=

ASAN_FLAGS  = -fsanitize=address -fsanitize=undefined
ASAN_FLAGS += -fno-sanitize-recover=all
CFLAGS      = -O1 -g $(ASAN_FLAGS) $(EXTRA_CFLAGS)
CFLAGS     += -DSQLITE_HEADER=\"$(SQLITE)\"
CFLAGS     += -DSQLITE_ENABLE_FTS3 -DSQLITE_ENABLE_FTS5
CFLAGS     += -DSQLITE_ENABLE_RTREE -DSQLITE_ENABLE_JSON1
CFLAGS     += -DSQLITE_MAX_EXPR_DEPTH=1000
CFLAGS     += -DSQLITE_DEBUG
CFLAGS     += -DHAVE_MREMAP=0

NOSANIT_CFLAGS  = -O1 -g $(EXTRA_CFLAGS)
NOSANIT_CFLAGS += -DSQLITE_HEADER=\"$(SQLITE)\"
NOSANIT_CFLAGS += -DSQLITE_ENABLE_FTS3 -DSQLITE_ENABLE_FTS5
NOSANIT_CFLAGS += -DSQLITE_ENABLE_RTREE -DSQLITE_ENABLE_JSON1
NOSANIT_CFLAGS += -DSQLITE_MAX_EXPR_DEPTH=1000
NOSANIT_CFLAGS += -DHAVE_MREMAP=0

all: $(TARGET)

$(TARGET): sqlite_harness.c
	@if [ -z "$(SQLITE)" ]; then echo "Error: SQLITE not set"; exit 1; fi
	@mkdir -p ../afl
	$(AFL_CC) $(CFLAGS) -o ../afl/$@ sqlite_harness.c -ldl -lpthread -lm

test-build:
	@if [ -z "$(SQLITE)" ]; then echo "Error: SQLITE not set"; exit 1; fi
	@mkdir -p ../test
	clang $(CFLAGS) -o ../test/$(TARGET)_test sqlite_harness.c -ldl -lpthread -lm

nosanit:
	@if [ -z "$(SQLITE)" ]; then echo "Error: SQLITE not set"; exit 1; fi
	@mkdir -p ../nosanit
	clang $(NOSANIT_CFLAGS) -o ../nosanit/$(TARGET)_nosanit sqlite_harness.c -ldl -lpthread -lm

build-all:
	@for dir in ../../cve_builds/sqlite-*/; do \
		ver=$$(basename $$dir); \
		sqlite=$$dir/sqlite3.c; \
		if [ -f "$$sqlite" ]; then \
			echo "Building $$ver..."; \
			$(MAKE) SQLITE=$$sqlite TARGET=sqlite_harness_$$ver; \
			$(MAKE) SQLITE=$$sqlite TARGET=sqlite_harness_$$ver test-build; \
			$(MAKE) SQLITE=$$sqlite TARGET=sqlite_harness_$$ver nosanit; \
		fi; \
	done

clean:
	rm -f ../afl/sqlite_harness* ../test/sqlite_harness* ../nosanit/sqlite_harness*

.PHONY: all build-all test-build nosanit clean
