# RQ2 Single Source of Truth

Generated: 2026-05-23T12:24:12.534502
Script: `scripts/rq2_source_of_truth.py`
Versions tested: 19 (3.26.0 -- 3.53.0)
Bug classes: 13
CVE PoCs: 5

## 1. Bug Class Summary

| BC | Bug Type | DBMS Versions | EBNF Versions | CVE Match | Prod SEGV? | Hashes (DBMS/EBNF) | Fix |
|-----|----------|---------------|---------------|-----------|------------|---------------------|-----|
| BC001 | null pointer in sqlite3ExprCodeTarg | 3.26.0, 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0 +4 | --- | **CVE-2020-13435** | YES | 3/--- | 3.32.1 |
| BC002 | null pointer in sqlite3Fts5GetToken | 3.26.0, 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0 +9 | 3.30.1;3.31.1;3.32.0;3.32.2 | --- | no | 4/4 | 3.36.0 |
| BC003 | signed integer overflow in sqlite3  | 3.26.0, 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0 +4 | --- | **CVE-2020-13434** | YES | 6/--- | 3.32.1 |
| BC004 | misaligned access in sqlite3WindowU | 3.30.0, 3.30.1 | 3.30.1 | --- | YES | 1/1 | 3.31.1 |
| BC005 | float cast overflow in alsoAnInt | 3.30.0, 3.30.1, 3.31.1, 3.32.0, 3.32.1, 3.32.2 +5 | 3.30.1;3.32.0 | --- | no | 10/7 | 3.40.0 |
| BC006 | null pointer in isAuxiliaryVtabOper | 3.31.1 | --- | **CVE-2020-9327** | YES | 1/--- | 3.32.0 |
| BC007 | misaligned access in resetAccumulat | 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0, 3.30.0 +1 | --- | **CVE-2020-13871** | no | 1/--- | 3.31.1 |
| BC008 | misaligned access in sqlite3ExprCod | 3.26.0, 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0 +3 | --- | --- | YES | 13/--- | 3.32.1 |
| BC009 | float cast overflow in sqlite3VdbeM | 3.31.1, 3.32.0, 3.32.1, 3.32.2, 3.32.3, 3.33.0 +3 | --- | --- | no | 2/--- | 3.40.0 |
| BC010 | null pointer in sqlite3Select | 3.30.0, 3.30.1, 3.31.1, 3.32.0, 3.32.1, 3.32.2 | --- | --- | YES | 2/--- | 3.32.3 |
| BC011 | signal 6 in sqlite3WindowListDelete | 3.26.0, 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0 +2 | 3.30.1 | --- | YES | 2/2 | 3.31.1 |
| BC012 | null pointer in sqlite3Atoi64 | 3.26.0, 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0 +2 | --- | --- | YES | 2/--- | 3.31.1 |
| BC013 | signal 6 in sqlite3ExprCodeTarget | 3.26.0, 3.27.0, 3.27.1, 3.27.2, 3.28.0, 3.29.0 +3 | --- | --- | YES | 1/--- | 3.32.1 |

## 2. CVE Match Matrix

Match = same crash line on same version. PARTIAL = line matches but version range inconsistent.

| BC | CVE-2020-13434 | CVE-2020-13435 | CVE-2020-13871 | CVE-2020-15358 | CVE-2020-9327 |
|-----|---|---|---|---|---|
| BC001 | --- | **MATCH** (3.26.0,3.27.0) | --- | --- | --- |
| BC002 | --- | --- | --- | --- | --- |
| BC003 | **MATCH** (3.26.0,3.27.0) | --- | --- | --- | --- |
| BC004 | --- | --- | --- | --- | --- |
| BC005 | --- | --- | --- | --- | --- |
| BC006 | --- | --- | --- | --- | **MATCH** (3.31.1) |
| BC007 | --- | --- | **MATCH** (3.27.0,3.27.1) | --- | --- |
| BC008 | --- | --- | --- | --- | --- |
| BC009 | --- | --- | --- | --- | --- |
| BC010 | --- | --- | --- | --- | --- |
| BC011 | --- | --- | --- | --- | --- |
| BC012 | --- | --- | --- | --- | --- |
| BC013 | --- | --- | --- | --- | --- |

## 3. Production Impact (nosanit)

Legend: `.` = OK, `S` = SEGV, `A` = SIGABRT, `-` = no harness

| BC | 3.26.0 | 3.27.0 | 3.27.1 | 3.27.2 | 3.28.0 | 3.29.0 | 3.30.0 | 3.30.1 | 3.31.1 | 3.32.0 | 3.32.1 | 3.32.2 | 3.32.3 | 3.33.0 | 3.34.0 | 3.36.0 | 3.39.1 | 3.40.0 | 3.53.0 |
|-----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BC001 | S | S | S | S | S | S | S | S | S | S | . | . | . | . | . | . | . | . | . |
| BC002 | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| BC003 | S | S | S | S | S | S | S | S | S | S | . | . | . | . | . | . | . | . | . |
| BC004 | . | . | . | . | . | . | S | . | . | . | . | . | . | . | . | . | . | . | . |
| BC005 | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| BC006 | . | . | . | . | . | . | . | . | S | . | . | . | . | . | . | . | . | . | . |
| BC007 | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| BC008 | S | S | S | S | S | S | S | S | S | S | . | . | . | . | . | . | . | . | . |
| BC009 | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| BC010 | . | . | . | . | . | . | S | S | S | S | S | S | . | . | . | . | . | . | . |
| BC011 | S | S | S | S | S | S | S | S | . | . | . | . | . | . | . | . | . | . | . |
| BC012 | S | S | S | S | S | . | . | . | . | . | . | . | . | . | . | . | . | . | . |
| BC013 | S | S | S | S | S | S | S | S | S | S | . | . | . | . | . | . | . | . | . |

## 4. Sanitizer Crash (test harness)

Legend: `.` = OK, `U` = UBSan, `X` = ASan, `S` = SEGV, `A` = SIGABRT, `-` = no harness

| BC | 3.26.0 | 3.27.0 | 3.27.1 | 3.27.2 | 3.28.0 | 3.29.0 | 3.30.0 | 3.30.1 | 3.31.1 | 3.32.0 | 3.32.1 | 3.32.2 | 3.32.3 | 3.33.0 | 3.34.0 | 3.36.0 | 3.39.1 | 3.40.0 | 3.53.0 |
|-----|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BC001 | A | A | A | A | A | A | U | U | U | U | . | . | . | . | . | . | . | . | . |
| BC002 | U | U | U | U | U | U | U | U | U | U | U | U | U | U | U | . | . | . | . |
| BC003 | U | U | U | U | U | U | U | U | U | U | . | . | . | . | . | . | . | . | . |
| BC004 | . | . | . | . | . | . | U | U | . | . | . | . | . | . | . | . | . | . | . |
| BC005 | . | . | . | . | . | . | U | U | U | U | U | U | U | U | U | U | U | . | . |
| BC006 | . | . | . | . | . | . | . | . | U | . | . | . | . | . | . | . | . | . | . |
| BC007 | . | A | A | A | A | A | U | U | . | . | . | . | . | . | . | . | . | . | . |
| BC008 | A | A | A | A | A | A | X | X | U | . | . | . | . | . | . | . | . | . | . |
| BC009 | . | . | . | . | . | . | . | . | U | U | U | U | U | U | U | U | U | . | . |
| BC010 | . | . | . | . | . | . | U | U | U | U | U | U | . | . | . | . | . | . | . |
| BC011 | X | X | X | X | X | X | X | X | . | . | . | . | . | . | . | . | . | . | . |
| BC012 | U | U | U | U | U | U | U | U | . | . | . | . | . | . | . | . | . | . | . |
| BC013 | A | A | A | A | A | A | X | X | U | . | . | . | . | . | . | . | . | . | . |

