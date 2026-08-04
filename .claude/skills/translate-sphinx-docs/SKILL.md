---
name: translate-sphinx-docs
description: Translate a Sphinx/reStructuredText documentation project from one language into another (e.g. German docs into an English tree, or vice versa), producing a target-language tree that is a structural mirror of the source — same subdirectories, same filenames, same code/config blocks, same table and code-block indentation — so that after publishing, the only difference between the two languages' URLs is the language path segment. Use this skill whenever the user asks to translate documentation, create an English/German/other-language version of a docs folder, "port" or "sync" a Sphinx project into a new locale, or complains that a language version of the docs is missing sections, stubs, or placeholders compared to the other language. Also use it if the user wants to verify that an existing translated docs tree is complete and structurally consistent with its source.
---

# Translating Sphinx / reStructuredText Documentation

## What this is for

A source-language Sphinx project (say `de/webgis/source/`) needs a
target-language counterpart (`en/webgis/source/`) that:

1. Renders the same information, translated.
2. Has the **exact same file tree** — same directories, same filenames,
   same case — so published URLs only differ by the language segment
   (`/de/...` vs `/en/...`). Sphinx builds an HTML page's output filename
   from its *source document's filename*, never from its title, so this is
   a hard structural requirement, not a style preference.
3. Builds cleanly with `sphinx-build`, no warnings, no errors.
4. Keeps code blocks, config keys, list-tables, and directive indentation
   byte-for-byte structurally identical to the source — only the prose,
   comments, and human-readable labels change.

This is usually a big, mechanical, multi-file job. Treat it as one:
inventory first, translate in digestible chunks, verify continuously, and
do one final full-tree comparison at the end. Don't try to translate
everything in one giant pass and only check at the very end — heading
errors and indentation drift compound and get tedious to track down after
the fact.

## Step 0 — Scope the job

Before touching files, figure out:

- Which project (there may be several docs projects in one repo, e.g. a
  main product doc plus a sub-tool's doc — check for multiple
  `conf.py`/`Makefile` pairs).
- Source and target language, and whether the target tree already exists
  partially (previous incomplete translation attempt, stub files with
  placeholder text like "This section will describe...", etc.).
- Whether the user wants the whole project or a specific section first —
  for a large project, agree to go section by section and check in after
  each one rather than disappearing for a long single pass.

Get an inventory before writing anything:

```bash
find de/PROJECT/source -name "*.rst" | wc -l
find en/PROJECT/source -name "*.rst" | wc -l
python .claude/skills/translate-sphinx-docs/scripts/check_parity.py de/PROJECT/source en/PROJECT/source
```

If counts already match, don't assume the target is done — stub files
count too. Spot-check a few target files for placeholder content
("This section will cover...", a title with no body) before declaring
victory.

## Step 1 — Scaffold the target project (once, if it doesn't exist yet)

Copy the source project's structure so far as it's non-content:

- `Makefile`, `make.bat` (build entry points — copy verbatim).
- `source/conf.py` — copy, then change only the `language = "de"` line to
  the target language code (`"en"`, etc.). Leave `project`, theme, and
  extension settings alone unless the user says otherwise.
- `source/_static/` (custom CSS/JS/logo assets) — copy verbatim. These are
  almost never language-specific; check quickly for embedded text before
  assuming so, but don't skip this directory — a missing `_static` with a
  `conf.py` that references `html_css_files`/`html_js_files` will silently
  produce an unstyled build, not a build error.
- Every `img/` (or similarly named image) directory — copy verbatim,
  matched to the exact same relative path as the source. Do this
  directory-by-directory as you translate each section, not all at once
  up front, so you don't forget one buried three levels deep.

## Step 2 — Translate section by section

Follow the **project's own toctree order**, not alphabetical order — it
reflects how the maintainers think about the content and makes it easier
for the user to track progress ("done with Installation, now doing
Configuration"). For a large project, translate one toctree branch fully
(including its images), verify it, and only then move to the next.

For each `.rst` file:

- Read the source file in full before translating — don't guess structure
  from a partial read.
- Translate prose, table cell text, image `:alt:` text, admonition bodies
  (note/warning/tip/etc.), and comments inside code blocks.
- Do **not** translate: config/API keys, XML/JSON attribute names and
  values, code identifiers, CLI flags, file paths, URLs.
- Do **not** "fix" typos or grammar inside literal console/terminal
  transcripts or other verbatim tool output blocks, even if they look
  wrong. That text is what the user's screen will actually show when they
  run the command — silently "correcting" it makes the docs inaccurate,
  not better. Preserve it exactly as the source shows it, translating only
  any German words that are prose rather than literal output.
- Preserve the **exact indentation** of every code-block, list-table, and
  nested directive body from the source — same number of spaces or tabs,
  at the same nesting level. If the source uses tabs in one place and
  spaces in another, match that per-location, don't normalize it. This
  isn't about Sphinx correctness (both usually render fine); it's about
  keeping the two language trees easy to diff and maintain side by side,
  which is the whole point of mirroring the structure.
- Where an example uses domain data that isn't really "language" (sample
  SQL, a made-up German street name in a tutorial screenshot, a JSON
  payload with German field values from a real system) — leave it as is
  unless translating it is clearly what the user wants. When in doubt,
  translate the explanatory prose around the example and leave the
  example's literal content alone.
- Copy any `img/` files the new file references, at the matching relative
  path, before moving on.

After translating a batch of files, run the heading fixer (see below)
before doing a build check — most "heading underline too short" or
"overline & underline mismatch" errors come from translated titles being a
different length than the original, and it's much faster to fix them in
bulk than one Sphinx error at a time.

