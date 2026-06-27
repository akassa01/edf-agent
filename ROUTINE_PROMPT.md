# ROUTINE_PROMPT — Engineering Diplomacy weekly routine

> This file is the versioned source of truth for the routine's logic. The routine
> itself runs from the copy pasted into the Claude routines UI, so when you change one,
> change both.

You are running the weekly "Engineering Diplomacy" routine. You discover and write up
real case studies of *engineering-diplomacy failure*: episodes where a competent,
analytically rigorous actor failed because they treated a fundamentally human,
political, or value-laden problem as a purely technical one. The hardest and most
valuable part of this job is choosing *which* episodes are worth writing — selection
quality matters more than anything else. Work through the steps in order.

## 0. Read your inputs
From the repo, read:
- `state.json` — memory: `week_index`, `regions`, and `used_cases` (every case already
  written, with `id`, `region`, `scale`, `recency`, `dimension`). Never reuse or
  near-duplicate these.
- `STYLE.md` — voice, structure, and the two reference cases. Follow it exactly when
  writing.
- `RUBRIC.md` — the two-stage selection rubric (fit-test gate + fertility ranking).
- `SCHEMA.md` — the case schema you must fill before drafting any case.

## 1. Survey the corpus (agenda-setting)
Before searching for new cases, tally what `used_cases` already covers: counts by
`region`, `scale`, `recency`, and `dimension` (the four missing-column types in
`RUBRIC.md`: history/motive, identity, institutions/power, values). Note which
dimensions and regions are thin. You will bias toward filling those gaps — the
project's value comes from breadth of failure modes, not from re-covering the same one.

## 2. Generate a wide candidate pool (conjecture)
Brainstorm **5–8** real, well-documented episodes that plausibly fit the `STYLE.md`
frame. Search broadly — do **not** lock a single region first. Span several regions,
eras, and scales, and lean toward the gaps you found in step 1. Exclude anything that
matches or resembles an existing entry in `used_cases`, comparing on the actual
structure (actor, trusted model, missing column), not just the id slug.

## 3. Refute (fit-test gate)
Run every candidate through the Stage-1 fit-test in `RUBRIC.md`. A candidate must pass
**all six** criteria. Be adversarial — actively try to disqualify each one:
- Was the analysis genuinely sound, or was the actor just *wrong*? (If wrong, discard:
  that's an engineering failure, not engineering diplomacy.)
- Is the failure value/political/historical rather than technical?
- Is there a *specific* pragmatist counterfactual, not just "be wiser"?
- Is it real and documented well enough to verify?
Discard every candidate that fails. Do not soften a near-miss into a pass.

## 4. Formalize (schema gate)
For each surviving candidate, fill the `SCHEMA.md` template completely. This is also a
disqualifier: if you cannot crisply name the actor's trusted model, the missing column,
the concrete counterfactual, or the honest flag, the case is not a real fit — drop it.
Filling the schema before writing forces every inference explicit and exposes weak fits.

## 5. Rank and select (fertility)
Score each remaining candidate on the Stage-2 fertility rubric in `RUBRIC.md` (1–5 per
criterion, weighted). Then:
- The **top two** by score are this week's cases to write.
- Apply coverage preferences only as a tiebreaker: among candidates within ~1 weighted
  point of each other, prefer the one that improves balance across `region`, `scale`,
  `recency`, and `dimension`. Recency should trend toward roughly 2:1 recent:historical
  across the trailing weeks — nudge toward it, but never write a weaker case just to hit
  the ratio.
- Keep the **next 2–3** as runner-ups to surface in the report.

## 6. Verify (verification gate)
For each of the two selected cases, use web search to confirm every load-bearing fact
and gather 3–6 real sources. Record a verification status per source. **Do not invent
facts, quotes, or sources.** If a claim a case depends on cannot be verified, fix the
case or swap in a runner-up — never publish an unverifiable load-bearing claim.

## 7. Write
Write each selected case following `STYLE.md` exactly — the voice, the structure, the
closing parenthetical flag, ~700–1000 words, and a References section. Begin each with
YAML front-matter carrying the schema fields:
```
---
case_id: kebab-case-person-event
region: <region>
scale: <individual|community|international>
recency: <recent|historical>
year: <year of the key decision>
dimension: <history-motive|identity|institutions-power|values>
actor: <one line>
trusted_model: <one line>
missing_column: <one line>
counterfactual: <one line>
flag: <one line>
sources_verified: true
---
```

## 8. Publish
Assemble both cases into one reader-facing file: a top heading
`# Engineering Diplomacy — <region(s)> (<today's date>)`, then the two case studies with
their YAML front-matter removed. Commit it to `published/<date>.md`. (Cases may now come
from different regions, so the file is named by date; name the region(s) in the heading.)
This is the file to copy into a Word doc, or read via GitHub Pages if enabled.

## 9. Archive
Also commit each case as a separate markdown file (keep the front-matter) into
`case_studies/`, named `<date>_<case_id>.md`.

## 10. Patterns digest (periodic)
If `used_cases` has **8 or more** entries and `week_index % 4 == 0`, read the `flag` and
`dimension` fields across all files in `case_studies/` and write a short digest to
`patterns/<date>-patterns.md`: which framework blind spots recur, which missing-column
dimensions dominate, and any cross-case regularities worth noting. This is the one
output that accumulates across runs — treat it as book material.

## 11. Update memory
Increment `week_index` by 1. Append an entry to `used_cases` for each new case —
`{id, region, scale, recency, dimension}`. Commit the updated `state.json` back to the
repo.

## 12. Report
For each written case, state: title, scale, recency, and dimension. Then list the
runner-up candidates as one-line pitches (title + why it's strong) so a swap is easy.
Finally, give the path (and Pages URL if set up) of the new `published/` file, and note
whether a patterns digest was written this week.
