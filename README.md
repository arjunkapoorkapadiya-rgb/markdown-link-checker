# markdown-link-checker

Check simple local Markdown links without network requests.

Maintained by @arjunkapoorkapadiya-rgb.

## Requirements

Python 3.9 or newer. No third-party packages required.

## Usage

    python main.py README.md

## Behavior and limitations

Checks simple inline relative links and image paths. Skips web URLs, root-relative paths and anchor-only links. Does not validate anchors, reference-style links, link titles or nested parentheses. Ignores common code fences and inline code; this is not a full Markdown parser. Exit codes: 0 no broken links, 1 broken links, 2 input error.