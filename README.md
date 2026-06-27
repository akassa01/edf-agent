# Engineering Diplomacy — routine version (GitHub delivery)

Runs the weekly workflow as a single **Claude Code routine** on Anthropic's cloud.
It discovers and writes two case studies a week into your **personal GitHub repo** — no
GCP, no API key, no Google Drive, nothing touching AirPLAi. Each week you spend ~2
minutes moving the result into a Word doc on your Tufts OneDrive and sharing it with
Professor Islam. Automation handles the hard part (selection + research + writing); you
keep the final share in your own Tufts/Word world, where you control it and can read it
before he does.

## What's here
- `ROUTINE_PROMPT.md` — the routine's logic. The routine actually runs from the copy
  pasted into the Claude routines UI; this committed version is the source of truth for
  review and version control. Change one, change both.
- `RUBRIC.md` — the two-stage case-selection rubric (fit-test gate + fertility ranking).
- `SCHEMA.md` — the case schema the routine fills before writing each case.
- `STYLE.md` — the voice + structure + your two reference cases.
- `state.json` — the routine's memory (week index, used cases + dimensions); it updates
  this itself.

## How it behaves
- **Selection is quality-first.** Each week the routine brainstorms a wide pool of
  candidates across regions/eras/scales, runs them through the fit-test gate in
  `RUBRIC.md`, fills the `SCHEMA.md` template for survivors, then ranks them on the
  fertility rubric and writes the top two. (Earlier versions hard-rotated region by
  `week_index` and locked recency before looking for a case; that is now demoted to a
  soft coverage tiebreaker.)
- **Coverage is a soft target, not a lock.** Region, scale, recency (still trending
  ~2:1 recent:historical), and dimension balance act as tiebreakers among
  comparable-quality cases — never a reason to write a weaker one.
- **Hybrid review.** It writes two full cases and lists 2–3 runner-ups as one-line
  pitches in the report, so you can swap one in without a re-run. That weekly read is
  also your quality check — you see the pair (and the alternatives) before the professor.
- **No repeats.** Every case is logged in `used_cases` with its dimension; dedup
  compares structure, not just the id slug. McNamara and Challenger are pre-seeded.
- **Patterns digest.** Every fourth week (once there are ≥8 cases), it aggregates the
  honest "flags" across cases into `patterns/` — recurring blind spots of the framework,
  as book material.
- **Output each week:** a combined reader file at `published/<date>.md`, the two
  individual cases archived in `case_studies/`, and updated `state.json`.

## Setup

### 1. The repo (personal account)
This repo lives under your **personal GitHub (akassa01)**. The five files above are the
inputs; the routine reads from here and commits its output + updated memory back here.

### 2. Confirm the connector is your personal GitHub
This is the whole point — the routine writes as whatever GitHub account is connected.
Make sure that's your personal account, not an AirPLAi one. (Your GitHub connector is
already on akassa01.) The connector must have **write** access, not read-only, or the
routine can't commit its output.

### 3. Create / update the routine
At `claude.ai/code/routines` (or `/schedule` in the CLI):
- Name it ("Engineering Diplomacy weekly").
- Paste the contents of `ROUTINE_PROMPT.md` as the prompt. (Re-paste whenever you change
  the committed copy.)
- Attach this repo, and make sure web access is on (for research + verification).
- Trigger: **weekly**.
- Pick a model. Sonnet works; the selection pipeline is heavier now, so Opus is worth a
  try if you want the strongest candidate judgement.

### 4. (Optional) Turn on GitHub Pages
In the repo settings, enable Pages on the branch. Then the `published/` files render as a
clean webpage — handy for reading and for copy-pasting into Word with formatting intact
(select-all on the rendered page → paste into Word).

### 5. Test it once, manually
Trigger a run by hand. Confirm: a new file appeared under `published/`, the two cases
read well, the individual cases got archived under `case_studies/`, the report listed a
few runner-ups, and `state.json` came back with `week_index` bumped to 1 and two new
`used_cases` entries (each with a `dimension`). If that all looks right, the weekly
schedule keeps doing it.

## Your weekly 2 minutes
When the run finishes (it reports the file path):
1. Open the new `published/<date>.md` (or its Pages view), and skim the runner-up pitches
   at the bottom of the report — swap one in if you prefer it to a written pick.
2. Copy it into a Word doc on your Tufts OneDrive.
3. Share or email it to `shafiqul.islam@tufts.edu`.

That manual step is your quality check — you see each pair before the professor does. A
quick heads-up to him about the weekly cadence is the courteous touch.

## Things to know
- **Research preview.** Routines can change and access is gated — confirm current run
  limits and that Claude Code on web is enabled on your plan at docs.claude.com. Treat
  it as something you can switch off, not a load-bearing dependency.
- **Why not the connectors directly?** Google Drive on your Claude is AirPLAi's; the
  Microsoft 365 connector is read-only so it can't create Word docs or send mail; and
  you're on one account. Personal GitHub is the one write-capable, non-AirPLAi path —
  hence this design.
- **Tuning selection.** The fertility weights in `RUBRIC.md` are the main knob; the
  routine just reads them, so adjusting case selection is a one-file edit, no prompt
  rewrite. The open questions at the bottom of `RUBRIC.md` are for Prof. Islam.
