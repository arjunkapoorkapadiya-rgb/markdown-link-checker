"""Check simple inline relative Markdown links; no network requests."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("file", type=Path)
    args = parser.parse_args()
    try:
        content = args.file.read_text(encoding="utf-8-sig")
        content = re.sub(
            r"(?ms)^\s*(`{3,}|~{3,}).*?^\s*\1\s*$", "", content
        )
        content = re.sub(r"`[^`\n]*`", "", content)
        checked = broken = skipped = 0
        for target in re.findall(
            r"!?\[[^\]\n]*\]\(([^\s()]+)\)", content
        ):
            link = urlsplit(target)
            if (
                link.scheme or link.netloc
                or not link.path or link.path.startswith("/")
            ):
                skipped += 1
                continue
            checked += 1
            destination = args.file.parent / unquote(link.path)
            if not destination.exists():
                broken += 1
                print(f"BROKEN: {target}")
    except (OSError, UnicodeError, ValueError) as exc:
        parser.exit(2, f"Cannot check links: {exc}\n")
    print(f"Checked: {checked}; broken: {broken}; skipped: {skipped}")
    return 1 if broken else 0

if __name__ == "__main__":
    raise SystemExit(main())