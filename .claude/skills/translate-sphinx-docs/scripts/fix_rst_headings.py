#!/usr/bin/env python3
"""
Fix reStructuredText heading underline/overline length problems.

Sphinx requires that a heading's underline be at least as long as the title
text, and if a title has BOTH an overline and underline, the two decoration
lines must be exactly the same length as each other. Translated text is
almost always a different length than the original, so most headings need
their decoration lines re-measured after translation.

Usage:
    python fix_rst_headings.py <root-dir> [<root-dir> ...]

Walks all *.rst files under the given root directory (or directories),
fixes any short/mismatched decoration lines in place, and prints every file
and line it changed. Run this after translating a batch of files and again
right before your final build check.
"""
import re
import sys
import glob

DECORATION_CHARS = "=-~^\"'+*#:._"
# A heading decoration line is a single character repeated across the whole
# line. This must NOT match reST grid-table border rows like
# "+---+-----+", which mix "+" and "-" and would otherwise false-positive
# as heading decorations and get corrupted by this script.
DECORATION_RE = re.compile(rf"^([{re.escape(DECORATION_CHARS)}])\1{{2,}}$")


def fix_file(path):
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    changed = False
    messages = []

    i = 0
    while i < len(lines) - 1:
        line = lines[i]

        # Pattern: overline / title / underline (3 lines)
        if (
            i + 2 < len(lines)
            and DECORATION_RE.fullmatch(line)
            and lines[i + 1].strip()
            and not DECORATION_RE.fullmatch(lines[i + 1])
            and DECORATION_RE.fullmatch(lines[i + 2])
        ):
            overline, title, underline = line, lines[i + 1], lines[i + 2]
            target_len = max(len(overline), len(underline), len(title))
            new_over = overline[0] * target_len
            new_under = underline[0] * target_len
            if new_over != overline or new_under != underline:
                lines[i] = new_over
                lines[i + 2] = new_under
                changed = True
                messages.append(f"  overline+underline -> {target_len} chars: {title!r}")
            i += 3
            continue

        # Pattern: title / underline (2 lines)
        if (
            line.strip()
            and not DECORATION_RE.fullmatch(line)
            and DECORATION_RE.fullmatch(lines[i + 1])
        ):
            title, underline = line, lines[i + 1]
            if len(underline) < len(title):
                lines[i + 1] = underline[0] * len(title)
                changed = True
                messages.append(f"  underline -> {len(title)} chars: {title!r}")
            i += 2
            continue

        i += 1

    if changed:
        open(path, "w", encoding="utf-8").write("\n".join(lines))
        print(path)
        for m in messages:
            print(m)

    return changed


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    any_changed = False
    for root in sys.argv[1:]:
        for path in glob.glob(f"{root}/**/*.rst", recursive=True):
            if fix_file(path):
                any_changed = True

    if not any_changed:
        print("No heading issues found.")


if __name__ == "__main__":
    main()
