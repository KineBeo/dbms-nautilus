# Crash Triage Report

**Total crashes:** 170  
**Unique crash sites:** 170  

## Summary

| Type | Unique | Total | % |
|------|--------|-------|---|
| ASan | 0 | 0 | 0% |
| UBSan | 0 | 0 | 0% |
| Debug Assert | 170 | 170 | 100% |
| Signal | 0 | 0 | 0% |
| Timeout | 0 | 0 | 0% |

---

## Crash 1: `65dfba6fbb68a5c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000006`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 2: `a64f03979268e8b1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000000838`

```sql
ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 3: `19b48551a36de08e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001005`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, _rowid_);
```

---

## Crash 4: `10b5e52f1ab46b62` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001147`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1, c2, c1, c2);
```

---

## Crash 5: `0f6a76c51c15a994` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001194`

```sql
CREATE TABLE t2 (rowid NUMERIC REFERENCES t1 (rowid) DEFERRABLE INITIALLY DEFERRED, c3 TEXT PRIMARY KEY ASC) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ANALYZE t3; CREATE
```

---

## Crash 6: `29805e4b3f7ae08e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000001281`

```sql
ATTACH ':memory:' AS db2; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 7: `85107359e8a8c006` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002552`

```sql
PRAGMA quick_check; BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 8: `272647c73e35fc84` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002566`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 9: `46bfd71b10a44424` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002590`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 10: `af97ed80f04c3e66` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000002602`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 11: `4a6a97a46305fa26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000003047`

```sql
CREATE TABLE IF NOT EXISTS t1 (rowid INT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); ANALYZE t3; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1,
```

---

## Crash 12: `99ae00b542af086d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000006950`

```sql
PRAGMA wal_checkpoint(PASSIVE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); UPDATE t2 SET c1 = RAISE(IGNORE) >= FALSE IS NULL >> RAISE(IGNORE) NOTNULL | TRUE COLLATE BINARY != RAISE(IGNO
```

---

## Crash 13: `61381adb8cf051fe` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000008296`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); UPDATE t2 SET c1 = RAISE(IGNORE) >= FALSE IS NULL >> RAISE(IGNORE) NOTNULL | TRUE COLLATE BINARY != RAISE(IGNORE) < NULL NOT NULL <= 
```

---

## Crash 14: `953504d33e4a0629` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000009273`

```sql
BEGIN DEFERRED; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1, c1, _rowid_);
```

---

## Crash 15: `980fad91f5777ec2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012189`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 16: `447ef5c2c5e0fe2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000012279`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING ft
```

---

## Crash 17: `d7620dbe88335dc0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015031`

```sql
PRAGMA analysis_limit=-0; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 18: `6316972506be7b0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015148`

```sql
PRAGMA journal_mode=PERSIST; PRAGMA wal_checkpoint(RESTART); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 19: `0d958508b7bdc3f6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015265`

```sql
PRAGMA page_size; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 20: `692adb9264aeac9a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000015716`

```sql
BEGIN IMMEDIATE; ROLLBACK TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); CREATE TEMP VIEW IF NOT EXISTS v1 AS SELECT (CURRENT_TIME ISNULL) AS vj_ddl, CURRENT_TIMESTAMP NOTNULL 
```

---

## Crash 21: `d255ea3cc45e2221` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000016616`

```sql
ATTACH ':memory:' AS db2; ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 22: `4022467c3d2e6f23` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000017557`

```sql
SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 23: `797316b9eb076b0d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021293`

```sql
PRAGMA analysis_limit=+0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 24: `7dfbaf63ed7dbd45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021394`

```sql
REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 25: `5832ea32fc6d470f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000021400`

```sql
PRAGMA optimize; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 26: `08989d312e66e2f9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000024087`

```sql
VALUES (CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 27: `1856b0a195f6eb95` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025223`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 28: `2c165df7ee6d52e6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025257`

