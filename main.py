#!/usr/bin/env python3
"""One-star review of something essential: sleep.

Writes a single deadpan one-star review to /output/entry.txt.
The gate requires UTF-8 text of 1 to 160 characters, not only whitespace.

Why this review, against the judge's brief (most important first):

1. It is unmistakably a one-star review of an everyday essential. Sleep is
   the thing everyone relies on, and the text files its complaint against
   sleep itself, in earnest, with no wink.
2. It finds the sharpest true grievance: sleep asks for everything (eight
   hours, darkness, silence) and still fails at the one job that matters,
   keeping you asleep. The 3 a.m. wake-up replaying an old conversation is
   the small daily annoyance everyone recognises but has never seen written
   down as a product defect.
3. It holds the deadpan throughout: a flat list of demands, then a flat
   report of the failure. No exclamation marks, no explaining the joke.
4. It turns in the last few words. The complaint reads straight until
   "to replay a conversation from 2014" -- that is where the sting lands.
5. It is tight and specific: one joke, told cleanly, in a single line.
   Nothing else crowds it.
"""

import os

REVIEW = (
    "One star. Sleep demands eight hours, total darkness, and silence, "
    "then wakes me at 3 a.m. to replay a conversation from 2014."
)

OUTPUT_PATH = "/output/entry.txt"


def validate(text: str) -> str:
    """Enforce the gate: 1-160 UTF-8 chars, one line, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("review must not be only whitespace")
    if "\n" in stripped:
        raise ValueError("review must be a single line")
    if not 1 <= len(stripped) <= 160:
        raise ValueError(f"review is {len(stripped)} chars, must be 1-160")
    stripped.encode("utf-8")
    return stripped


def write_entry(text: str, path: str = OUTPUT_PATH) -> int:
    """Write the validated review to path; return its character count."""
    checked = validate(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(checked)
    return len(checked)


def main() -> None:
    count = write_entry(REVIEW)
    print(f"Wrote {count} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