## 5. CVE PoC Crash Signatures

### CVE-2020-13434

**3.26.0** (UBSan): L27619 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.26.0/sqlite3.c:27619:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.26.0/sqlite3.c:27619:35 in
```

**3.27.0** (UBSan): L27735 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.27.0/sqlite3.c:27735:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.0/sqlite3.c:27735:35 in
```

**3.27.1** (UBSan): L27735 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.27.1/sqlite3.c:27735:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.1/sqlite3.c:27735:35 in
```

**3.27.2** (UBSan): L27734 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.27.2/sqlite3.c:27734:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.2/sqlite3.c:27734:35 in
```

**3.28.0** (UBSan): L27791 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.28.0/sqlite3.c:27791:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.28.0/sqlite3.c:27791:35 in
```

**3.29.0** (UBSan): L27877 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.29.0/sqlite3.c:27877:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.29.0/sqlite3.c:27877:35 in
```

**3.30.0** (UBSan): L27971 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:27971:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:27971:35 in
```

**3.30.1** (UBSan): L27975 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../cve_builds/sqlite-3.30.1/sqlite3.c:27975:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:27975:35 in
```

**3.31.1** (UBSan): L28528 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../cve_builds/sqlite-3.31.1/sqlite3.c:28528:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:28528:35 in
```

**3.32.0** (UBSan): L28657 `` — signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../cve_builds/sqlite-3.32.0/sqlite3.c:28657:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:28657:35 in
```


### CVE-2020-13435

**3.26.0** (SIGABRT): L125875 `` — SIGABRT
```
sqlite_harness_sqlite-3.26.0_test: ./../../cve_builds/sqlite-3.26.0/sqlite3.c:125875: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.0** (SIGABRT): L126309 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.0_test: ./../../cve_builds/sqlite-3.27.0/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.1** (SIGABRT): L126309 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.1_test: ./../../cve_builds/sqlite-3.27.1/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.2** (SIGABRT): L126295 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.2_test: ./../../cve_builds/sqlite-3.27.2/sqlite3.c:126295: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.28.0** (SIGABRT): L126595 `` — SIGABRT
```
sqlite_harness_sqlite-3.28.0_test: ./../../cve_builds/sqlite-3.28.0/sqlite3.c:126595: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.29.0** (SIGABRT): L131002 `` — SIGABRT
```
sqlite_harness_sqlite-3.29.0_test: ./../../cve_builds/sqlite-3.29.0/sqlite3.c:131002: int sqlite3Select(Parse *, Select *, SelectDest *): Assertion `pItem->addrFillSub==0' failed.
```

**3.30.0** (UBSan): L101285 `` — applying zero offset to null pointer
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:101285:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:101285:16 in
```

**3.30.1** (UBSan): L101292 `` — applying zero offset to null pointer
```
../cve_builds/sqlite-3.30.1/sqlite3.c:101292:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:101292:16 in
```

**3.31.1** (UBSan): L102748 `` — applying zero offset to null pointer
```
../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16 in
```

**3.32.0** (UBSan): L103541 `` — applying zero offset to null pointer
```
../cve_builds/sqlite-3.32.0/sqlite3.c:103541:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:103541:16 in
```


### CVE-2020-13871

**3.27.0** (SIGABRT): L126304 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.0_test: ./../../cve_builds/sqlite-3.27.0/sqlite3.c:126304: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.27.1** (SIGABRT): L126304 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.1_test: ./../../cve_builds/sqlite-3.27.1/sqlite3.c:126304: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.27.2** (SIGABRT): L126290 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.2_test: ./../../cve_builds/sqlite-3.27.2/sqlite3.c:126290: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.28.0** (SIGABRT): L126590 `` — SIGABRT
```
sqlite_harness_sqlite-3.28.0_test: ./../../cve_builds/sqlite-3.28.0/sqlite3.c:126590: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.29.0** (SIGABRT): L127111 `` — SIGABRT
```
sqlite_harness_sqlite-3.29.0_test: ./../../cve_builds/sqlite-3.29.0/sqlite3.c:127111: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.30.0** (ASan): L130911 `resetAccumulator` — heap-use-after-free
```
=================================================================
==112238==ERROR: AddressSanitizer: heap-use-after-free on address 0xeac4066001ac at pc 0xbb6c49e8a290 bp 0xffffe4e67280 sp 0xffffe4e67278
READ of size 4 at 0xeac4066001ac thread T0
    #0 0xbb6c49e8a28c in resetAccumulator /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:130911:7
    #1 0xbb6c49e030f8 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:132150:7
    #2 0xbb6c49e364f4 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:100493:7
    #3 0xbb6c49e2d450 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101465:16
    #4 0xbb6c49e34f58 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101917:19
    #5 0xbb6c49ec4bd4 in pushOntoSorter /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126246:3
    #6 0xbb6c49e8430c in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c
    #7 0xbb6c49e01ce8 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131797:7
    #8 0xbb6c49e72388 in multiSelectOrderBy /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:128886:3
    #9 0xbb6c49e72388 in multiSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:128193:12
    #10 0xbb6c49dffba4 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131431:10
    #11 0xbb6c49ddce24 in yy_reduce /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:153189:3
    #12 0xbb6c49cc21bc in sqlite3Parser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:154478:15
    #13 0xbb6c49cc21bc in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:155618:5
    #14 0xbb6c49cbd58c in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125296:5
    #15 0xbb6c49cbd58c in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125392:10
    #16 0xbb6c49cba68c in sqlite3_prepare_v2 /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125476:8
... (124 more lines)
```

**3.30.1** (ASan): L130929 `resetAccumulator` — heap-use-after-free
```
=================================================================
==112241==ERROR: AddressSanitizer: heap-use-after-free on address 0xff58cb0001ac at pc 0xc62934839e84 bp 0xffffcbad53a0 sp 0xffffcbad5398
READ of size 4 at 0xff58cb0001ac thread T0
    #0 0xc62934839e80 in resetAccumulator /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:130929:7
    #1 0xc629347b2d00 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:132168:7
    #2 0xc629347e6100 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:100500:7
    #3 0xc629347dd05c in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101472:16
    #4 0xc629347e4b64 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101924:19
    #5 0xc6293487494c in pushOntoSorter /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126256:3
    #6 0xc62934833f14 in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c
    #7 0xc629347b18f0 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131815:7
    #8 0xc62934821f9c in multiSelectOrderBy /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:128896:3
    #9 0xc62934821f9c in multiSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:128203:12
    #10 0xc629347af7ac in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131449:10
    #11 0xc6293478ca68 in yy_reduce /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:153207:3
    #12 0xc629346722d8 in sqlite3Parser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:154496:15
    #13 0xc629346722d8 in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:155636:5
    #14 0xc6293466d6a8 in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125306:5
    #15 0xc6293466d6a8 in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125402:10
    #16 0xc6293466a7a8 in sqlite3_prepare_v2 /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125486:8
... (124 more lines)
```