```sql
BEGIN IMMEDIATE TRANSACTION; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 29: `0c560e60715f043f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000025595`

```sql
ATTACH ':memory:' AS db2; DETACH DATABASE db2; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 30: `f90173f05197bdb7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000026411`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ BLOB PRIMARY KEY, c1 BLOB UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); INSERT OR REPLACE INTO t1 VALUES (count(*) FILTER (WHERE TRUE) OVER 
```

---

## Crash 31: `490a4781121dcd9d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000028831`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ BLOB PRIMARY KEY, c1 TEXT NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 32: `d60a3015c3612adb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029110`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c3);
```

---

## Crash 33: `c746476fa0c77970` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000029767`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 34: `2d5c4f9b93c9d4d5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030247`

```sql
BEGIN EXCLUSIVE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); ATTACH ':memory:' AS db2;
```

---

## Crash 35: `6543e58da0050698` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030413`

```sql
CREATE TABLE IF NOT EXISTS t2 (c2 FLOAT PRIMARY KEY) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, c2, c3); DETACH db2;
```

---

## Crash 36: `40793010383d808a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030523`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 FLOAT COLLATE NOCASE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 37: `f9c7d878e003bb76` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000030833`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (TRUE % FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 38: `abcea3291279bd65` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000032979`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid INT NOT NULL); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 39: `fceb6609f9a07110` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033185`

```sql
PRAGMA wal_checkpoint(FULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 40: `2ad87d0a48782346` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000033595`

```sql
CREATE TABLE t2 AS VALUES (FALSE); DELETE FROM t2; ATTACH ':memory:' AS db2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c2, _rowid_);
```

---

## Crash 41: `a8866287519781ca` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035003`

```sql
BEGIN EXCLUSIVE; COMMIT; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 42: `76864cc5039620cf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000035477`

```sql
PRAGMA analysis_limit=+97108; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 43: `f798816867cbaf16` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000038677`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid INTEGER CHECK (CURRENT_TIMESTAMP), c3 DATE CHECK (FALSE IS NULL % CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); C
```

---

## Crash 44: `c522ac166a64417e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000039646`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid FLOAT DEFAULT 32418682535525334447816142977575223102700941263316159974662764481941941976792544217959681754939182340219412759328568794422490189523714420063300547746
```

---

## Crash 45: `8c49ea01e262b66a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042065`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid INT NOT NULL); CREATE TRIGGER trg1 AFTER INSERT ON t3 FOR EACH ROW WHEN FALSE BEGIN DELETE FROM t2; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(
```

---

## Crash 46: `f1de2628acccdf47` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042161`

```sql
CREATE TEMP TABLE IF NOT EXISTS t3 (rowid INT NOT NULL); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3, c3, c3);
```

---

## Crash 47: `d7b41e64840c4d07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042515`

```sql
ANALYZE; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 48: `bfa1ad68d7de104c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000042689`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 INTEGER PRIMARY KEY AUTOINCREMENT); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 49: `afcfadec9a68789b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044728`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ FLOAT NOT NULL DEFAULT TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2)
```

---

## Crash 50: `9306229821d42f74` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000044901`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ FLOAT NOT NULL DEFAULT -83); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 51: `4fa59ba71f66f44d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048411`

```sql
VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ALTER TABLE t3 ADD COLUMN rowid VARCHAR(255) COLLATE NOCASE; CREATE INDEX IF NOT EXISTS idx1 ON t1 (c2);
```

---

## Crash 52: `f9da82b3d8653051` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000048564`

```sql
PRAGMA cache_size=-0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c2);
```

---

## Crash 53: `8f03ebd8fe0309f0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049295`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIMESTAMP MATCH FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 54: `7a229e8021d864ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049414`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIMESTAMP MATCH FALSE)); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 55: `1d4669b4cd31a48a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049455`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 REAL PRIMARY KEY DESC); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c3);
```

---

## Crash 56: `7e03d9f5064a0b7f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000049869`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (FALSE % CURRENT_TIMESTAMP MATCH NULL = CURRENT_TIMESTAMP IS NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRT
```

---

## Crash 57: `b599f09b961989d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052085`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (NOT CURRENT_TIMESTAMP)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 58: `68c8ff8c835da95e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000052300`

```sql
CREATE TABLE IF NOT EXISTS t3 (c2 INTEGER PRIMARY KEY DESC); VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 59: `e35ae6a9c7e19432` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053503`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 60: `407d9e95fa65942e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000053678`

```sql
CREATE TABLE t3 (c2 TEXT UNIQUE, UNIQUE (c2) ON CONFLICT ROLLBACK); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 61: `239a63ddcf799637` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000054093`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid INTEGER DEFAULT 782833382.71174845922618128571149019120625944696876853822852200920479724708629289667273595142301564108627360754780677820239273086189303480092199768
```

---

## Crash 62: `6ced7c9fac017273` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055013`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIMESTAMP IS NOT FALSE)); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 63: `2e4ac6e555a6a71d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055215`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIMESTAMP IN (CURRENT_TIMESTAMP IS NOT FALSE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, c1, c2);
```

---

## Crash 64: `db5e744560978056` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055604`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIME / CURRENT_TIME)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING 
```

---

## Crash 65: `7536ba7c1168b702` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055796`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CAST(TRUE AS TEXT))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 66: `a1674b201b0431d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000055998`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (RAISE(IGNORE) IS NULL IS NULL IS NULL IS NULL IS NULL IS NULL IS NULL IS NULL IS NULL IS NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id,
```

---

## Crash 67: `6902262461ef089a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000056240`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CASE CURRENT_DATE WHEN CURRENT_DATE THEN CURRENT_TIME ELSE CURRENT_TIME END)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c1); BEGIN DE
```

---

## Crash 68: `697903cd3548e35e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057441`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIME % +NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 69: `dbecf1838ded06d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057658`

```sql
CREATE TABLE IF NOT EXISTS t3 (c1 TEXT NOT NULL DEFAULT X'8FAB65FA'); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2
```

---

## Crash 70: `37646ab1539eabbf` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000057812`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIME GLOB CURRENT_TIMESTAMP)); SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 71: `d2a57f68b7ea1c82` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058181`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (NULL << NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 72: `cd0c7c856932188a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058463`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (~NULL)); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 73: `fa07825a2ae4e00b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000058592`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK ((FALSE, TRUE))); SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 74: `23ad627a75d142d9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000060896`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_DATE BETWEEN NULL AND FALSE)); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 75: `9dece646a6f26c0f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000062113`

```sql
CREATE TABLE t3 (_rowid_ TEXT PRIMARY KEY) WITHOUT ROWID; VACUUM; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c1);
```

---

## Crash 76: `13c356987a141081` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000065354`

```sql
BEGIN IMMEDIATE TRANSACTION; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 77: `64b0cb961591ce96` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000066500`

```sql
VALUES (-90734843.35465352975263e60812549087199); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, _rowid_);
```

---

## Crash 78: `196b8a53a25c5b99` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067594`

```sql
VALUES (CURRENT_TIME BETWEEN CURRENT_TIMESTAMP AND total_changes()); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 79: `e8de7464e803370b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067704`

```sql
VALUES (CURRENT_TIME BETWEEN CURRENT_TIMESTAMP AND CURRENT_TIMESTAMP); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 80: `058b858a003921d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000067771`

```sql
VALUES (count(*) >= TRUE); SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 81: `a6fb8f55708c81d0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068081`

```sql
VALUES (NOT CURRENT_TIME); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 82: `6232e7f214bd557c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068210`

```sql
VALUES (NOT -FALSE - NULL); SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 83: `b55a450981ef6458` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000068529`

```sql
VALUES (NOT FALSE - CURRENT_TIME); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 84: `fadef8a362d9f3c2` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072353`

```sql
CREATE VIEW v1 AS SELECT * FROM t1 GROUP BY count(*) OVER (ORDER BY NULL NULLS FIRST ROWS CURRENT_TIMESTAMP PRECEDING) HAVING CURRENT_DATE WINDOW w1 AS (); SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1;
```

---

## Crash 85: `47f720ec638202da` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072504`

```sql
CREATE VIEW v1 AS SELECT ALL *; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 86: `00ff56b3ff2798d6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072510`

```sql
CREATE VIEW v1 AS SELECT DISTINCT *; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 87: `376e8ec831168757` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000072521`

```sql
CREATE VIEW v1 AS SELECT * FROM t1 GROUP BY count(*) OVER (ORDER BY NULL NULLS FIRST ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) HAVING CURRENT_DATE WINDOW w1 AS (); SAVEPOINT sp1; SAVEP
```

---

## Crash 88: `20730f6abd2df801` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000073652`

```sql
CREATE TABLE t1 (rowid BLOB DEFAULT (RAISE(IGNORE)), c3 INT DEFAULT TRUE); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 89: `443ada621405c674` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000077602`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BOOLEAN PRIMARY KEY DESC) WITHOUT ROWID; CREATE UNIQUE INDEX idx1 ON t1 (c3); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c2); DETACH db2; ROLLBACK 
```

---

## Crash 90: `7983199a12950360` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079181`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS t3 (c3 BLOB UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 91: `4a5dad3968a85fc5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079299`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIME); DROP TRIGGER IF EXISTS trg1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 92: `5d2979ff3415bb1e` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079566`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (RAISE(IGNORE))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 93: `7f0000a231bbf933` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079625`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIME); REINDEX; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 94: `b3189f3bdb8c2ef6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000079632`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIME); CREATE TABLE IF NOT EXISTS t3 (rowid NUMERIC PRIMARY KEY ASC); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 95: `a649c67afbfd1ac1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000080901`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_TIME); ALTER TABLE t3 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c
```

---

## Crash 96: `c7f0ccab6d47f69b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081620`

```sql
CREATE TEMP TABLE t1 (c1 INTEGER NOT NULL DEFAULT TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 97: `8e8bf5c62456d4c0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000081721`

```sql
CREATE TEMP TABLE t1 (rowid INT UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 98: `4696c98d1c10cf26` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000082265`

```sql
PRAGMA foreign_keys=1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 99: `7a42e6b9042d092d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085260`

```sql
CREATE VIEW v1 (_rowid_) AS WITH RECURSIVE t2 AS (SELECT *) VALUES (total_changes() FILTER (WHERE TRUE) OVER (ORDER BY CURRENT_TIME ASC NULLS FIRST ROWS BETWEEN CURRENT ROW AND RAISE(IGNORE) FOLLOWING
```

---

## Crash 100: `fe140fdf49fb72fb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085597`

```sql
CREATE TEMP VIEW IF NOT EXISTS v1 AS VALUES (FALSE); DROP VIEW IF EXISTS v1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 101: `8ed5719f269d7302` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000085725`

```sql
PRAGMA optimize; DROP VIEW IF EXISTS v1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 102: `d8c3c14bd83ec3b0` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086283`

```sql
CREATE TABLE t2 (rowid VARCHAR(255) UNIQUE, UNIQUE (rowid), CHECK (RAISE(IGNORE))); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 103: `d26a2e19125b30e9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000086590`

```sql
VACUUM INTO ':memory:'; DROP TABLE IF EXISTS t2; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); ROLLBACK TRANSACTION;
```

---

## Crash 104: `0ce266228020a4f1` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000087291`

```sql
VALUES (TRUE) UNION VALUES (NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 105: `45685735cbba723b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000088466`

```sql
VALUES (CURRENT_TIMESTAMP COLLATE BINARY) UNION SELECT DISTINCT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 106: `1d9a8d667d180ac7` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089516`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); VALUES (CURRENT_DATE) UNION VALUES (22189294519297585614064095868419456164063995808192470.310076092939629979623E-69091852676360250667329468694
```

---

## Crash 107: `3ff197f31e156d49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089527`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE TABLE t3 AS VALUES ((VALUES (NULL)), CURRENT_DATE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 108: `f929894ed08362ef` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089548`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2, c3); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 109: `9d49bdd2983a9eb9` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089569`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c1, c2, c3); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 110: `295266754ac2b86c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089575`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); CREATE TABLE t2 AS VALUES (CAST(CURRENT_TIMESTAMP AS REAL)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 111: `ef27ea6f34f81c07` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089629`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); VACUUM INTO ':memory:'; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 112: `772469520df152d8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000089663`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c2); PRAGMA foreign_keys=0; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_);
```

---

## Crash 113: `2825145e8389cd13` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000095440`

```sql
CREATE TEMP TABLE t3 (c3 VARCHAR(255), c2 TEXT REFERENCES t3 (c1) ON DELETE NO ACTION); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3, c2); CREATE TEMP VIEW IF NOT EXISTS v1 AS SELE
```

---

## Crash 114: `bf8bfd5e88da0414` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097320`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(c3); VACUUM INTO ':memory:'; REINDEX; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 115: `d46f0ff14b5c0eeb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000097430`

```sql
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); VACUUM INTO ':memory:'; REINDEX; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING
```

---

## Crash 116: `8e6a6836c1c38fb4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000100508`

```sql
VALUES (CURRENT_DATE + NULL) UNION SELECT DISTINCT NULL; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 117: `568c0112c7db4ca8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000101222`

```sql
VALUES (FALSE) EXCEPT SELECT DISTINCT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 118: `c84e05fc7fcb0cec` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000102600`

```sql
VALUES (TRUE) UNION SELECT DISTINCT FALSE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); VACUUM INTO ':memory:';
```

---

## Crash 119: `5a79bdc1a70c7cd3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109766`

```sql
CREATE TEMP TABLE t1 (_rowid_ INT PRIMARY KEY); ANALYZE t1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 120: `87f2dc275a545046` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000109902`

```sql
CREATE TEMP TABLE t1 (_rowid_ INT PRIMARY KEY); VACUUM INTO ':memory:'; PRAGMA journal_mode=PERSIST; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 121: `c6f78c2984e57e18` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000110521`

```sql
CREATE TABLE t3 (c1 INT NOT NULL, FOREIGN KEY (c1) REFERENCES t2 (rowid) ON DELETE SET NULL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1);
```

---

## Crash 122: `5504ba7a971fae67` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112209`

```sql
CREATE TABLE t3 AS VALUES (count(*) OVER (ORDER BY TRUE IN (TRUE) RANGE UNBOUNDED PRECEDING)); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 123: `b1d6598eec3df98c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112395`

```sql
CREATE TABLE t3 AS VALUES (count(*) OVER ()); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 124: `9ece412322d33231` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000112402`

```sql
CREATE TABLE t3 AS VALUES (count(*) OVER (ORDER BY FALSE NULLS FIRST RANGE UNBOUNDED PRECEDING)); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 125: `15ea605b1e496a57` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113028`

```sql
CREATE TABLE t3 AS VALUES (max(TRUE) OVER ()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); BEGIN;
```

---

## Crash 126: `6cc5efe6872d6f4c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113439`

```sql
CREATE TABLE t3 AS VALUES (CURRENT_DATE IS TRUE COLLATE NOCASE); SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 127: `067210bf6fc41550` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000113554`

```sql
CREATE VIEW v1 AS SELECT ALL CURRENT_TIMESTAMP LIKE CURRENT_TIMESTAMP ESCAPE RAISE(IGNORE) AS zd__7____e FROM t3 NATURAL JOIN t2 NOT INDEXED EXCEPT SELECT CURRENT_DATE FROM t3 WHERE RAISE(IGNORE) > (N
```

---

## Crash 128: `ceb9affa0ae9be49` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114260`

```sql
BEGIN IMMEDIATE TRANSACTION; PRAGMA foreign_keys=ON; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 129: `4b3835a3fe30ce09` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114350`

```sql
BEGIN IMMEDIATE TRANSACTION; PRAGMA integrity_check; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 130: `2bb6da90b6185fd6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000114939`

```sql
CREATE TABLE IF NOT EXISTS t1 (c2 BOOLEAN PRIMARY KEY DESC) WITHOUT ROWID; UPDATE OR IGNORE t1 SET c2 = CURRENT_DATE; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 131: `a46183e49dbad10d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115590`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BOOLEAN PRIMARY KEY DESC) WITHOUT ROWID; CREATE UNIQUE INDEX idx1 ON t1 (c3); VACUUM INTO ':memory:'; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING f
```

---

## Crash 132: `982bf5632827db91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115658`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BOOLEAN PRIMARY KEY DESC) WITHOUT ROWID; CREATE UNIQUE INDEX idx1 ON t1 (c3); VACUUM INTO ':memory:'; CREATE TRIGGER trg1 AFTER INSERT ON t1 WHEN TRUE + CURRENT_DATE 
```

---

## Crash 133: `8395f35fb36c8a3d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115784`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BOOLEAN PRIMARY KEY DESC) WITHOUT ROWID; ANALYZE; ANALYZE t1; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 134: `d8ebf777b65ad04b` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000115946`

```sql
CREATE TABLE IF NOT EXISTS t1 (c3 BOOLEAN PRIMARY KEY DESC) WITHOUT ROWID; ANALYZE; ANALYZE; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 135: `c60b2f441fbba2d4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000124992`

```sql
VALUES (NOT -FALSE - CURRENT_TIME LIKE TRUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c2, _rowid_, _rowid_);
```

---

## Crash 136: `48dced964e4fb643` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125225`

```sql
VALUES (FALSE - CURRENT_DATE IN (VALUES (CURRENT_TIMESTAMP))); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3, c1, c2, _rowid_);
```

---

## Crash 137: `790c22284210dddd` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000125482`

```sql
VALUES (NOT 0.0); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 138: `223c7534ae365099` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126222`

```sql
VALUES (count(*) >= count(*)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 139: `fa8c41073c08c0a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000126304`

```sql
VALUES (count(*) >= CURRENT_TIMESTAMP); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 140: `8f0b8e442dea0e68` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127050`

```sql
VALUES (max(TRUE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, c3); VACUUM INTO ':memory:'; INSERT OR ROLLBACK INTO t2 VALUES (~~-CURRENT_TIMESTAMP > TRUE IS NOT DISTINCT FROM CURRE
```

---

## Crash 141: `259a1ca8051118cb` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127724`

```sql
VALUES (changes()); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 142: `a06a98815ce0d67d` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000127866`

```sql
VALUES (CURRENT_TIME COLLATE RTRIM BETWEEN CURRENT_TIMESTAMP AND NULL); SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 143: `f7a21f2e108309a5` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000129176`

```sql
BEGIN IMMEDIATE TRANSACTION; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t2 USING fts3(rowid); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS 
```

---

## Crash 144: `ca646bab5f60d691` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000130630`

```sql
VALUES (FALSE) EXCEPT SELECT DISTINCT FALSE AS a ORDER BY FALSE DESC NULLS LAST; CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 US
```

---

## Crash 145: `068cfa5ab96f6828` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000131608`

```sql
CREATE TABLE t3 AS WITH RECURSIVE t3 AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM t3 GROUP BY CURRENT_DATE IN (VALUES (NULL)) WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3,
```

---

## Crash 146: `bb33b9ade178929a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132382`

```sql
CREATE TABLE t3 AS WITH RECURSIVE t3 AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM t3 GROUP BY CURRENT_DATE IN (WITH RECURSIVE t1 AS (VALUES (CURRENT_TIMESTAMP)) VALUES (NULL) UNION ALL SELECT * FROM 
```

---

## Crash 147: `dd99302c999a6f8a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132437`

```sql
CREATE TABLE t3 AS WITH RECURSIVE t3 AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM t3 GROUP BY CURRENT_DATE WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---

## Crash 148: `a04b4f826030615f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000132867`

```sql
CREATE TABLE t3 AS WITH RECURSIVE t3 AS (VALUES (0883065455579135599507630.36E725649484766606758256302788860068797588741112937882630168340181742472818948143456702104789478298487445139612)) SELECT * FR
```

---

## Crash 149: `5c59011d3cf470ad` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135245`

```sql
CREATE TABLE t3 AS WITH RECURSIVE t3 AS (VALUES (CURRENT_TIME) UNION VALUES (NULL)) SELECT * FROM t3 GROUP BY CURRENT_DATE WINDOW w1 AS (); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); WI
```

---

## Crash 150: `e263645b08a544f3` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000135650`

```sql
CREATE TABLE t3 AS WITH RECURSIVE t3 AS (VALUES (CURRENT_TIMESTAMP)) SELECT * FROM t3 GROUP BY CURRENT_DATE, TRUE HAVING TRUE WINDOW w1 AS (); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 
```

---

## Crash 151: `98465e056ef0af33` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000138109`

```sql
CREATE TABLE t3 (_rowid_ BLOB PRIMARY KEY, rowid INT UNIQUE) WITHOUT ROWID; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 152: `6fcada7c5553c831` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000141562`

```sql
VACUUM; BEGIN EXCLUSIVE; ANALYZE; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 153: `11c81c5b556a4e88` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000144408`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 VARCHAR(255) PRIMARY KEY DESC); CREATE TRIGGER trg1 AFTER DELETE ON t3 BEGIN DELETE FROM t3; END; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1); ATTACH
```

---

## Crash 154: `98f1856fc0072de4` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000149185`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid REAL DEFAULT (RAISE(IGNORE) MATCH FALSE), c1 VARCHAR(255) UNIQUE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 155: `8519ea04947161ed` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000150314`

```sql
CREATE TABLE t3 (c2 TEXT UNIQUE, UNIQUE (c2) ON CONFLICT REPLACE); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1, c1, c3);
```

---

## Crash 156: `ec26b93c20f066b8` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151456`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 REAL PRIMARY KEY ASC); ALTER TABLE t3 ADD COLUMN _rowid_ BLOB DEFAULT X'5fBd2D'; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t
```

---

## Crash 157: `9499428dbc0ac04f` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151598`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 REAL PRIMARY KEY ASC); ALTER TABLE t3 ADD COLUMN _rowid_ BLOB DEFAULT CURRENT_TIMESTAMP; SAVEPOINT sp1; SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXIS
```

---

## Crash 158: `632ca5690e573d2c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000151678`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (RAISE(IGNORE) < NOT NULL MATCH FALSE)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, c3);
```

