# Crash Triage Report

**Total crashes:** 3  
**Unique crash sites:** 3  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 3 | 3 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `c6665f1edcb0237e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015570`

```sql
SELECT fpdecode(-1.0, 2147483648, 0); EXPLAIN ALTER TABLE p DROP COLUMN a;
```

---

## Crash 2: `e597adac7ccf563c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024258`

```sql
SELECT fpdecode(1.0, 2147483648, 32767);
```

---

## Crash 3: `8498fe02dd77be56` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000034034`

```sql
SELECT fpdecode(1e308, -2147483648, -2147483648);
```

---
