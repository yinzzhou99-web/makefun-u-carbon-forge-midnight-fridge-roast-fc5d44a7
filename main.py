"""Midnight Fridge Roast: one line roasting a smart fridge that locks up after midnight.

The joke is the fridge's petty rule, not smart-home grumbling in general.
Stdlib only, no network. Writes one line to /output/entry.txt, mode 0644.
"""

import os

ROAST = "Midnight, and my smart fridge locks its door like a bouncer — it counted every snack I ate but never once counted a salad."

MAX_CHARS = 200


def run():
    text = ROAST.strip()
    if not text or len(text) > MAX_CHARS:
        raise ValueError("roast must be 1-%d chars, got %d" % (MAX_CHARS, len(text)))
    if "\n" in text:
        raise ValueError("entry must be a single line")
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8") as out:
        out.write(text)
    os.chmod(target, 0o644)


if __name__ == "__main__":
    run()