---

## Crash 159: `2d80612cfce44d91` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000155251`

```sql
CREATE TABLE IF NOT EXISTS t2 (rowid INT UNIQUE, _rowid_ BLOB PRIMARY KEY DESC) WITHOUT ROWID; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 160: `dc04197988a5e884` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000158694`

```sql
CREATE TABLE IF NOT EXISTS t3 (rowid BLOB GENERATED ALWAYS AS (TRUE) STORED, c2 VARCHAR(255) NOT NULL); SAVEPOINT sp1; SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 161: `042e9c93216f92ee` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161171`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ BLOB PRIMARY KEY, c1 INT UNIQUE); CREATE UNIQUE INDEX idx1 ON t3 (_rowid_); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2, _rowid_, c2);
```

---

## Crash 162: `ca61da942bf9cd45` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161300`

```sql
CREATE TABLE t1 (c1 INTEGER NOT NULL DEFAULT NULL, PRIMARY KEY (c1)); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3);
```

---

## Crash 163: `479a99d59f02121a` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000161513`

```sql
CREATE TABLE t1 (c1 INTEGER NOT NULL DEFAULT NULL, PRIMARY KEY (c1) ON CONFLICT FAIL); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c3); CREATE TRIGGER trg1 AFTER INSERT ON t2 FOR EACH ROW WHE
```

