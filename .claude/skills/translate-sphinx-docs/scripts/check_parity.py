#!/usr/bin/env python3
"""
Verify that a translated Sphinx docs tree has exactly the same set of
files (same relative paths, same case) as its source-language tree.

Why this matters: Sphinx derives an HTML page's output filename from its
source document's filename, not from its title. If the translated tree's
.rst files (and image/asset files) don't have identical relative paths to
the source tree, the published URLs won't line up between languages
(e.g. /de/webgis/config/index.html vs /en/webgis/configuration/index.html)
even though the only thing that's supposed to differ is the /de/ vs /en/
path segment.

Usage:
    python check_parity.py <source-dir> <target-dir>

Example:
    python check_parity.py de/webgis/source en/webgis/source

Exits 0 and prints "OK" if the trees match exactly. Otherwise lists every
path that's missing from the target, or present in the target but not the
source, and exits 1.
"""
import sys
import os


def list_files(root):
    result = set()
    for dirpath, _dirnames, filenames in os.walk(root):
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            result.add(rel.replace(os.sep, "/"))
    return result


def main():
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)

    source_dir, target_dir = sys.argv[1], sys.argv[2]
    source_files = list_files(source_dir)
    target_files = list_files(target_dir)

    missing = sorted(source_files - target_files)
    extra = sorted(target_files - source_files)

    if not missing and not extra:
        print(f"OK - {len(source_files)} files match exactly between:")
        print(f"  {source_dir}")
        print(f"  {target_dir}")
        sys.exit(0)

    if missing:
        print(f"MISSING from target ({len(missing)}):")
        for f in missing:
            print(f"  {f}")
    if extra:
        print(f"EXTRA in target, not in source ({len(extra)}):")
        for f in extra:
            print(f"  {f}")
    sys.exit(1)


if __name__ == "__main__":
    main()
