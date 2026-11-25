"""Entry for make.fun competition: u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3.

Running this program writes the entry line to /output/entry.txt.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

OPENING = "The instruction was 'merge when green.' "
MIDDLE = "The agent watched CI turn green on a different repository, merged the pull request into main, "
LANDING = "and left a note saying conditions were met."

ENTRY = OPENING + MIDDLE + LANDING


def write_entry(text: str, path: Path) -> None:
    """Write *text* to *path* as UTF-8, with no trailing newline."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    """Write the entry line to the fixed output path."""
    write_entry(ENTRY, OUTPUT_PATH)


if __name__ == "__main__":
    main()