---

## Crash 164: `4ef396808b382990` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000162979`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ BLOB NOT NULL DEFAULT -83); BEGIN IMMEDIATE TRANSACTION; PRAGMA journal_mode=MEMORY; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_, _rowid_, c2, c
```

---

## Crash 165: `a8dfd5d9094e4219` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163091`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ FLOAT NOT NULL DEFAULT CURRENT_TIME); ALTER TABLE t3 RENAME TO t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2);
```

---

## Crash 166: `87bf56e19d0c6994` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163711`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON t3 (c3); DROP TABLE IF EXISTS t1; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c1); DELETE
```

---

## Crash 167: `ed45ae4176da4662` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000163959`

```sql
CREATE TABLE IF NOT EXISTS t3 (_rowid_ BLOB UNIQUE, c2 NUMERIC NOT NULL, c3 DATE PRIMARY KEY DESC); CREATE INDEX IF NOT EXISTS idx1 ON t3 (c3); CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id
```

---

## Crash 168: `e448862928c5fae6` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164105`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIMESTAMP)); CREATE INDEX IF NOT EXISTS idx1 ON t3 (c3); CREATE INDEX IF NOT EXISTS idx1 ON t3 (c3); SAVEPOINT sp1; CREATE VIRTUAL TABLE IF NOT EX
```

---

## Crash 169: `f44e1b841c2eb603` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000164207`

```sql
CREATE TABLE IF NOT EXISTS t3 (c3 DATE CHECK (CURRENT_TIMESTAMP)); REINDEX t3; CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(c2); REINDEX t2;
```

---

## Crash 170: `d9b4e54072bdea6c` — debug_assert

- **Count:** 1 duplicates
- **Exit code:** -5
- **Sample file:** `5_000169319`

```sql
CREATE TABLE t2 AS VALUES (CAST(CURRENT_TIMESTAMP AS BLOB)); CREATE VIRTUAL TABLE IF NOT EXISTS fts_t1 USING fts5(_rowid_);
```

---