```bash
python .claude/skills/translate-sphinx-docs/scripts/fix_rst_headings.py en/PROJECT/source
```

This rewrites any heading whose underline is shorter than its title, and
any heading with an overline+underline pair whose two decoration lines
don't match each other in length (a `CRITICAL: Title overline & underline
mismatch` build error). It's idempotent — safe to run repeatedly.

## Step 3 — Verify with a real build, incrementally

Don't wait until the whole project is translated to build it once. Build
after each section:

```bash
cd en/PROJECT
rm -rf build
sphinx-build -b html -E source build/html 2>&1 | grep -iE "warning|error|critical"
rm -rf build
```

(`-E` forces a full re-read so stale cached state doesn't hide problems;
delete `build/` afterwards so you're not accidentally committing build
output — check whether the repo's `.gitignore` already excludes `build/`,
most Sphinx projects do.)

Expected, OK-to-ignore warnings mid-project:

- `toctree contains reference to nonexisting document 'X'` for sections
  you haven't translated yet.
- `undefined label: 'Y'` for a `:ref:` target that lives in a
  not-yet-translated file.

Both of these should disappear once the whole project is done — if either
is still present in the final full-project build, something was missed.

Anything else (heading errors, malformed directives, broken image paths,
bad list-table structure) should be fixed immediately, not deferred.

## Step 4 — Final whole-tree checks

Once every file is translated:

1. Re-run the heading fixer one more time over the whole tree (cheap
   insurance).
2. Full clean build, zero tolerance:

   ```bash
   cd en/PROJECT
   rm -rf build
   sphinx-build -b html -E source build/html 2>&1 | grep -iE "warning|error|critical"
   ```

   This should now print nothing at all.

3. **File parity check** — this is the check that actually matters most to
   the user, because it's what guarantees stable URLs after publishing:

   ```bash
   python .claude/skills/translate-sphinx-docs/scripts/check_parity.py \
       de/PROJECT/source en/PROJECT/source
   ```

   This diffs *every* file (not just `.rst` — images, `_static`, `conf.py`,
   everything) by relative path, case-sensitive. It must report `OK` with
   an exact file count match. If it doesn't, the mismatch list tells you
   exactly what's missing or extra.

4. If the repo has a top-level build script (e.g. `build.bat`,
   `Makefile`) that builds each language/project into a published output
   directory, check whether it already has a target for the project you
   just translated. If not, add one, following the existing pattern for
   sibling targets exactly (same `robocopy`/`cp` structure, same output
   path shape, just a different project/language pair).

## Step 5 — Committing

Translating a big docs tree usually happens in a repo that has *other*,
unrelated in-progress changes (someone else's edits to the source-language
docs, a partially rebuilt output directory, editor settings, etc.). Don't
sweep those into your commit:

- Stage precisely: `git add en/PROJECT/` (the exact tree you created/
  changed), not `git add -A` or `git add .`.
- Run `git status --short` on what's staged vs. not staged and confirm the
  unstaged list is exactly the pre-existing unrelated stuff, nothing you
  touched.
- Double check you haven't accidentally modified a source-language file —
  it's easy for an overly broad `glob`/`find` pattern in a bulk-fix script
  to match `de/**/*.rst` as well as `en/**/*.rst` if the pattern wasn't
  anchored carefully. If `git diff` shows a source-language file you
  didn't mean to touch, `git checkout -- <file>` it before committing.
- Write a commit message that states the file/line-count scope (helps
  reviewers gauge the size at a glance) and explicitly calls out that
  filenames mirror the source tree 1:1.

## Common pitfalls (from experience)

- **Heading overline without matching underline fix.** A script that only
  extends underlines to match a new (translated) title length, without
  also checking for a paired overline, produces a heading where overline
  and underline are now different lengths — a *build-breaking* `CRITICAL`
  error, worse than the "too short" warning you started with. Always fix
  overline+underline pairs together (see `fix_rst_headings.py`).
- **"Correcting" verbatim console output.** Real terminal transcripts
  sometimes contain typos or awkward phrasing that's *actually what the
  tool prints* (a program's own English string, even if grammatically
  rough). Translating/fixing it makes the docs lie about what the user
  will see on screen. Only translate text that's genuinely the
  document author's prose.
- **Tabs vs. spaces drift.** Retyping a block by hand instead of
  preserving it exactly tends to normalize indentation to whatever the
  editor defaults to. Copy the structural skeleton (indentation, blank
  lines) from the source and only substitute the translated words, rather
  than free-typing a new paragraph with "equivalent" formatting.
- **Toctree settings silently changed.** A prior partial translation pass
  may have simplified a `:maxdepth:` or dropped a `:caption:` compared to
  the source. Diff these directives too, not just the prose — they affect
  navigation, not just content.
- **Stub files masquerading as "done".** A target file with a title and
  one placeholder sentence ("This section will describe...") will make a
  naive file-count comparison look complete. Spot-check content, not just
  counts, especially on a partially-pre-existing target tree.
- **Declaring victory on file *count* instead of file *identity*.** Two
  trees can have the same number of files with different names/paths.
  Always finish with `check_parity.py`'s full-path diff, not just
  `find | wc -l` on both sides.

## Bundled scripts

- `scripts/fix_rst_headings.py <dir> [<dir> ...]` — walks all `.rst`
  files under the given root(s) and fixes heading underline/overline
  length problems in place, printing every file and line changed. Safe to
  run repeatedly; a no-op on files that are already correct.
- `scripts/check_parity.py <source-dir> <target-dir>` — recursively
  diffs two directory trees by relative path (case-sensitive, every file
  type). Prints `OK` and exits 0 on an exact match; otherwise lists what's
  missing/extra and exits 1.

Both are plain Python 3 with no third-party dependencies.
