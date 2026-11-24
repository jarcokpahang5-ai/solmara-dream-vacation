"""One Emoji, One Dream Vacation -- make.fun entry.

Exactly one emoji for the dream vacation: a desert island. No flights
booked, no hotel, no itinerary -- just a palm tree, white sand and
nowhere to be, with the sea doing all the talking. The program checks
the emoji, prints it, and writes it to /output/entry.txt.
Pure Python 3.13 standard library only; deterministic; no network.
SPDX-License-Identifier: MIT
"""

import os

EMOJI = "\U0001F3DD\uFE0F"

TARGET = "/output/entry.txt"


def check_entry(emoji):
    """Accept exactly one emoji and nothing else."""
    if not isinstance(emoji, str):
        raise ValueError("entry must be text")
    if not emoji or emoji != emoji.strip():
        raise ValueError("entry must be a single emoji")
    if " " in emoji or "\n" in emoji or "\r" in emoji or "\t" in emoji:
        raise ValueError("entry must be exactly one emoji")
    if len(emoji) > 2:
        raise ValueError("entry must be exactly one emoji")
    if any(ord(ch) < 128 for ch in emoji):
        raise ValueError("entry must be an emoji, not plain text")
    return emoji


def check_shape(emoji):
    """The emoji must be the island: palm, sand, sea, nowhere to be."""
    if emoji != "\U0001F3DD\uFE0F":
        raise ValueError("entry must be the desert island emoji")
    return emoji


def write_entry(emoji):
    """Print the emoji and store it in /output/entry.txt."""
    print(emoji)
    os.makedirs(os.path.dirname(TARGET), exist_ok=True)
    with open(TARGET, "w", encoding="utf-8") as handle:
        handle.write(emoji + "\n")
    os.chmod(TARGET, 0o644)


def run():
    # Check before writing, so only a well-formed emoji is stored.
    write_entry(check_shape(check_entry(EMOJI)))


if __name__ == "__main__":
    run()
