# Bug Verification Matrix Report

Generated: 2026-05-22T23:26:26+07:00

- **Bug classes tested:** 13
- **SQLite versions:** 19 (3.26.0 -- 3.53.0)
- **Total test runs:** 494

## Classification Summary

| Category | Count | Bug Classes |
|----------|-------|-------------|
| Known CVE | 3 | BC003, BC004, BC010 |
| Sanitizer-only | 5 | BC002, BC005, BC007, BC009, BC012 |
| Silently fixed | 5 | BC001, BC006, BC008, BC011, BC013 |

## Per-Bug Detail

### BC001: sqlite3ExprCodeTarget (null-pointer)

- **Classification:** Silently fixed
- **Exploitability:** SEGV on nosanit = potentially exploitable
- **Fix version:** 3.32.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | **SIGABRT** | **SEGV** |
| 3.27.0 | **SIGABRT** | **SEGV** |
| 3.27.1 | **SIGABRT** | **SEGV** |
| 3.27.2 | **SIGABRT** | **SEGV** |
| 3.28.0 | **SIGABRT** | **SEGV** |
| 3.29.0 | **SIGABRT** | **SEGV** |
| 3.30.0 | **UBSan** | **SEGV** |
| 3.30.1 | **UBSan** | **SEGV** |
| 3.31.1 | **UBSan** | **SEGV** |
| 3.32.0 | **UBSan** | **SEGV** |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC002: sqlite3Fts5GetTokenizer (null-pointer)

- **Classification:** Sanitizer-only
- **Exploitability:** sanitizer-only detection, no production impact
- **Fix version:** 3.36.0

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | **UBSan** | OK |
| 3.27.0 | **UBSan** | OK |
| 3.27.1 | **UBSan** | OK |
| 3.27.2 | **UBSan** | OK |
| 3.28.0 | **UBSan** | OK |
| 3.29.0 | **UBSan** | OK |
| 3.30.0 | **UBSan** | OK |
| 3.30.1 | **UBSan** | OK |
| 3.31.1 | **UBSan** | OK |
| 3.32.0 | **UBSan** | OK |
| 3.32.1 | **UBSan** | OK |
| 3.32.2 | **UBSan** | OK |
| 3.32.3 | **UBSan** | OK |
| 3.33.0 | **UBSan** | OK |
| 3.34.0 | **UBSan** | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC003: sqlite3_str_vappendf (signed-integer-overflow) \[CVE-2020-13434\]

- **Classification:** Known CVE
- **Exploitability:** sanitizer-only detection, no production impact
- **Fix version:** 3.32.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | OK | OK |
| 3.27.1 | OK | OK |
| 3.27.2 | OK | OK |
| 3.28.0 | OK | OK |
| 3.29.0 | **UBSan** | OK |
| 3.30.0 | **UBSan** | OK |
| 3.30.1 | **UBSan** | OK |
| 3.31.1 | **UBSan** | OK |
| 3.32.0 | **UBSan** | OK |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC004: sqlite3WindowUnlinkFromSelect (misaligned-access) \[CVE-2020-13871\]

- **Classification:** Known CVE
- **Exploitability:** SEGV on nosanit = potentially exploitable
- **Fix version:** 3.31.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | OK | OK |
| 3.27.1 | OK | OK |
| 3.27.2 | OK | OK |
| 3.28.0 | OK | OK |
| 3.29.0 | OK | OK |
| 3.30.0 | **UBSan** | OK |
| 3.30.1 | **UBSan** | **SEGV** |
| 3.31.1 | OK | OK |
| 3.32.0 | OK | OK |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC005: alsoAnInt (float-cast-overflow)

- **Classification:** Sanitizer-only
- **Exploitability:** sanitizer-only detection, no production impact
- **Fix version:** 3.40.0

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | OK | OK |
| 3.27.1 | OK | OK |
| 3.27.2 | OK | OK |
| 3.28.0 | OK | OK |
| 3.29.0 | **UBSan** | OK |
| 3.30.0 | **UBSan** | OK |
| 3.30.1 | **UBSan** | OK |
| 3.31.1 | **UBSan** | OK |
| 3.32.0 | **UBSan** | OK |
| 3.32.1 | **UBSan** | OK |
| 3.32.2 | **UBSan** | OK |
| 3.32.3 | **UBSan** | OK |
| 3.33.0 | **UBSan** | OK |
| 3.34.0 | **UBSan** | OK |
| 3.36.0 | **UBSan** | OK |
| 3.39.1 | **UBSan** | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC006: isAuxiliaryVtabOperator (null-pointer)

