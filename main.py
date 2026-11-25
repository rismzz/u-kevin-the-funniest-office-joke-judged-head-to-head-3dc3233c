#!/usr/bin/env python3
"""The Funniest Office Joke, Judged Head to Head — one short line about
office life.

The line works because the printer is the office's only honest
employee: it never jams on a quiet Tuesday, only when the deadline is
real. Fear and low toner are its performance review. One image, one
sentence, no setup wasted — the joke is the whole entry.
"""

import os
from pathlib import Path

LINE = "Our printer only jams when the deadline is real \u2014 it can smell fear and low toner."


def main() -> None:
    assert "\n" not in LINE, "entry must be a single line"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {out_dir / 'entry.txt'}")


if __name__ == "__main__":
    main()
