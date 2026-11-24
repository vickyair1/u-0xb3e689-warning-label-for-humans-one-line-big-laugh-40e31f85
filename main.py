"""Warning Label for Humans — one-line big laugh (resubmit).

Deterministic program: writes the entry line to /output/entry.txt and
prints it to stdout. Stdlib only, no randomness.
"""

LINE = "WARNING: Do not say 'we need to talk.' This human has already rehearsed the breakup, the custody of the dog, and your apology speech."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate: at most 160 chars, exactly one line, no leading/trailing whitespace.
    assert 1 <= len(LINE) <= 160, "line must be 1-160 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
