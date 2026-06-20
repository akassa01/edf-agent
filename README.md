# Engineering Diplomacy — routine version (GitHub delivery)

Runs the weekly workflow as a single **Claude Code routine** on Anthropic's cloud.
It generates two case studies a week into your **personal GitHub repo** — no GCP, no
API key, no Google Drive, nothing touching AirPLAi. Each week you spend ~2 minutes
moving the result into a Word doc on your Tufts OneDrive and sharing it with
Professor Islam. Automation handles the hard part (research + writing); you keep the
final share in your own Tufts/Word world, where you control it and can read it before
he does.

## What's here
- `ROUTINE_PROMPT.md` — paste this as the routine's prompt (the whole logic)
- `STYLE.md` — the voice + structure + your two reference cases
- `state.json` — the routine's memory (rotation, used cases); it updates this itself

## How it behaves
- **Region** rotates one per week through Asia → Europe → Middle East → Africa →
  Americas (`week_index % 5`).
- **Recency** follows a fixed 2:1 pattern (`week_index % 3`): weeks 0/1 get one recent
  + one historical; every third week gets two recent. Exact ratio, no clumping.
- **Scale** is chosen per case and varied against the two most recent entries.
- **No repeats:** every case is logged in `used_cases`; McNamara and Challenger are
  pre-seeded as done.
- **Output each week:** a combined reader file at `published/<date>-<region>.md`, plus
  the two individual cases archived in `case_studies/`, plus updated `state.json`.

## Setup

### 1. Make the repo (personal account)
Create a repo under your **personal GitHub (akassa01)** — private is fine. Add the
three files: `ROUTINE_PROMPT.md`, `STYLE.md`, `state.json`. The routine reads from
here and commits its output + updated memory back here.

### 2. Confirm the connector is your personal GitHub
This is the whole point — the routine writes as whatever GitHub account is connected.
Make sure that's your personal account, not an AirPLAi one. (Your GitHub connector is
already on akassa01.)

### 3. Create the routine
At `claude.ai/code/routines` (or `/schedule` in the CLI):
- Name it ("Engineering Diplomacy weekly").
- Paste the contents of `ROUTINE_PROMPT.md` as the prompt.
- Attach the repo from step 1, and make sure web access is on (for research).
- Trigger: **weekly**.
- Pick a model (Sonnet is plenty; try Opus if you want to compare quality).

### 4. (Optional) Turn on GitHub Pages
In the repo settings, enable Pages on the branch. Then the `published/` files render
as a clean webpage — handy for reading, and for copy-pasting into Word with formatting
intact (select-all on the rendered page → paste into Word).

### 5. Test it once, manually
Trigger a run by hand. Confirm: a new file appeared under `published/`, the two cases
read well, the individual cases got archived, and `state.json` came back with
`week_index` bumped to 1 and two new `used_cases`. If that's all right, the weekly
schedule just keeps doing it.

## Your weekly 2 minutes
When the run finishes (it'll report the file path):
1. Open the new `published/<date>-<region>.md` (or its Pages view).
2. Copy it into a Word doc on your Tufts OneDrive.
3. Share or email it to `shafiqul.islam@tufts.edu`.

That manual step is also your quality check — you see each pair before the professor
does. A quick heads-up to him about the weekly cadence is the courteous touch.

## Things to know
- **Research preview.** Routines can change and access is gated — confirm current run
  limits and that Claude Code on web is enabled on your plan at docs.claude.com. Treat
  it as something you can switch off, not a load-bearing dependency.
- **Why not the connectors directly?** Google Drive on your Claude is AirPLAi's; the
  Microsoft 365 connector is read-only so it can't create Word docs or send mail; and
  you're on one account. Personal GitHub is the one write-capable, non-AirPLAi path —
  hence this design.
- **Randomness.** Recency is deterministic by design. If you want the *scale* picks
  truly random, add a line to the prompt telling the routine to run a one-line shell
  command for the draw.
