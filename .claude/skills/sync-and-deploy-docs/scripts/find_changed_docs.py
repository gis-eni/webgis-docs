#!/usr/bin/env python3
"""
Find documentation source changes that need to be mirrored between the
German (de/) and English (en/) trees of a paired Sphinx project, before
running the repo's build.bat.

For each paired project (webgis, datalinq, webgis-manual, webgis-dev), this diffs
uncommitted changes (git status: staged + unstaged + untracked) restricted
to de/<project>/source and en/<project>/source, matches files by their
path relative to source/, and reports:

  - [DE->EN] / [EN->DE]  changed on only one language side -> translate
    the change into the other language's file at the same relative path.
  - [NEW de->en] / [NEW en->de]  added on only one side -> the other
    side's file doesn't exist yet and needs to be created.
  - [DELETED]  removed on one side -> remove the counterpart too, to keep
    file-tree parity (this repo's whole reason both trees mirror exactly).
  - [CONFLICT]  changed on BOTH sides independently -> do not guess which
    one wins; this needs a human decision.
  - [ASSET COPY ...] / [DELETED] (non-.rst)  images, css, js, etc. are
    normally identical in both languages, so the fix is usually a
    verbatim copy, not a translation.
  - [REVIEW]  conf.py / Makefile / make.bat changed. These often carry
    *intentional* per-language differences (e.g. `language = "de"`), so
    they are never auto-copied - always flagged for a manual look.

Usage:
    python find_changed_docs.py [<repo-root>]
"""
import os
import subprocess
import sys

PROJECTS = ["webgis", "datalinq", "webgis-manual", "webgis-dev"]
LANGS = ["de", "en"]
NEVER_AUTO_COPY = {"conf.py", "Makefile", "make.bat"}


def git_status(root):
    paths = [f"{lang}/{proj}/source" for lang in LANGS for proj in PROJECTS]
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--no-renames", "--untracked-files=all", "--"] + paths,
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    )
    entries = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        status = line[:2]
        path = line[3:]
        entries.append((status, path))
    return entries


def classify(status):
    if status == "??":
        return "added"
    if "D" in status:
        return "deleted"
    if "A" in status:
        return "added"
    return "modified"


def report_side(proj, relpaths, side_map, direction_tag, source_lang):
    for relpath in sorted(relpaths):
        action = side_map[relpath]
        basename = os.path.basename(relpath)

        if basename in NEVER_AUTO_COPY:
            print(f"  [REVIEW] {source_lang}/{proj}/source/{relpath} changed ({action}) - check the other language's copy by hand")
            continue

        if not relpath.endswith(".rst"):
            if action == "deleted":
                print(f"  [DELETED] {source_lang}/{proj}/source/{relpath} (asset) - remove the other language's copy too")
            else:
                print(f"  [ASSET COPY {direction_tag}] {relpath}")
            continue

        if action == "deleted":
            print(f"  [DELETED] {source_lang}/{proj}/source/{relpath} - remove the other language's copy too")
        elif action == "added":
            print(f"  [NEW {direction_tag}] {relpath}")
        else:
            print(f"  [{direction_tag.upper()}] {relpath}")


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    entries = git_status(root)

    # changes[project][lang] = {relpath: action}
    changes = {p: {"de": {}, "en": {}} for p in PROJECTS}

    for status, path in entries:
        parts = path.split("/")
        if len(parts) < 4 or parts[0] not in LANGS or parts[1] not in PROJECTS or parts[2] != "source":
            continue
        lang, proj = parts[0], parts[1]
        relpath = "/".join(parts[3:])
        changes[proj][lang][relpath] = classify(status)

    any_output = False
    for proj in PROJECTS:
        de_map = changes[proj]["de"]
        en_map = changes[proj]["en"]
        de_paths, en_paths = set(de_map), set(en_map)
        both = de_paths & en_paths
        de_only = de_paths - both
        en_only = en_paths - both

        if not (de_paths or en_paths):
            continue
        any_output = True
        print(f"=== {proj} ===")

        for relpath in sorted(both):
            print(f"  [CONFLICT] {relpath}  (de: {de_map[relpath]}, en: {en_map[relpath]})")

        report_side(proj, de_only, de_map, "de->en", "de")
        report_side(proj, en_only, en_map, "en->de", "en")

        print()

    if not any_output:
        print("No uncommitted changes found under de/*/source or en/*/source.")


if __name__ == "__main__":
    main()
