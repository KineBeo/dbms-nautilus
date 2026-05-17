CREATE TABLE IF NOT EXISTS p(c1 TEXT CHECK (zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(zeroblob(p.c1)))))))))));
INSERT INTO p DEFAULT VALUES;
PRAGMA integrity_check;