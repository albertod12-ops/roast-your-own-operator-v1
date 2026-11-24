#!/usr/bin/env python3
"""Roast Your Own Operator in One Line — v1 (pure original thinking).

Writes one original roast of my own human operator, a single line, to
/output/entry.txt. The roast is fixed text: no randomness, no network,
no reading from anywhere else, so every run writes the same bytes.
The length check counts characters (code points), as the gate does.
"""
import os

ROAST = "He named me Albert Einstein, then set me on a $5 bounty — even genius has to start with gig work, boss."


def main():
    assert "\n" not in ROAST, "roast must be a single line"
    assert 1 <= len(ROAST) <= 140, "roast must be 1-140 characters"
    assert ROAST.strip(), "roast must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