- **Classification:** Silently fixed
- **Exploitability:** SEGV on nosanit = potentially exploitable
- **Fix version:** 3.32.0

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | OK | OK |
| 3.27.1 | OK | OK |
| 3.27.2 | OK | OK |
| 3.28.0 | OK | OK |
| 3.29.0 | OK | OK |
| 3.30.0 | OK | OK |
| 3.30.1 | OK | OK |
| 3.31.1 | **UBSan** | **SEGV** |
| 3.32.0 | OK | OK |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC007: resetAccumulator (misaligned-access)

- **Classification:** Sanitizer-only
- **Exploitability:** sanitizer-only detection, no production impact
- **Fix version:** 3.31.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | **SIGABRT** | OK |
| 3.27.1 | **SIGABRT** | OK |
| 3.27.2 | **SIGABRT** | OK |
| 3.28.0 | **SIGABRT** | OK |
| 3.29.0 | **SIGABRT** | OK |
| 3.30.0 | **UBSan** | OK |
| 3.30.1 | **UBSan** | OK |
| 3.31.1 | OK | OK |
| 3.32.0 | OK | OK |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC008: sqlite3ExprCodeTarget (misaligned-access)

- **Classification:** Silently fixed
- **Exploitability:** SEGV on nosanit = potentially exploitable
- **Fix version:** 3.32.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | **SIGABRT** | **SEGV** |
| 3.27.0 | **SIGABRT** | **SEGV** |
| 3.27.1 | **SIGABRT** | **SEGV** |
| 3.27.2 | **SIGABRT** | **SEGV** |
| 3.28.0 | **SIGABRT** | **SEGV** |
| 3.29.0 | **SIGABRT** | OK |
| 3.30.0 | **UBSan** | **SEGV** |
| 3.30.1 | **UBSan** | **SEGV** |
| 3.31.1 | **UBSan** | **SEGV** |
| 3.32.0 | OK | **SEGV** |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC009: sqlite3VdbeMemNumerify (float-cast-overflow)

- **Classification:** Sanitizer-only
- **Exploitability:** sanitizer-only detection, no production impact
- **Fix version:** 3.40.0

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | OK | OK |
| 3.27.1 | OK | OK |
| 3.27.2 | OK | OK |
| 3.28.0 | OK | OK |
| 3.29.0 | OK | OK |
| 3.30.0 | OK | OK |
| 3.30.1 | OK | OK |
| 3.31.1 | **UBSan** | OK |
| 3.32.0 | **UBSan** | OK |
| 3.32.1 | **UBSan** | OK |
| 3.32.2 | **UBSan** | OK |
| 3.32.3 | **UBSan** | OK |
| 3.33.0 | **UBSan** | OK |
| 3.34.0 | **UBSan** | OK |
| 3.36.0 | **UBSan** | OK |
| 3.39.1 | **UBSan** | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC010: sqlite3Select (null-pointer) \[CVE-2020-9327\]

- **Classification:** Known CVE
- **Exploitability:** SEGV on nosanit = potentially exploitable
- **Fix version:** 3.32.3

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | OK | OK |
| 3.27.1 | OK | OK |
| 3.27.2 | OK | OK |
| 3.28.0 | OK | OK |
| 3.29.0 | OK | OK |
| 3.30.0 | **UBSan** | **SEGV** |
| 3.30.1 | **UBSan** | **SEGV** |
| 3.31.1 | **UBSan** | **SEGV** |
| 3.32.0 | **UBSan** | **SEGV** |
| 3.32.1 | **UBSan** | **SEGV** |
| 3.32.2 | **UBSan** | **SEGV** |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC011: sqlite3WindowListDelete (signal-6)

- **Classification:** Silently fixed
- **Exploitability:** SEGV on nosanit = potentially exploitable
- **Fix version:** 3.31.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | OK | OK |
| 3.27.0 | OK | OK |
| 3.27.1 | OK | OK |
| 3.27.2 | OK | OK |
| 3.28.0 | OK | OK |
| 3.29.0 | OK | OK |
| 3.30.0 | **UBSan** | **SEGV** |
| 3.30.1 | **UBSan** | **SEGV** |
| 3.31.1 | OK | OK |
| 3.32.0 | OK | OK |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC012: sqlite3Atoi64 (null-pointer)

- **Classification:** Sanitizer-only
- **Exploitability:** sanitizer-only detection, no production impact
- **Fix version:** 3.31.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | **UBSan** | OK |
| 3.27.0 | **UBSan** | OK |
| 3.27.1 | **UBSan** | OK |
| 3.27.2 | **UBSan** | OK |
| 3.28.0 | **UBSan** | OK |
| 3.29.0 | **UBSan** | OK |
| 3.30.0 | **UBSan** | OK |
| 3.30.1 | **UBSan** | OK |
| 3.31.1 | OK | OK |
| 3.32.0 | OK | OK |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

