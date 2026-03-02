-- Verified: only %.*g reliably triggers UBSan exit 1 on sqlite-3.31.1
-- %.*f and %.*e exit 0 (different precision path, no overflow)
-- %.*c and %.*s cause OOM (allocation before overflow check)
SELECT printf('%.*g',2147483647,0.01);
