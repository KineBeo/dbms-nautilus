# PHP Bug Report: Crash When Calling `timezone_abbreviations_list()` After `extract()`

**Date:** 2018-06-03 11:24 UTC
**Reporter:** daniel dot teuchert at rub dot de

## Description

When executing the test script PHP crashes.

## Test Script

```php
<?php
$b = timezone_abbreviations_list();
extract($b);
timezone_abbreviations_list();
?>
```

## Actual Result

**Backtrace:**

```
#0  0x0000000001918d3e in zend_mm_alloc_small (size=0, heap=<optimized out>, 
    bin_num=<optimized out>) at Zend/zend_alloc.c:1273
#1  _emalloc_56 () at Zend/zend_alloc.c:2352
#2  0x0000000001a78a0f in _array_init (arg=0x7fffffff99a0, size=0) at Zend/zend_API.c:1090
#3  0x000000000051c220 in zif_timezone_abbreviations_list (execute_data=<optimized out>, 
    return_value=<optimized out>) at ext/date/php_date.c:4830
#4  0x0000000001ea9d23 in ZEND_DO_ICALL_SPEC_RETVAL_UNUSED_HANDLER (execute_data=<optimized out>)
    at Zend/zend_vm_execute.h:573
#5  0x0000000001c126d6 in execute_ex (ex=<optimized out>) at Zend/zend_vm_execute.h:59723
#6  0x0000000001c1312f in zend_execute (op_array=<optimized out>, return_value=<optimized out>)
    at Zend/zend_vm_execute.h:63760
#7  0x0000000001a6678e in zend_execute_scripts (type=-3184, retval=0x0, file_count=<optimized out>)
    at Zend/zend.c:1496
#8  0x00000000017e108a in php_execute_script (primary_file=0x7fffffffc560) at main/main.c:2590
#9  0x000000000200dba7 in do_cli (argc=<optimized out>, argv=<optimized out>)
    at sapi/cli/php_cli.c:1011
#10 0x000000000200aa8d in main (argc=<optimized out>, argv=<optimized out>)
    at sapi/cli/php_cli.c:1404
```