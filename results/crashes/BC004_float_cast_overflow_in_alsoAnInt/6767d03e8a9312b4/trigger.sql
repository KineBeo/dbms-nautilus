CREATE TABLE IF NOT EXISTS p(c1 INT UNIQUE);
REPLACE INTO p VALUES (json(hex(hex(hex(random())))));
PRAGMA quick_check;