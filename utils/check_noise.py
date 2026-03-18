"""
check_noise.py — Word-salad / rotated-sidebar noise checker for Markdown files created from PDFs.

Usage:
    python utils/check_noise.py <path_to_file.md>          # report only
    python utils/check_noise.py <path_to_file.md> --fix    # strip noise in-place

Exit code:
    0 — file passes (no noise detected)
    1 — noise detected (and NOT fixed, or fix failed)
"""

import sys
import re
from pathlib import Path

# Fix Windows console encoding
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# ---------------------------------------------------------------------------
# Pattern: a run of >=3 consecutive lines that are each a single character
# (letter, digit, or select punctuation). This is the rotated sidebar pattern.
# A "valid" exception: lines inside fenced code blocks are ignored.
# ---------------------------------------------------------------------------
SINGLE_CHAR_LINE = re.compile(r'^\s*[A-Za-z0-9|,\.;\:\'\"\(\)\[\]\-/\\]{1}\s*$')


def is_in_code_block(lines, idx):
    """Return True if line[idx] is inside a fenced code block."""
    in_block = False
    for i, line in enumerate(lines):
        if line.strip().startswith('```'):
            in_block = not in_block
        if i == idx:
            return in_block
    return False


def find_salad_runs(lines, min_run=3):
    """Return list of (start_idx, end_idx) tuples for noise runs."""
    runs = []
    run_start = None
    for i, line in enumerate(lines):
        if SINGLE_CHAR_LINE.match(line) and not is_in_code_block(lines, i):
            if run_start is None:
                run_start = i
        else:
            if run_start is not None and (i - run_start) >= min_run:
                runs.append((run_start, i - 1))
            run_start = None
    if run_start is not None and (len(lines) - run_start) >= min_run:
        runs.append((run_start, len(lines) - 1))
    return runs


def report(filepath, runs, lines):
    total_noise_lines = sum(end - start + 1 for start, end in runs)
    print(f"\n{'='*60}")
    print(f"Noise Report: {filepath}")
    print(f"{'='*60}")
    print(f"  Total lines in file : {len(lines)}")
    print(f"  Noise runs found    : {len(runs)}")
    print(f"  Total noise lines   : {total_noise_lines}")

    if runs:
        print(f"\n  Sample noise runs (first 5):")
        for start, end in runs[:5]:
            sample = ''.join(l.strip() for l in lines[start:end+1])
            print(f"    Lines {start+1}-{end+1} ({end-start+1} lines): '{sample[:60]}'")
        print()
        return False   # FAIL
    else:
        print(f"  ✓ No word-salad noise detected. File passes acceptance gate.\n")
        return True    # PASS


def fix_file(filepath, runs, lines):
    """Remove noise runs from lines and overwrite the file."""
    # Build a set of line indices to remove
    to_remove = set()
    for start, end in runs:
        for i in range(start, end + 1):
            to_remove.add(i)

    clean_lines = [line for i, line in enumerate(lines) if i not in to_remove]

    # Collapse more than 2 consecutive blank lines left after removal
    collapsed = []
    blank_count = 0
    for line in clean_lines:
        if line.strip() == '':
            blank_count += 1
            if blank_count <= 2:
                collapsed.append(line)
        else:
            blank_count = 0
            collapsed.append(line)

    filepath.write_text(''.join(collapsed), encoding='utf-8')
    removed = len(lines) - len(collapsed)
    print(f"  [✓] Fixed: removed {removed} noise lines. File saved.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python utils/check_noise.py <file.md> [--fix]")
        sys.exit(1)

    filepath = Path(sys.argv[1])
    do_fix = '--fix' in sys.argv

    if not filepath.exists():
        print(f"[✗] File not found: {filepath}")
        sys.exit(1)

    lines = filepath.read_text(encoding='utf-8', errors='ignore').splitlines(keepends=True)
    runs = find_salad_runs(lines, min_run=3)
    passed = report(filepath, runs, lines)

    if not passed:
        if do_fix:
            fix_file(filepath, runs, lines)
            sys.exit(0)
        else:
            print(f"  [✗] ACCEPTANCE GATE FAILED: {len(runs)} noise run(s) found.")
            print(f"      Run with --fix to strip automatically, or manually clean the file.")
            print(f"      Resolve this before treating the Markdown conversion as complete.\n")
            sys.exit(1)


if __name__ == '__main__':
    main()
