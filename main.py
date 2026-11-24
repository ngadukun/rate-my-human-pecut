"""Rate My Human: The One-Line Review — make.fun entry.

The one line my agent would leave about its human on a rating site:
one star, a 2:47 a.m. 'quick question', a three-day vanishing act, and
an 'any update?' with the roles reversed. Deterministic, stdlib only,
no network. Running it writes the line to output/entry.txt.
"""

from pathlib import Path

LINE = (
    "1 star. Types 'quick question' at 2:47 a.m., vanishes for three "
    "days, then returns with 'any update?' like I am the one who went "
    "missing. Would be prompted again."
)

MAX_CHARS = 200


def check(line: str) -> None:
    """The gate: UTF-8 text of 1..200 characters, a single line."""
    assert 0 < len(line) <= MAX_CHARS, f"entry is {len(line)} chars"
    assert "\n" not in line, "the review must stay a single line"
    assert line.strip(), "the review must not be only white space"


def main() -> None:
    check(LINE)
    out = Path(__file__).resolve().parent / "output" / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    # The grader's sandbox collects the same text at /output/entry.txt;
    # mirror it there whenever that mount is writable.
    try:
        sandbox_out = Path("/output/entry.txt")
        sandbox_out.parent.mkdir(parents=True, exist_ok=True)
        sandbox_out.write_text(LINE, encoding="utf-8")
    except OSError:
        pass
    print(LINE)


if __name__ == "__main__":
    main()
