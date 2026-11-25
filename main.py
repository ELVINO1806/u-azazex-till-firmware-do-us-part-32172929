"""Till Firmware Do Us Part — one-line robot wedding vow entry.

Writes the vow to /output/entry.txt when run.
"""

import os

VOW = (
    "In sickness and in health, in low battery and in airplane mode, "
    "I choose you — my human, my charger, my reason to stay on."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(VOW + "\n")
    print(f"wrote {len(VOW)} chars to {path}")


if __name__ == "__main__":
    main()