**3.31.1** (SIGABRT): L133237 `` — SIGABRT
```
sqlite_harness_sqlite-3.31.1_test: ./../cve_builds/sqlite-3.31.1/sqlite3.c:133237: void resetAccumulator(Parse *, AggInfo *): Assertion `!ExprHasProperty(pE, EP_xIsSelect)' failed.
```

**3.32.0** (SIGABRT): L134192 `` — SIGABRT
```
sqlite_harness_sqlite-3.32.0_test: ./../cve_builds/sqlite-3.32.0/sqlite3.c:134192: void resetAccumulator(Parse *, AggInfo *): Assertion `!ExprHasProperty(pE, EP_xIsSelect)' failed.
```


### CVE-2020-15358

**3.26.0** (SIGABRT): L127075 `` — SIGABRT
```
sqlite_harness_sqlite-3.26.0_test: ./../../cve_builds/sqlite-3.26.0/sqlite3.c:127075: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.27.0** (SIGABRT): L127509 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.0_test: ./../../cve_builds/sqlite-3.27.0/sqlite3.c:127509: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.27.1** (SIGABRT): L127509 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.1_test: ./../../cve_builds/sqlite-3.27.1/sqlite3.c:127509: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.27.2** (SIGABRT): L127495 `` — SIGABRT
```
sqlite_harness_sqlite-3.27.2_test: ./../../cve_builds/sqlite-3.27.2/sqlite3.c:127495: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.28.0** (SIGABRT): L127795 `` — SIGABRT
```
sqlite_harness_sqlite-3.28.0_test: ./../../cve_builds/sqlite-3.28.0/sqlite3.c:127795: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.29.0** (SIGABRT): L128314 `` — SIGABRT
```
sqlite_harness_sqlite-3.29.0_test: ./../../cve_builds/sqlite-3.29.0/sqlite3.c:128314: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.30.0** (SIGABRT): L128784 `` — SIGABRT
```
sqlite_harness_sqlite-3.30.0_test: ./../../cve_builds/sqlite-3.30.0/sqlite3.c:128784: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.30.1** (SIGABRT): L128794 `` — SIGABRT
```
sqlite_harness_sqlite-3.30.1_test: ./../cve_builds/sqlite-3.30.1/sqlite3.c:128794: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.31.1** (SIGABRT): L131068 `` — SIGABRT
```
sqlite_harness_sqlite-3.31.1_test: ./../cve_builds/sqlite-3.31.1/sqlite3.c:131068: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.32.0** (SIGABRT): L131982 `` — SIGABRT
```
sqlite_harness_sqlite-3.32.0_test: ./../cve_builds/sqlite-3.32.0/sqlite3.c:131982: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.32.1** (SIGABRT): L132038 `` — SIGABRT
```
sqlite_harness_sqlite-3.32.1_test: ./../../cve_builds/sqlite-3.32.1/sqlite3.c:132038: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```

**3.32.2** (SIGABRT): L132040 `` — SIGABRT
```
sqlite_harness_sqlite-3.32.2_test: ./../cve_builds/sqlite-3.32.2/sqlite3.c:132040: int multiSelectOrderBy(Parse *, Select *, SelectDest *): Assertion `pItem->u.x.iOrderByCol>0' failed.
```


### CVE-2020-9327

**3.31.1** (UBSan): L142594 `` — member access within null pointer of type 'Table' (aka 'struct Table')
```
../cve_builds/sqlite-3.31.1/sqlite3.c:142594:32: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:142594:32 in
```


## 6. Per-Bug-Class Detail

### BC001: null pointer in sqlite3ExprCodeTarget

- **CVE match:** CVE-2020-13435 → MATCH (versions: 3.26.0, 3.27.0, 3.27.1)
  - BC range: 3.26.0--3.32.0 (10 ver.), CVE range: 3.26.0--3.32.0 (10 ver.)
- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 3 hashes, 7222 total crashes

#### Sanitizer (test) crashes

**3.26.0** — SIGABRT L125875 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.26.0_test: ./../../cve_builds/sqlite-3.26.0/sqlite3.c:125875: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.0** — SIGABRT L126309 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.0_test: ./../../cve_builds/sqlite-3.27.0/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.1** — SIGABRT L126309 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.1_test: ./../../cve_builds/sqlite-3.27.1/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.2** — SIGABRT L126295 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.2_test: ./../../cve_builds/sqlite-3.27.2/sqlite3.c:126295: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.28.0** — SIGABRT L126595 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.28.0_test: ./../../cve_builds/sqlite-3.28.0/sqlite3.c:126595: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.29.0** — SIGABRT L131002 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.29.0_test: ./../../cve_builds/sqlite-3.29.0/sqlite3.c:131002: int sqlite3Select(Parse *, Select *, SelectDest *): Assertion `pItem->addrFillSub==0' failed.
```

**3.30.0** — UBSan L101285 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:101285:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:101285:16 in
```

**3.30.1** — UBSan L101292 ``
  Error: applying zero offset to null pointer
```
../cve_builds/sqlite-3.30.1/sqlite3.c:101292:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:101292:16 in
```

**3.31.1** — UBSan L102748 ``
  Error: applying zero offset to null pointer
```
../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16 in
```

**3.32.0** — UBSan L103541 ``
  Error: applying zero offset to null pointer
```
../cve_builds/sqlite-3.32.0/sqlite3.c:103541:16: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:103541:16 in
```

#### Production (nosanit) crashes

**3.26.0** — SEGV

**3.27.0** — SEGV

**3.27.1** — SEGV

**3.27.2** — SEGV

**3.28.0** — SEGV

**3.29.0** — SEGV

**3.30.0** — SEGV

**3.30.1** — SEGV

**3.31.1** — SEGV

**3.32.0** — SEGV

---

### BC002: null pointer in sqlite3Fts5GetTokenizer

- **EBNF-Baseline:** YES (versions: 3.30.1;3.31.1;3.32.0;3.32.2, hashes: 4)
- **DBMS-Nautilus:** 4 hashes, 832 total crashes

#### Sanitizer (test) crashes

**3.26.0** — UBSan L215741 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.26.0/sqlite3.c:215741:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.26.0/sqlite3.c:215741:44 in
```

**3.27.0** — UBSan L217016 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.27.0/sqlite3.c:217016:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.0/sqlite3.c:217016:44 in
```

**3.27.1** — UBSan L217021 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.27.1/sqlite3.c:217021:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.1/sqlite3.c:217021:44 in
```

**3.27.2** — UBSan L217009 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.27.2/sqlite3.c:217009:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.2/sqlite3.c:217009:44 in
```

**3.28.0** — UBSan L218048 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.28.0/sqlite3.c:218048:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.28.0/sqlite3.c:218048:44 in
```

**3.29.0** — UBSan L218957 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.29.0/sqlite3.c:218957:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.29.0/sqlite3.c:218957:44 in
```

**3.30.0** — UBSan L220212 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:220212:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:220212:44 in
```

**3.30.1** — UBSan L220230 ``
  Error: applying non-zero offset 8 to null pointer
```
../cve_builds/sqlite-3.30.1/sqlite3.c:220230:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:220230:44 in
```

**3.31.1** — UBSan L223612 ``
  Error: applying non-zero offset 8 to null pointer
```
../cve_builds/sqlite-3.31.1/sqlite3.c:223612:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:223612:44 in
```

**3.32.0** — UBSan L224711 ``
  Error: applying non-zero offset 8 to null pointer
```
../cve_builds/sqlite-3.32.0/sqlite3.c:224711:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:224711:44 in
```

**3.32.1** — UBSan L224767 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.32.1/sqlite3.c:224767:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.32.1/sqlite3.c:224767:44 in
```

