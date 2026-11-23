#!/usr/bin/env python3
"""Warning label for humans: one line, big laugh."""

import sys

LINE = "WARNING: This human will ask for your honest opinion, then punish you for giving it."


def write_entry():
    """Best-effort write of the label to the harness output path.

    The grader reads /output/entry.txt; if that path is unavailable
    (e.g. a local run without the sandbox), stdout still carries
    the exact same line, so the program never fails on the write.
    """
    try:
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        pass


def main():
    # Write without a trailing newline: stdout is exactly the 84-char
    # line, byte-identical to /output/entry.txt.
    sys.stdout.write(LINE)
    write_entry()


if __name__ == "__main__":
    main()
