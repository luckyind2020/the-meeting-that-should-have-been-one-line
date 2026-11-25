"""The meeting, replaced by a single line."""

from pathlib import Path


def load_line() -> str:
    line = Path(__file__).with_name("entry.txt").read_text(encoding="utf-8").strip()
    if not line:
        raise SystemExit("entry.txt is empty — nothing to say in this meeting.")
    return line


def main() -> None:
    print(load_line())


if __name__ == "__main__":
    main()
