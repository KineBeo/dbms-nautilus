"""Tests for triage/classify.py classification logic."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from triage.classify import classify_crash


def test_ubsan_via_signal6_detected():
    """UBSan runtime error that caused SIGABRT should classify as ubsan, not signal."""
    stderr = (
        "../cve_builds/sqlite-3.31.1/sqlite3.c:28488:24: "
        "runtime error: signed integer overflow: "
        "2147483647 + 341 cannot be represented in type 'int'\n"
        "    #0 0xaaaa in sqlite3_str_vappendf\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"
    assert subtype == "signed-integer-overflow"


def test_ubsan_null_pointer_via_signal6():
    """Null pointer UBSan error via SIGABRT."""
    stderr = (
        "../cve_builds/sqlite-3.30.1/sqlite3.c:220230:44: "
        "runtime error: applying non-zero offset 8 to null pointer\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"
    assert subtype == "null-pointer"


def test_ubsan_misaligned_via_signal6():
    """Misaligned address UBSan error via SIGABRT."""
    stderr = (
        "runtime error: store to misaligned address 0xaaaaaaaaaaaaaaaa "
        "for type 'Window *'\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"


def test_ubsan_float_overflow_via_signal6():
    """Float-to-int overflow UBSan error via SIGABRT."""
    stderr = (
        "runtime error: 1.11111e+135 is outside the range of "
        "representable values of type 'long long'\n"
    )
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "ubsan", f"Expected ubsan, got {crash_type}"


def test_pure_signal6_no_ubsan():
    """SIGABRT without runtime error stays as signal."""
    stderr = "some other abort reason\n"
    crash_type, subtype = classify_crash(-6, stderr)
    assert crash_type == "signal"
    assert subtype == "signal-6"


def test_asan_exit223():
    """ASan heap-buffer-overflow still works."""
    stderr = "heap-buffer-overflow at 0xdeadbeef\n"
    crash_type, subtype = classify_crash(223, stderr)
    assert crash_type == "asan"
    assert subtype == "heap-buffer-overflow"


def test_ubsan_exit1():
    """Normal UBSan exit code 1 still works."""
    stderr = "runtime error: signed integer overflow: 1 + 1\n"
    crash_type, subtype = classify_crash(1, stderr)
    assert crash_type == "ubsan"


def test_debug_assert():
    """SIGTRAP (exit -5) stays as debug_assert."""
    crash_type, subtype = classify_crash(-5, "")
    assert crash_type == "debug_assert"


def test_segfault():
    """SIGSEGV (exit -11) stays as signal."""
    crash_type, subtype = classify_crash(-11, "no runtime error here\n")
    assert crash_type == "signal"
    assert subtype == "signal-11"


def test_nosanit_clean_exit():
    """Nosanit harness: exit 0 = no crash."""
    crash_type, subtype = classify_crash(0, "")
    assert crash_type == "debug_assert"
