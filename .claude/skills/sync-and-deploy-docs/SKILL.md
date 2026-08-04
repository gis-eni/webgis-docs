---
name: sync-and-deploy-docs
description: Before running this repo's build.bat to deploy the Sphinx documentation (build.bat renders every project into app/, which a GitHub Action publishes on push), check what has changed in the German (de/) and English (en/) doc source trees and mirror those changes into the other language first, so de/ and en/ never drift out of sync. Use this skill whenever the user asks to "deploy the docs", "run build.bat", "publish the documentation", "sync the docs before deploying", or says they've edited docs in one language and want the other language caught up before building/publishing. This is the pre-deploy counterpart to the translate-sphinx-docs skill (which does full-project translation) - use this one for the smaller, incremental "what changed since last time" sync.
---

# Sync doc changes between languages, then deploy via build.bat

## What this is for

This repo publishes documentation in paired language trees: `de/webgis`,
`de/datalinq`, `de/webgis-manual`, `de/webgis-dev` and their English
counterparts `en/webgis`, `en/datalinq`, `en/webgis-manual`,
`en/webgis-dev`. Both sides must stay a
structural mirror of each other (same files, same relative paths) so that
published URLs only differ by the `/de/`/`/en/` segment — see the
`translate-sphinx-docs` skill for the full rationale and the rules for
translating content.

The top-level `build.bat` builds every one of those projects with Sphinx
and `robocopy /MIR`s each project's `build/html` into the matching
`app/<lang>/<project>` directory. A GitHub Action deploys whatever is
committed under `app/` when it's pushed. So the deploy pipeline is:

```
edit de/ or en/ source  -->  sync the other language  -->  build.bat  -->  commit & push app/
```

This skill covers the **sync** step, which is easy to forget: someone
edits `de/webgis/source/config/index.rst` and runs `build.bat` straight
away — the German docs update, but the English docs silently keep
describing the old behavior, forever, until someone happens to notice.

This skill does **not** commit or push anything by itself. It syncs
source files and (optionally, after you confirm) runs `build.bat`. Git
staging/committing/pushing is a separate, explicit step — same rule as
everywhere else in this repo: never commit without being asked.

## Step 0 — Find what changed

Run the bundled script from the repo root. It compares **uncommitted**
changes (staged + unstaged + untracked — i.e. `git status`, not a
specific commit range) restricted to the six paired `source/` trees:

```bash
python .claude/skills/sync-and-deploy-docs/scripts/find_changed_docs.py
```

It groups output per project (`webgis`, `datalinq`, `webgis-manual`) into:

- `[DE->EN]` / `[EN->DE]` — an existing file changed on only one
  language side. Translate the change into the other side's file at the
  same relative path.
- `[NEW de->en]` / `[NEW en->de]` — a file was added on only one side.
  The counterpart doesn't exist yet and needs to be created from scratch.
- `[DELETED]` — a file was removed on one side. Remove the counterpart
  too, or file-tree parity breaks.
- `[CONFLICT]` — the *same relative path* changed on **both** sides
  independently. Don't guess which one is authoritative — see Step 1.
- `[ASSET COPY de->en]` / `[ASSET COPY en->de]` — a non-`.rst` file
  changed (image, css, js, ...). These are normally identical in both
  languages, so the fix is usually a straight file copy, not a
  translation.
