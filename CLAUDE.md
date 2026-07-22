# edf-agent repo instructions

## Git workflow

**Local/human work:** commit and push directly to `main`.

**The weekly routine (Claude cloud routine):** runs in a sandbox that puts each run on its
own branch and opens a Pull Request — it does **not** push straight to `main`, and cannot.
So the routine must (a) sync to `origin/main` at the start of every run, and (b) enable
auto-merge on its PR (`gh pr merge --squash --auto`) so the PR lands before the next run.
An unmerged PR left open causes the next run to branch from a stale `main`. See
`ROUTINE_PROMPT.md` steps 0, 12, 14.

## State is computed, not stored

`state.json` holds only static config and the 6 immutable `seed_cases`. It does **not** store
`week_index` or the full `used_cases` corpus — those are derived from the repo by `survey.py`
(`week_index` = count of `published/*.md`; corpus = `seed_cases` + every `case_studies/*.md`
front-matter). Do not reintroduce a hand-maintained corpus counter into `state.json`: that
shared mutable field is what caused weekday runs to overwrite each other. Runs only ever
*add* dated files. Run `python3 survey.py` to see the current survey.
