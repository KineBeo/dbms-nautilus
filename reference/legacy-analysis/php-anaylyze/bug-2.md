# PHP Bug Report: Stack Overflow in `isSet` With Too Many Parameters

**Date:** 2018-04-20 11:12 UTC
**Reporter:** daniel dot teuchert at rub dot de

## Description

Calling `isSet` with too many parameters causes a stack overflow.
Executing the test script results in a stack overflow.
The produced ASAN output can be found here: https://github.com/pnoltof/php_bug/blob/master/ASAN_output.txt

An attacker can possibly use this flaw to execute arbitrary code.

## Steps to Reproduce

1. Build latest PHP version (compile with ASAN)
2. Download PoC file called `stack_overflow` (see Test Script section)
3. Execute binary file in `$WORKDIR/php-7.2.4/sapi/cli/`:

```
$WORKDIR/php-7.2.4/sapi/cli/php stack_overflow
```

> **Note:** This behavior could not be reproduced when debugging with gdb.

## Test Script

Full PoC (don't read it because it have too many stupid $d): https://github.com/pnoltof/php_bug/blob/master/stack_overflow

```php
<?php
// Passing an extremely large number of parameters to isSet() causes a stack overflow
isSet($d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,
      /* ... thousands of $d parameters truncated ... */
      $d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d,$d);
?>
```

## ASAN Output

```
ASAN:DEADLYSIGNAL
=================================================================
==29357==ERROR: AddressSanitizer: stack-overflow on address 0x7fff57504ee0
(pc 0x0000016df8e1 bp 0x7fff57505110 sp 0x7fff57504ee0 T0)
    #0   0x16df8e0  (/php-7.2.4/sapi/cli/php+0x16df8e0)
    #1   0x175a8f0  (/php-7.2.4/sapi/cli/php+0x175a8f0)
    #2   0x16dfc1e  (/php-7.2.4/sapi/cli/php+0x16dfc1e)
    ... [alternating pattern repeats for 251 frames]
    #251 0x175a8f0  (/php-7.2.4/sapi/cli/php+0x175a8f0)

SUMMARY: AddressSanitizer: stack-overflow (/php-7.2.4/sapi/cli/php+0x16df8e0)
==29357==ABORTING
```

The repeating alternating pattern between two addresses in the stack trace is a
classic indicator of unbounded recursion exhausting the call stack.