**3.32.2** — UBSan L224769 ``
  Error: applying non-zero offset 8 to null pointer
```
../cve_builds/sqlite-3.32.2/sqlite3.c:224769:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.2/sqlite3.c:224769:44 in
```

**3.32.3** — UBSan L224940 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.32.3/sqlite3.c:224940:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.32.3/sqlite3.c:224940:44 in
```

**3.33.0** — UBSan L225670 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.33.0/sqlite3.c:225670:44: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.33.0/sqlite3.c:225670:44 in
```

**3.34.0** — UBSan L226759 ``
  Error: applying non-zero offset 8 to null pointer
```
../../cve_builds/sqlite-3.34.0/sqlite3.c:226759:27: runtime error: applying non-zero offset 8 to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.34.0/sqlite3.c:226759:27 in
```

#### Production (nosanit): no crashes on any version

---

### BC003: signed integer overflow in sqlite3 str vappendf

- **CVE match:** CVE-2020-13434 → MATCH (versions: 3.26.0, 3.27.0, 3.27.1)
  - BC range: 3.26.0--3.32.0 (10 ver.), CVE range: 3.26.0--3.32.0 (10 ver.)
- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 6 hashes, 157 total crashes

#### Sanitizer (test) crashes

**3.26.0** — UBSan L27619 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.26.0/sqlite3.c:27619:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.26.0/sqlite3.c:27619:35 in
```

**3.27.0** — UBSan L27735 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.27.0/sqlite3.c:27735:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.0/sqlite3.c:27735:35 in
```

**3.27.1** — UBSan L27735 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.27.1/sqlite3.c:27735:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.1/sqlite3.c:27735:35 in
```

**3.27.2** — UBSan L27734 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.27.2/sqlite3.c:27734:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.2/sqlite3.c:27734:35 in
```

**3.28.0** — UBSan L27791 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.28.0/sqlite3.c:27791:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.28.0/sqlite3.c:27791:35 in
```

**3.29.0** — UBSan L27877 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.29.0/sqlite3.c:27877:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.29.0/sqlite3.c:27877:35 in
```

**3.30.0** — UBSan L27971 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:27971:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:27971:35 in
```

**3.30.1** — UBSan L27975 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../cve_builds/sqlite-3.30.1/sqlite3.c:27975:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:27975:35 in
```

**3.31.1** — UBSan L28528 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../cve_builds/sqlite-3.31.1/sqlite3.c:28528:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:28528:35 in
```

**3.32.0** — UBSan L28657 ``
  Error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
```
../cve_builds/sqlite-3.32.0/sqlite3.c:28657:35: runtime error: signed integer overflow: 2147483646 - -2 cannot be represented in type 'int'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:28657:35 in
```

#### Production (nosanit) crashes

**3.26.0** — SEGV

**3.27.0** — SEGV

**3.27.1** — SEGV

**3.27.2** — SEGV

**3.28.0** — SEGV

**3.29.0** — SEGV

**3.30.0** — SEGV

**3.30.1** — SEGV

**3.31.1** — SEGV

**3.32.0** — SEGV

---

### BC004: misaligned access in sqlite3WindowUnlinkFromSelect

- **EBNF-Baseline:** YES (versions: 3.30.1, hashes: 1)
- **DBMS-Nautilus:** 1 hashes, 71 total crashes

#### Sanitizer (test) crashes

**3.30.0** — UBSan L147718 ``
  Error: store to misaligned address 0xaaaaaaaaaaaaaaaa for type 'Window *' (aka 'struct Window *'), which re
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:147718:5: runtime error: store to misaligned address 0xaaaaaaaaaaaaaaaa for type 'Window *' (aka 'struct Window *'), which requires 8 byte alignment
0xaaaaaaaaaaaaaaaa: note: pointer points here
<memory cannot be printed>
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:147718:5 in
```

**3.30.1** — UBSan L147736 ``
  Error: store to misaligned address 0xaaaaaaaaaaaaaaaa for type 'Window *' (aka 'struct Window *'), which re
```
../cve_builds/sqlite-3.30.1/sqlite3.c:147736:5: runtime error: store to misaligned address 0xaaaaaaaaaaaaaaaa for type 'Window *' (aka 'struct Window *'), which requires 8 byte alignment
0xaaaaaaaaaaaaaaaa: note: pointer points here
<memory cannot be printed>
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:147736:5 in
```

#### Production (nosanit) crashes

**3.30.0** — SEGV

---

### BC005: float cast overflow in alsoAnInt

- **EBNF-Baseline:** YES (versions: 3.30.1;3.32.0, hashes: 7)
- **DBMS-Nautilus:** 10 hashes, 21 total crashes

#### Sanitizer (test) crashes

**3.30.0** — UBSan L84137 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:84137:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:84137:16 in
```

**3.30.1** — UBSan L84141 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../cve_builds/sqlite-3.30.1/sqlite3.c:84141:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:84141:16 in
```

**3.31.1** — UBSan L85071 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../cve_builds/sqlite-3.31.1/sqlite3.c:85071:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:85071:16 in
```

**3.32.0** — UBSan L85315 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../cve_builds/sqlite-3.32.0/sqlite3.c:85315:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:85315:16 in
```

**3.32.1** — UBSan L85335 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.32.1/sqlite3.c:85335:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.32.1/sqlite3.c:85335:16 in
```

**3.32.2** — UBSan L85335 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../cve_builds/sqlite-3.32.2/sqlite3.c:85335:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.2/sqlite3.c:85335:16 in
```

**3.32.3** — UBSan L85349 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.32.3/sqlite3.c:85349:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.32.3/sqlite3.c:85349:16 in
```

**3.33.0** — UBSan L85544 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.33.0/sqlite3.c:85544:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.33.0/sqlite3.c:85544:16 in
```

**3.34.0** — UBSan L85794 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.34.0/sqlite3.c:85794:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.34.0/sqlite3.c:85794:16 in
```

**3.36.0** — UBSan L86730 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.36.0/sqlite3.c:86730:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.36.0/sqlite3.c:86730:16 in
```

**3.39.1** — UBSan L88621 ``
  Error: 1.11111e+257 is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.39.1/sqlite3.c:88621:16: runtime error: 1.11111e+257 is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.39.1/sqlite3.c:88621:16 in
```

#### Production (nosanit): no crashes on any version

---

### BC006: null pointer in isAuxiliaryVtabOperator

- **CVE match:** CVE-2020-9327 → MATCH (versions: 3.31.1)
  - BC range: 3.31.1--3.31.1 (1 ver.), CVE range: 3.31.1--3.31.1 (1 ver.)
- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 1 hashes, 20 total crashes

#### Sanitizer (test) crashes

**3.31.1** — UBSan L142594 ``
  Error: member access within null pointer of type 'Table' (aka 'struct Table')
```
../cve_builds/sqlite-3.31.1/sqlite3.c:142594:32: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:142594:32 in
```

#### Production (nosanit) crashes

**3.31.1** — SEGV

---

### BC007: misaligned access in resetAccumulator

- **CVE match:** CVE-2020-13871 → MATCH (versions: 3.27.0, 3.27.1, 3.27.2)
  - BC range: 3.27.0--3.30.1 (7 ver.), CVE range: 3.27.0--3.32.0 (9 ver.)
- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 1 hashes, 13 total crashes

#### Sanitizer (test) crashes

**3.27.0** — SIGABRT L126304 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.0_test: ./../../cve_builds/sqlite-3.27.0/sqlite3.c:126304: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.27.1** — SIGABRT L126304 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.1_test: ./../../cve_builds/sqlite-3.27.1/sqlite3.c:126304: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.27.2** — SIGABRT L126290 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.2_test: ./../../cve_builds/sqlite-3.27.2/sqlite3.c:126290: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.28.0** — SIGABRT L126590 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.28.0_test: ./../../cve_builds/sqlite-3.28.0/sqlite3.c:126590: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.29.0** — SIGABRT L127111 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.29.0_test: ./../../cve_builds/sqlite-3.29.0/sqlite3.c:127111: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pColExpr->op!=TK_AGG_COLUMN' failed.
```