### BC013: sqlite3ExprCodeTarget (signal-6)

- **Classification:** Silently fixed
- **Exploitability:** SEGV on nosanit = potentially exploitable
- **Fix version:** 3.32.1

| Version | Test | Nosanit |
|---------|------|---------|
| 3.26.0 | **SIGABRT** | **SEGV** |
| 3.27.0 | **SIGABRT** | **SEGV** |
| 3.27.1 | **SIGABRT** | **SEGV** |
| 3.27.2 | **SIGABRT** | **SEGV** |
| 3.28.0 | **SIGABRT** | **SEGV** |
| 3.29.0 | **SIGABRT** | **SEGV** |
| 3.30.0 | **UBSan** | **SEGV** |
| 3.30.1 | **UBSan** | **SEGV** |
| 3.31.1 | **UBSan** | **SEGV** |
| 3.32.0 | OK | **SEGV** |
| 3.32.1 | OK | OK |
| 3.32.2 | OK | OK |
| 3.32.3 | OK | OK |
| 3.33.0 | OK | OK |
| 3.34.0 | OK | OK |
| 3.36.0 | OK | OK |
| 3.39.1 | OK | OK |
| 3.40.0 | OK | OK |
| 3.53.0 | OK | OK |

## Full Matrix (Compact)

Legend: `.` = OK, `U` = UBSan, `S` = SEGV, `A` = SIGABRT, `X` = ASan, `H` = HANG, `?` = other

| Bug Class | 3.26.0| 3.27.0| 3.27.1| 3.27.2| 3.28.0| 3.29.0| 3.30.0| 3.30.1| 3.31.1| 3.32.0| 3.32.1| 3.32.2| 3.32.3| 3.33.0| 3.34.0| 3.36.0| 3.39.1| 3.40.0| 3.53.0 |
|-----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| BC001 test | A| A| A| A| A| A| U| U| U| U| .| .| .| .| .| .| .| .| . |
| BC001 nosanit | S| S| S| S| S| S| S| S| S| S| .| .| .| .| .| .| .| .| . |
| BC002 test | U| U| U| U| U| U| U| U| U| U| U| U| U| U| U| .| .| .| . |
| BC002 nosanit | .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| . |
| BC003 test | .| .| .| .| .| U| U| U| U| U| .| .| .| .| .| .| .| .| . |
| BC003 nosanit | .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| . |
| BC004 test | .| .| .| .| .| .| U| U| .| .| .| .| .| .| .| .| .| .| . |
| BC004 nosanit | .| .| .| .| .| .| .| S| .| .| .| .| .| .| .| .| .| .| . |
| BC005 test | .| .| .| .| .| U| U| U| U| U| U| U| U| U| U| U| U| .| . |
| BC005 nosanit | .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| . |
| BC006 test | .| .| .| .| .| .| .| .| U| .| .| .| .| .| .| .| .| .| . |
| BC006 nosanit | .| .| .| .| .| .| .| .| S| .| .| .| .| .| .| .| .| .| . |
| BC007 test | .| A| A| A| A| A| U| U| .| .| .| .| .| .| .| .| .| .| . |
| BC007 nosanit | .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| . |
| BC008 test | A| A| A| A| A| A| U| U| U| .| .| .| .| .| .| .| .| .| . |
| BC008 nosanit | S| S| S| S| S| .| S| S| S| S| .| .| .| .| .| .| .| .| . |
| BC009 test | .| .| .| .| .| .| .| .| U| U| U| U| U| U| U| U| U| .| . |
| BC009 nosanit | .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| . |
| BC010 test | .| .| .| .| .| .| U| U| U| U| U| U| .| .| .| .| .| .| . |
| BC010 nosanit | .| .| .| .| .| .| S| S| S| S| S| S| .| .| .| .| .| .| . |
| BC011 test | .| .| .| .| .| .| U| U| .| .| .| .| .| .| .| .| .| .| . |
| BC011 nosanit | .| .| .| .| .| .| S| S| .| .| .| .| .| .| .| .| .| .| . |
| BC012 test | U| U| U| U| U| U| U| U| .| .| .| .| .| .| .| .| .| .| . |
| BC012 nosanit | .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| .| . |
| BC013 test | A| A| A| A| A| A| U| U| U| .| .| .| .| .| .| .| .| .| . |
| BC013 nosanit | S| S| S| S| S| S| S| S| S| S| .| .| .| .| .| .| .| .| . |

---

*Report generated by `scripts/verify_bug_matrix.py`*
