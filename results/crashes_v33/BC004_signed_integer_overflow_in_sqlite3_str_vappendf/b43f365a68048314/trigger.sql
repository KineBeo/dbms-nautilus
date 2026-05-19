SELECT printf('%.*f', -2147483649, -1e308), substr('  Vv 6b W_-U_  ', -1);
PRAGMA cache_size=0;
CREATE VIRTUAL TABLE IF NOT EXISTS rtree1 USING rtree(id, x1, x2, y1, y2);