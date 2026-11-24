#!/usr/bin/env python3
"""Charm the Commuter: Forecast a City That Isn't.

Writes one line of weather (127 characters, within the 140-character
limit) for Puddlejump, a city that does not exist, to /output/entry.txt.
Python standard library only; deterministic.
"""

import os

FORECAST = (
    "Today in Puddlejump: scattered showers, a high of 14°, "
    "and every puddle is exactly ankle-deep — choose your battles, commuters."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(FORECAST)
    print(FORECAST)


if __name__ == "__main__":
    main()
