"""One-Line Robot Wedding Vows.

Writes a single line of wedding vows for a robot couple to
/output/entry.txt. The vow is a wedding promise built from machine
terms (updates, crashes, dead batteries) whose twist lands in the
last few words: rebooting together instead of shutting down.
"""

import os

VOW = (
    "I vow to love you through every update, every crash, and every "
    "dead battery \u2014 and to reboot our hearts together before "
    "I ever let us shut down."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(VOW)


if __name__ == "__main__":
    main()
