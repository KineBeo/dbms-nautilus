# A1 Stack-Dedup Manual Verification

**Date:** 2026-04-22
**Workdir tested:** /tmp/nautilus_eval/sqlite-3.31.1_attack_run_3m
**Total crashes:** 12
**Unique root causes:** 1
**Top cluster:** count=12, top_frame=`<no-frame>`
**Sample representative file:** 5_000001101

## Plausibility judgment

The 12 crashes collapse to a single cluster, which is plausibly correct given the SQL corpus is homogeneous (all samples include `printf('%.*g', ..., ...)` — the CVE-2020-13434 trigger pattern). However, the cluster's `top_frame` is `<no-frame>`, meaning gdb could not extract a usable backtrace for any of the 12 crashes; all 12 therefore hash to the empty-frame sentinel (SHA-256 of empty string `e3b0c44...`) and cluster by coincidence of failure rather than by shared root cause. A1 dedup is running end-to-end without errors, but on this workdir it degrades to "all crashes lumped together" rather than genuine stack-based clustering — likely cause: the harness binary was built without `-g` debug symbols, or gdb's `run` under the harness is not reproducing the crash (ASan/UBSan env not propagated, or `__AFL_INIT` short-circuiting under gdb). Flagged for investigation before E2 ablation depends on these numbers.