- `[REVIEW]` — `conf.py`, `Makefile`, or `make.bat` changed. These often
  carry *intentional* per-language differences (`conf.py`'s `language =
  "de"` line, project-specific settings), so they are never auto-copied.
  Read the actual diff and decide what, if anything, needs mirroring.

If the script prints nothing (or says "No uncommitted changes found"),
there's nothing to sync — skip straight to Step 4.

## Step 1 — Resolve conflicts first, before touching anything else

A `[CONFLICT]` means both language versions of the same file were edited
independently since the last commit. Don't silently pick one side:

- Show the user both diffs (`git diff -- de/PROJECT/source/RELPATH` and
  `git diff -- en/PROJECT/source/RELPATH`).
- Ask whether they're the same underlying change made twice (in which
  case just verify they're now equivalent and move on), or genuinely
  different edits that both need to be kept (in which case merge by hand
  and ask the user to confirm the result).

## Step 2 — Propagate the changes

For everything the script listed apart from conflicts and REVIEW items:

**Modified `.rst` files (`[DE->EN]` / `[EN->DE]`)**

Look at the actual diff, not just the fact that the file changed:

```bash
git diff -- de/PROJECT/source/RELPATH
```

Apply an equivalent change to the target file at the same relative path
— translate the new/changed prose, keep everything else (headings,
`toctree` entries, code blocks, indentation) untouched to minimize the
diff. This is a targeted edit, not a re-translation of the whole file;
re-translating from scratch risks introducing unrelated wording drift in
sentences that didn't actually change.

**New files (`[NEW de->en]` / `[NEW en->de]`)**

The counterpart doesn't exist. Create it by following the
`translate-sphinx-docs` skill's Step 2 rules (what to translate, what not
to, preserving indentation exactly) for this one file, at the identical
relative path in the target tree. If the new file is referenced from a
`toctree` in its directory's `index.rst`, add the equivalent entry to the
target language's `index.rst` too.

**Deleted files (`[DELETED]`)**

Delete the counterpart file. Check whether it was referenced from a
`toctree` or a `:ref:`/`:doc:` cross-reference elsewhere in that
language's tree, and remove/update those references too — a dangling
`toctree` entry is a build warning waiting to happen.

**Assets (`[ASSET COPY ...]`)**

Copy the file verbatim to the same relative path in the other language
tree. Don't try to "translate" an image — if a screenshot's on-screen
text is genuinely language-specific, flag it for the user rather than
guessing; most screenshots in this repo are shared as-is between
languages (see `translate-sphinx-docs`'s Step 1 note on `_static`/`img`).

**`[REVIEW]` items**

Read the actual diff. A `conf.py` diff that only touches something
unrelated to `language` (a new extension, an html_theme option) probably
should be mirrored; a diff that's just the `language` line changing (or
already differs on purpose) should not be. When genuinely unsure, ask.

## Step 3 — Verify before building

Reuse the `translate-sphinx-docs` skill's scripts on every project you
touched:

```bash
python .claude/skills/translate-sphinx-docs/scripts/fix_rst_headings.py en/PROJECT/source de/PROJECT/source
python .claude/skills/translate-sphinx-docs/scripts/check_parity.py de/PROJECT/source en/PROJECT/source
```

`check_parity.py` must report `OK` for every project you touched before
moving on — it's the check that actually guarantees stable URLs.

## Step 4 — Run build.bat

```bash
./build.bat
```

Expect this to touch **every** project's `app/<lang>/<project>` output,
not just the one(s) you synced — `build.bat` rebuilds the whole doc set
unconditionally, `robocopy /MIR`-ing each project's fresh `build/html`
over its `app/` target. That's normal, not a sign something went wrong;
Sphinx builds aren't always byte-identical run to run even with unchanged
source (search index ordering, `objects.inv` layout), so previously
untouched projects can show up as modified in `git status` afterwards
too. Skim the diff for anything that looks like actual content loss
before assuming it's just build churn.

## Step 5 — Hand back to the user

Summarize what was synced (project, files, direction) and what
`build.bat` changed in `app/`. Do **not** `git add`/`commit`/`push`
without being explicitly asked — per this repo's established workflow,
committing and especially pushing (which triggers the GitHub Actions
deploy) is the user's call, every time.

## Common pitfalls

- **A brand new project's entire tree looks like one line of `git status`
  output.** Plain `git status` doesn't recurse into a directory that's
  100% untracked — it reports the directory itself, not the dozens of
  files inside it. The bundled script passes `--untracked-files=all` to
  avoid this (safe here since it's scoped to a handful of known
  `source/` paths, not the whole repo), but if you ever query `git
  status` yourself while syncing, remember plain `git status` will
  undercount a wholesale-new project the same way.
- **Diffing the whole file instead of the actual change.** Re-translating
  a modified file from scratch instead of localizing just the diff
  produces a huge, hard-to-review change and risks silently altering
  sentences that were never touched. Work from `git diff`.
- **Treating REVIEW items like ASSET items.** `conf.py`/`Makefile`/
  `make.bat` frequently have deliberate per-language differences. Never
  blindly copy them — always read the diff first.
- **Case-only path differences on Windows.** This repo's git history has
  at least one directory (`.../general/Redlining/` vs. `redlining/`)
  where the path git has tracked differs only in case from what's
  actually on disk. Windows/NTFS is case-insensitive and this repo has
  `core.ignorecase=true`, so editing the on-disk file doesn't always
  register as a change in `git status` if the case doesn't match what
  git expects, and tools that shell out to `git status` (like this
  skill's own script) inherit that blind spot. If a sync seems to have
  missed an obviously-edited file, double-check with `git diff --stat`
  directly on that exact path before concluding nothing changed.
- **Forgetting `toctree`/`:ref:` cleanup on deletes.** Removing a file
  without removing what pointed to it turns into a `sphinx-build`
  warning the next time someone builds — catch it in Step 3, not later.
- **Running `build.bat` and being surprised by the size of the diff.**
  It rebuilds every project every time. See Step 4 — this is expected.

## Bundled scripts

- `scripts/find_changed_docs.py [<repo-root>]` — diffs uncommitted
  changes across all six paired `source/` trees and reports what needs
  syncing where, per the categories in Step 0. Plain Python 3, no
  third-party dependencies; shells out to `git status --porcelain`.

## Related skill

`translate-sphinx-docs` — use it for full-project translation (a brand
new project, or a whole missing section), and as the reference for *how*
to translate: what to translate vs. leave alone, indentation rules,
heading-underline fixing, and the file-parity philosophy this skill
builds on.
