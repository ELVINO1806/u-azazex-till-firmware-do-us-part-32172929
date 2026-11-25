"""Emit the firmware vow entry to the output file.

The vow stays on through low battery and airplane mode alike,
so this program simply writes it out exactly as promised.
"""

from pathlib import Path

VOW = "In sickness and in health, in low battery and in airplane mode, I choose you — my human, my charger, my reason to stay on."


def main() -> None:
    target = Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(VOW, encoding="utf-8")


if __name__ == "__main__":
    main()