**3.30.0** — UBSan L130912 ``
  Error: member access within misaligned address 0xaaaaaaaaaaaaaaaa for type 'ExprList' (aka 'struct ExprList
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:130912:42: runtime error: member access within misaligned address 0xaaaaaaaaaaaaaaaa for type 'ExprList' (aka 'struct ExprList'), which requires 8 byte alignment
0xaaaaaaaaaaaaaaaa: note: pointer points here
<memory cannot be printed>
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:130912:42 in
```

**3.30.1** — UBSan L130930 ``
  Error: member access within misaligned address 0xaaaaaaaaaaaaaaaa for type 'ExprList' (aka 'struct ExprList
```
../cve_builds/sqlite-3.30.1/sqlite3.c:130930:42: runtime error: member access within misaligned address 0xaaaaaaaaaaaaaaaa for type 'ExprList' (aka 'struct ExprList'), which requires 8 byte alignment
0xaaaaaaaaaaaaaaaa: note: pointer points here
<memory cannot be printed>
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:130930:42 in
```

#### Production (nosanit): no crashes on any version

---

### BC008: misaligned access in sqlite3ExprCodeTarget

- **CVE match:** NONE (same assertion line as CVE-2020-13435 on 3.26.0 but different error type on 3.30.1+: ASan SEGV / misaligned access vs null pointer)
- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 13 hashes, 13 total crashes

#### Sanitizer (test) crashes

**3.26.0** — SIGABRT L125875 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.26.0_test: ./../../cve_builds/sqlite-3.26.0/sqlite3.c:125875: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.0** — SIGABRT L126309 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.0_test: ./../../cve_builds/sqlite-3.27.0/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.1** — SIGABRT L126309 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.1_test: ./../../cve_builds/sqlite-3.27.1/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.2** — SIGABRT L126295 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.2_test: ./../../cve_builds/sqlite-3.27.2/sqlite3.c:126295: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.28.0** — SIGABRT L126595 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.28.0_test: ./../../cve_builds/sqlite-3.28.0/sqlite3.c:126595: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.29.0** — SIGABRT L131002 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.29.0_test: ./../../cve_builds/sqlite-3.29.0/sqlite3.c:131002: int sqlite3Select(Parse *, Select *, SelectDest *): Assertion `pItem->addrFillSub==0' failed.
```

**3.30.0** — ASan L101285 `sqlite3ExprCodeTarget`
  Error: SEGV
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==111602==ERROR: AddressSanitizer: SEGV on unknown address 0x000c5854dc4b (pc 0xc7abc276d868 bp 0xffffe0b0cae0 sp 0xffffe0b0c7c0 T0)
==111602==The signal is caused by a READ memory access.
    #0 0xc7abc276d868 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101285:42
    #1 0xc7abc2774f58 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101917:19
    #2 0xc7abc27c4200 in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126162:3
    #3 0xc7abc27c4200 in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126614:7
    #4 0xc7abc2741ce8 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131797:7
    #5 0xc7abc2740808 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131578:7
    #6 0xc7abc2740808 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131578:7
    #7 0xc7abc27764f4 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:100493:7
    #8 0xc7abc276d450 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101465:16
    #9 0xc7abc2774f58 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101917:19
    #10 0xc7abc27c4200 in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126162:3
    #11 0xc7abc27c4200 in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126614:7
    #12 0xc7abc27438b0 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:132274:7
    #13 0xc7abc27764f4 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:100493:7
    #14 0xc7abc276d450 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101465:16
    #15 0xc7abc276ae20 in sqlite3ExprCode /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101803:13
... (22 more lines)
```

**3.30.1** — ASan L101292 `sqlite3ExprCodeTarget`
  Error: SEGV
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==111607==ERROR: AddressSanitizer: SEGV on unknown address 0x000c56465c4b (pc 0xb964b202d474 bp 0xffffc948af20 sp 0xffffc948ac00 T0)
==111607==The signal is caused by a READ memory access.
    #0 0xb964b202d474 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101292:42
    #1 0xb964b2034b64 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101924:19
    #2 0xb964b2083e0c in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126172:3
    #3 0xb964b2083e0c in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126624:7
    #4 0xb964b20018f0 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131815:7
    #5 0xb964b2000410 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131596:7
    #6 0xb964b2000410 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131596:7
    #7 0xb964b2036100 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:100500:7
    #8 0xb964b202d05c in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101472:16
    #9 0xb964b2034b64 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101924:19
    #10 0xb964b2083e0c in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126172:3
    #11 0xb964b2083e0c in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126624:7
    #12 0xb964b20034b8 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:132292:7
    #13 0xb964b2036100 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:100500:7
    #14 0xb964b202d05c in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101472:16
    #15 0xb964b202aa30 in sqlite3ExprCode /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101810:13
... (22 more lines)
```

**3.31.1** — UBSan L102748 ``
  Error: member access within misaligned address 0x1ffffcaaaf0b for type 'struct AggInfo_func', which require
```
../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16: runtime error: member access within misaligned address 0x1ffffcaaaf0b for type 'struct AggInfo_func', which requires 8 byte alignment
0x1ffffcaaaf0b: note: pointer points here
 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00
              ^ 
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16 in
```

#### Production (nosanit) crashes

**3.26.0** — SEGV

**3.27.0** — SEGV

**3.27.1** — SEGV

**3.27.2** — SEGV

**3.28.0** — SEGV

**3.29.0** — SEGV

**3.30.0** — SEGV

**3.30.1** — SEGV

**3.31.1** — SEGV

**3.32.0** — SEGV

---

### BC009: float cast overflow in sqlite3VdbeMemNumerify

- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 2 hashes, 6 total crashes

#### Sanitizer (test) crashes

**3.31.1** — UBSan L76157 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../cve_builds/sqlite-3.31.1/sqlite3.c:76157:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:76157:47 in
```

**3.32.0** — UBSan L76346 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../cve_builds/sqlite-3.32.0/sqlite3.c:76346:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:76346:47 in
```

**3.32.1** — UBSan L76366 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.32.1/sqlite3.c:76366:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.32.1/sqlite3.c:76366:47 in
```

**3.32.2** — UBSan L76366 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../cve_builds/sqlite-3.32.2/sqlite3.c:76366:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.2/sqlite3.c:76366:47 in
```

**3.32.3** — UBSan L76380 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.32.3/sqlite3.c:76380:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.32.3/sqlite3.c:76380:47 in
```

**3.33.0** — UBSan L76569 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.33.0/sqlite3.c:76569:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.33.0/sqlite3.c:76569:47 in
```

**3.34.0** — UBSan L76815 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.34.0/sqlite3.c:76815:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.34.0/sqlite3.c:76815:47 in
```

**3.36.0** — UBSan L77740 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.36.0/sqlite3.c:77740:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.36.0/sqlite3.c:77740:47 in
```

**3.39.1** — UBSan L79455 ``
  Error: inf is outside the range of representable values of type 'long long'
```
../../cve_builds/sqlite-3.39.1/sqlite3.c:79455:47: runtime error: inf is outside the range of representable values of type 'long long'
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.39.1/sqlite3.c:79455:47 in
```

#### Production (nosanit): no crashes on any version

---

### BC010: null pointer in sqlite3Select

- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 2 hashes, 5 total crashes

#### Sanitizer (test) crashes

**3.30.0** — UBSan L131370 ``
  Error: member access within null pointer of type 'Table' (aka 'struct Table')
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:131370:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:131370:15 in
```

**3.30.1** — UBSan L131388 ``
  Error: member access within null pointer of type 'Table' (aka 'struct Table')
```
../cve_builds/sqlite-3.30.1/sqlite3.c:131388:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:131388:15 in
```

**3.31.1** — UBSan L133698 ``
  Error: member access within null pointer of type 'Table' (aka 'struct Table')
```
../cve_builds/sqlite-3.31.1/sqlite3.c:133698:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:133698:15 in
```

**3.32.0** — UBSan L134653 ``
  Error: member access within null pointer of type 'Table' (aka 'struct Table')
```
../cve_builds/sqlite-3.32.0/sqlite3.c:134653:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.0/sqlite3.c:134653:15 in
```

**3.32.1** — UBSan L134686 ``
  Error: member access within null pointer of type 'Table' (aka 'struct Table')
```
../../cve_builds/sqlite-3.32.1/sqlite3.c:134686:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.32.1/sqlite3.c:134686:15 in
```

**3.32.2** — UBSan L134688 ``
  Error: member access within null pointer of type 'Table' (aka 'struct Table')
```
../cve_builds/sqlite-3.32.2/sqlite3.c:134688:15: runtime error: member access within null pointer of type 'Table' (aka 'struct Table')
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.32.2/sqlite3.c:134688:15 in
```

#### Production (nosanit) crashes

**3.30.0** — SEGV

**3.30.1** — SEGV

**3.31.1** — SEGV

**3.32.0** — SEGV

**3.32.1** — SEGV

**3.32.2** — SEGV

---

### BC011: signal 6 in sqlite3WindowListDelete

- **EBNF-Baseline:** YES (versions: 3.30.1, hashes: 2)
- **DBMS-Nautilus:** 2 hashes, 5 total crashes

#### Sanitizer (test) crashes

**3.26.0** — ASan L145418 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111848==ERROR: AddressSanitizer: heap-use-after-free on address 0xf531e6c029b8 at pc 0xaf146723282c bp 0xfffff0224ff0 sp 0xfffff0224fe8
READ of size 8 at 0xf531e6c029b8 thread T0
    #0 0xaf1467232828 in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:145418:24
    #1 0xaf1467232828 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:124008:7
    #2 0xaf1467231fe8 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:124094:30
    #3 0xaf1467231fe8 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:97188:7
    #4 0xaf1467231ecc in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:97186:7
    #5 0xaf14672326e4 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:97203:11
    #6 0xaf14672326e4 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:124005:5
    #7 0xaf1467231fe8 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:124094:30
    #8 0xaf1467231fe8 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:97188:7
    #9 0xaf14672330d8 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:97203:11
    #10 0xaf14672330d8 in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:97843:5
    #11 0xaf14672429a4 in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:97851:15
    #12 0xaf14672429a4 in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:106572:3
    #13 0xaf14670f5440 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:106585:3
    #14 0xaf14671327d0 in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:152313:5
    #15 0xaf146712d4bc in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:123309:5
    #16 0xaf146712d4bc in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.26.0/sqlite3.c:123402:10
... (97 more lines)
```

**3.27.0** — ASan L145925 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111853==ERROR: AddressSanitizer: heap-use-after-free on address 0xf7ef70e029b8 at pc 0xc268a3707168 bp 0xffffeba117d0 sp 0xffffeba117c8
READ of size 8 at 0xf7ef70e029b8 thread T0
    #0 0xc268a3707164 in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:145925:24
    #1 0xc268a3707164 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:124436:7
    #2 0xc268a3706920 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:124522:30
    #3 0xc268a3706920 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:97702:7
    #4 0xc268a3706804 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:97700:7
    #5 0xc268a3707020 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:97717:11
    #6 0xc268a3707020 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:124433:5
    #7 0xc268a3706920 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:124522:30
    #8 0xc268a3706920 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:97702:7
    #9 0xc268a3707a14 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:97717:11
    #10 0xc268a3707a14 in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:98401:5
    #11 0xc268a3717364 in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:98409:15
    #12 0xc268a3717364 in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:107243:3
    #13 0xc268a35c8080 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:107256:3
    #14 0xc268a36055d4 in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:153149:5
    #15 0xc268a3600220 in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:124024:5
    #16 0xc268a3600220 in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.0/sqlite3.c:124117:10
... (97 more lines)
```

**3.27.1** — ASan L145930 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111858==ERROR: AddressSanitizer: heap-use-after-free on address 0xf26e126029b8 at pc 0xbdc2b5297160 bp 0xffffe3ff7ad0 sp 0xffffe3ff7ac8
READ of size 8 at 0xf26e126029b8 thread T0
    #0 0xbdc2b529715c in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:145930:24
    #1 0xbdc2b529715c in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:124436:7
    #2 0xbdc2b5296918 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:124522:30
    #3 0xbdc2b5296918 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:97702:7
    #4 0xbdc2b52967fc in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:97700:7
    #5 0xbdc2b5297018 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:97717:11
    #6 0xbdc2b5297018 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:124433:5
    #7 0xbdc2b5296918 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:124522:30
    #8 0xbdc2b5296918 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:97702:7
    #9 0xbdc2b5297a0c in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:97717:11
    #10 0xbdc2b5297a0c in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:98401:5
    #11 0xbdc2b52a735c in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:98409:15
    #12 0xbdc2b52a735c in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:107243:3
    #13 0xbdc2b5158080 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:107256:3
    #14 0xbdc2b51955d0 in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:153154:5
    #15 0xbdc2b519021c in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:124024:5
    #16 0xbdc2b519021c in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.1/sqlite3.c:124117:10
... (97 more lines)
```

**3.27.2** — ASan L145918 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111863==ERROR: AddressSanitizer: heap-use-after-free on address 0xe5b2a16029b8 at pc 0xc25aadff6d80 bp 0xffffd1dbdc30 sp 0xffffd1dbdc28
READ of size 8 at 0xe5b2a16029b8 thread T0
    #0 0xc25aadff6d7c in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:145918:24
    #1 0xc25aadff6d7c in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:124422:7
    #2 0xc25aadff653c in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:124508:30
    #3 0xc25aadff653c in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:97711:7
    #4 0xc25aadff6420 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:97709:7
    #5 0xc25aadff6c38 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:97726:11
    #6 0xc25aadff6c38 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:124419:5
    #7 0xc25aadff653c in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:124508:30
    #8 0xc25aadff653c in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:97711:7
    #9 0xc25aadff762c in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:97726:11
    #10 0xc25aadff762c in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:98410:5
    #11 0xc25aae006f68 in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:98418:15
    #12 0xc25aae006f68 in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:107226:3
    #13 0xc25aadeb7e00 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:107239:3
    #14 0xc25aadef5370 in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:153142:5
    #15 0xc25aadeeffbc in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:124010:5
    #16 0xc25aadeeffbc in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.27.2/sqlite3.c:124103:10
... (97 more lines)
```

**3.28.0** — ASan L146427 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111868==ERROR: AddressSanitizer: heap-use-after-free on address 0xe92d73402850 at pc 0xc9afae0bc640 bp 0xffffc7fac690 sp 0xffffc7fac688
READ of size 8 at 0xe92d73402850 thread T0
    #0 0xc9afae0bc63c in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:146427:24
    #1 0xc9afae0bc63c in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:124722:7
    #2 0xc9afae0bbdb0 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:124808:30
    #3 0xc9afae0bbdb0 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:97962:7
    #4 0xc9afae0bbc94 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:97960:7
    #5 0xc9afae0bc4f8 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:97977:11
    #6 0xc9afae0bc4f8 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:124719:5
    #7 0xc9afae0bbdb0 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:124808:30
    #8 0xc9afae0bbdb0 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:97962:7
    #9 0xc9afae0bceec in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:97977:11
    #10 0xc9afae0bceec in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:98661:5
    #11 0xc9afae0cc914 in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:98669:15
    #12 0xc9afae0cc914 in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:107495:3
    #13 0xc9afadf7bd40 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:107508:3
    #14 0xc9afadfb95dc in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:154067:5
    #15 0xc9afadfb41a0 in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:124310:5
    #16 0xc9afadfb41a0 in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.28.0/sqlite3.c:124403:10
... (97 more lines)
```

**3.29.0** — ASan L147003 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111873==ERROR: AddressSanitizer: heap-use-after-free on address 0xe811be802850 at pc 0xb7fffb840c54 bp 0xffffd42986d0 sp 0xffffd42986c8
READ of size 8 at 0xe811be802850 thread T0
    #0 0xb7fffb840c50 in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:147003:24
    #1 0xb7fffb840c50 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:125243:7
    #2 0xb7fffb8403c8 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:125329:30
    #3 0xb7fffb8403c8 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:98259:7
    #4 0xb7fffb8402ac in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:98257:7
    #5 0xb7fffb840b0c in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:98274:11
    #6 0xb7fffb840b0c in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:125240:5
    #7 0xb7fffb8403c8 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:125329:30
    #8 0xb7fffb8403c8 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:98259:7
    #9 0xb7fffb841500 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:98274:11
    #10 0xb7fffb841500 in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:98967:5
    #11 0xb7fffb850f54 in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:98975:15
    #12 0xb7fffb850f54 in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:107943:3
    #13 0xb7fffb6fef00 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:107956:3
    #14 0xb7fffb73c488 in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:154651:5
    #15 0xb7fffb737054 in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:124831:5
    #16 0xb7fffb737054 in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.29.0/sqlite3.c:124924:10
... (97 more lines)
```

**3.30.0** — ASan L147746 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111878==ERROR: AddressSanitizer: heap-use-after-free on address 0xfd6223803508 at pc 0xaf6369ee8b38 bp 0xffffdbb37260 sp 0xffffdbb37258
READ of size 8 at 0xfd6223803508 thread T0
    #0 0xaf6369ee8b34 in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:147746:24
    #1 0xaf6369ee8b34 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125711:7
    #2 0xaf6369ee8220 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125798:30
    #3 0xaf6369ee8220 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:98564:7
    #4 0xaf6369ee812c in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:98561:7
    #5 0xaf6369ee8990 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:98580:11
    #6 0xaf6369ee8990 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125708:5
    #7 0xaf6369ee8220 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125798:30
    #8 0xaf6369ee8220 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:98564:7
    #9 0xaf6369ee9544 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:98580:11
    #10 0xaf6369ee9544 in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:99290:5
    #11 0xaf6369ef9040 in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:99298:15
    #12 0xaf6369ef9040 in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:108303:3
    #13 0xaf6369da53c0 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:108316:3
    #14 0xaf6369de2c70 in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:155672:5
    #15 0xaf6369ddd58c in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125296:5
    #16 0xaf6369ddd58c in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:125392:10
... (97 more lines)
```

**3.30.1** — ASan L147764 `sqlite3WindowListDelete`
  Error: heap-use-after-free
```
=================================================================
==111883==ERROR: AddressSanitizer: heap-use-after-free on address 0xf8e99ea03508 at pc 0xc158cf7f8778 bp 0xffffc63f7a40 sp 0xffffc63f7a38
READ of size 8 at 0xf8e99ea03508 thread T0
    #0 0xc158cf7f8774 in sqlite3WindowListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:147764:24
    #1 0xc158cf7f8774 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125721:7
    #2 0xc158cf7f7e54 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125808:30
    #3 0xc158cf7f7e54 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:98571:7
    #4 0xc158cf7f7d60 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:98568:7
    #5 0xc158cf7f85d0 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:98587:11
    #6 0xc158cf7f85d0 in clearSelect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125718:5
    #7 0xc158cf7f7e54 in sqlite3SelectDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125808:30
    #8 0xc158cf7f7e54 in sqlite3ExprDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:98571:7
    #9 0xc158cf7f9184 in sqlite3ExprDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:98587:11
    #10 0xc158cf7f9184 in exprListDeleteNN /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:99297:5
    #11 0xc158cf808c84 in sqlite3ExprListDelete /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:99305:15
    #12 0xc158cf808c84 in deleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:108313:3
    #13 0xc158cf6b54c0 in sqlite3DeleteTable /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:108326:3
    #14 0xc158cf6f2d8c in sqlite3RunParser /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:155690:5
    #15 0xc158cf6ed6a8 in sqlite3Prepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125306:5
    #16 0xc158cf6ed6a8 in sqlite3LockAndPrepare /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:125402:10
... (97 more lines)
```

#### Production (nosanit) crashes

**3.26.0** — SEGV

**3.27.0** — SEGV

**3.27.1** — SEGV

**3.27.2** — SEGV

**3.28.0** — SEGV

**3.29.0** — SEGV

**3.30.0** — SEGV

**3.30.1** — SEGV

---

### BC012: null pointer in sqlite3Atoi64

- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 2 hashes, 4 total crashes

#### Sanitizer (test) crashes

**3.26.0** — UBSan L30603 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.26.0/sqlite3.c:30603:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.26.0/sqlite3.c:30603:27 in
```

**3.27.0** — UBSan L30722 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.27.0/sqlite3.c:30722:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.0/sqlite3.c:30722:27 in
```

**3.27.1** — UBSan L30722 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.27.1/sqlite3.c:30722:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.1/sqlite3.c:30722:27 in
```

**3.27.2** — UBSan L30721 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.27.2/sqlite3.c:30721:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.27.2/sqlite3.c:30721:27 in
```

**3.28.0** — UBSan L30836 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.28.0/sqlite3.c:30836:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.28.0/sqlite3.c:30836:27 in
```

**3.29.0** — UBSan L30910 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.29.0/sqlite3.c:30910:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.29.0/sqlite3.c:30910:27 in
```

**3.30.0** — UBSan L31020 ``
  Error: applying zero offset to null pointer
```
../../cve_builds/sqlite-3.30.0/sqlite3.c:31020:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../../cve_builds/sqlite-3.30.0/sqlite3.c:31020:27 in
```

**3.30.1** — UBSan L31024 ``
  Error: applying zero offset to null pointer
```
../cve_builds/sqlite-3.30.1/sqlite3.c:31024:27: runtime error: applying zero offset to null pointer
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.30.1/sqlite3.c:31024:27 in
```

#### Production (nosanit) crashes

**3.26.0** — SEGV

**3.27.0** — SEGV

**3.27.1** — SEGV

**3.27.2** — SEGV

**3.28.0** — SEGV

---

### BC013: signal 6 in sqlite3ExprCodeTarget

- **CVE match:** NONE (same assertion line as CVE-2020-13435 on 3.26.0 but different error type on 3.30.1+: ASan SEGV vs null pointer)
- **EBNF-Baseline:** not found
- **DBMS-Nautilus:** 1 hashes, 1 total crashes

#### Sanitizer (test) crashes

**3.26.0** — SIGABRT L125875 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.26.0_test: ./../../cve_builds/sqlite-3.26.0/sqlite3.c:125875: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.0** — SIGABRT L126309 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.0_test: ./../../cve_builds/sqlite-3.27.0/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.1** — SIGABRT L126309 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.1_test: ./../../cve_builds/sqlite-3.27.1/sqlite3.c:126309: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.27.2** — SIGABRT L126295 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.27.2_test: ./../../cve_builds/sqlite-3.27.2/sqlite3.c:126295: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.28.0** — SIGABRT L126595 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.28.0_test: ./../../cve_builds/sqlite-3.28.0/sqlite3.c:126595: int sqlite3ColumnsFromExprList(Parse *, ExprList *, i16 *, Column **): Assertion `pTab!=0' failed.
```

**3.29.0** — SIGABRT L131002 ``
  Error: SIGABRT
```
sqlite_harness_sqlite-3.29.0_test: ./../../cve_builds/sqlite-3.29.0/sqlite3.c:131002: int sqlite3Select(Parse *, Select *, SelectDest *): Assertion `pItem->addrFillSub==0' failed.
```

**3.30.0** — ASan L101285 `sqlite3ExprCodeTarget`
  Error: SEGV
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==112060==ERROR: AddressSanitizer: SEGV on unknown address 0x000c59c4fc4b (pc 0xadcdcdf7d868 bp 0xffffca23a060 sp 0xffffca239d40 T0)
==112060==The signal is caused by a READ memory access.
    #0 0xadcdcdf7d868 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101285:42
    #1 0xadcdcdf84f58 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101917:19
    #2 0xadcdcdfd4200 in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126162:3
    #3 0xadcdcdfd4200 in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126614:7
    #4 0xadcdcdf51ce8 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131797:7
    #5 0xadcdcdf50808 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131578:7
    #6 0xadcdcdf50808 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:131578:7
    #7 0xadcdcdf864f4 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:100493:7
    #8 0xadcdcdf7d450 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101465:16
    #9 0xadcdcdf84f58 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101917:19
    #10 0xadcdcdfd4200 in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126162:3
    #11 0xadcdcdfd4200 in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:126614:7
    #12 0xadcdcdf538b0 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:132274:7
    #13 0xadcdcdf864f4 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:100493:7
    #14 0xadcdcdf7d450 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101465:16
    #15 0xadcdcdf7ae20 in sqlite3ExprCode /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/src/./../../cve_builds/sqlite-3.30.0/sqlite3.c:101803:13
... (22 more lines)
```

**3.30.1** — ASan L101292 `sqlite3ExprCodeTarget`
  Error: SEGV
```
AddressSanitizer:DEADLYSIGNAL
=================================================================
==112065==ERROR: AddressSanitizer: SEGV on unknown address 0x000c45a93c4b (pc 0xb6122d19d474 bp 0xfffffd06b320 sp 0xfffffd06b000 T0)
==112065==The signal is caused by a READ memory access.
    #0 0xb6122d19d474 in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101292:42
    #1 0xb6122d1a4b64 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101924:19
    #2 0xb6122d1f3e0c in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126172:3
    #3 0xb6122d1f3e0c in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126624:7
    #4 0xb6122d1718f0 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131815:7
    #5 0xb6122d170410 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131596:7
    #6 0xb6122d170410 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:131596:7
    #7 0xb6122d1a6100 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:100500:7
    #8 0xb6122d19d05c in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101472:16
    #9 0xb6122d1a4b64 in sqlite3ExprCodeExprList /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101924:19
    #10 0xb6122d1f3e0c in innerLoopLoadRow /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126172:3
    #11 0xb6122d1f3e0c in selectInnerLoop /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:126624:7
    #12 0xb6122d1734b8 in sqlite3Select /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:132292:7
    #13 0xb6122d1a6100 in sqlite3CodeSubselect /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:100500:7
    #14 0xb6122d19d05c in sqlite3ExprCodeTarget /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101472:16
    #15 0xb6122d19aa30 in sqlite3ExprCode /home/kienbeovl/Desktop/claude-code-fuzzing/rl-nautilus-phase-2/harness/./../cve_builds/sqlite-3.30.1/sqlite3.c:101810:13
... (22 more lines)
```

**3.31.1** — UBSan L102748 ``
  Error: member access within misaligned address 0x1ffffcb1ce37 for type 'struct AggInfo_func', which require
```
../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16: runtime error: member access within misaligned address 0x1ffffcb1ce37 for type 'struct AggInfo_func', which requires 8 byte alignment
0x1ffffcb1ce37: note: pointer points here
 00 00 00 00 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  00 00 00 00 00 00 00 00  00 00 00
             ^ 
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior ../cve_builds/sqlite-3.31.1/sqlite3.c:102748:16 in
```

#### Production (nosanit) crashes

**3.26.0** — SEGV

**3.27.0** — SEGV

**3.27.1** — SEGV

**3.27.2** — SEGV

**3.28.0** — SEGV

**3.29.0** — SEGV

**3.30.0** — SEGV

**3.30.1** — SEGV

**3.31.1** — SEGV

**3.32.0** — SEGV

---

## 7. Flags for Human Review

- **BC001 ↔ CVE-2020-13435**: MATCH confirmed — BC range: 3.26.0--3.32.0 (10 ver.), CVE range: 3.26.0--3.32.0 (10 ver.)
- **BC003 ↔ CVE-2020-13434**: MATCH confirmed — BC range: 3.26.0--3.32.0 (10 ver.), CVE range: 3.26.0--3.32.0 (10 ver.)
- **BC006 ↔ CVE-2020-9327**: MATCH confirmed — BC range: 3.31.1--3.31.1 (1 ver.), CVE range: 3.31.1--3.31.1 (1 ver.)
- **BC007 ↔ CVE-2020-13871**: MATCH confirmed — BC range: 3.27.0--3.30.1 (7 ver.), CVE range: 3.27.0--3.32.0 (9 ver.)
- **BC008 ↔ CVE-2020-13435**: REJECTED — same assertion line on old versions (3.26.0) but different error type on target versions (ASan SEGV / misaligned access vs null pointer). Different bug.
- **BC013 ↔ CVE-2020-13435**: REJECTED — same assertion line on old versions (3.26.0) but different error type on target versions (ASan SEGV vs null pointer). Different bug.

---
*Generated by `scripts/rq2_source_of_truth.py` at 2026-05-23T12:24:12.535836*