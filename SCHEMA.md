# SCHEMA.md — Engineering Diplomacy case schema

Fill this completely for every candidate that passes the Stage-1 fit-test in
`RUBRIC.md`, **before** writing any prose. If a required field can't be filled crisply
and truthfully, the case isn't a real fit — drop it. This is the *formalization gate*:
making every inference explicit exposes weak cases (the same way running an argument
through a proof assistant exposes a gap), and the structured fields enable real dedup
(on structure, not just the id slug) and the cross-case patterns digest.

## Required fields

- **case_id** — `kebab-case-person-event` (e.g. `mcnamara-vietnam-body-count`).
- **actor** — who they were and what kind of "scientist/engineer" archetype they are.
- **trusted_model** — the specific metric, model, or mode they relied on that was
  internally valid. (*body count as a proxy for winning; the engineer-to-engineer
  evidentiary mode.*)
- **missing_column** — the human/political/historical/value dimension the model had no
  place for, stated as the thing the spreadsheet had no column for. (*what the
  Vietnamese were fighting for; who in the room had standing to halt the launch.*)
- **dimension** — classify the missing column as exactly one of: `history-motive`,
  `identity`, `institutions-power`, `values`. (Drives corpus balance.)
- **why_decisive** — one or two sentences on how the missing column actually changed
  the outcome. If it didn't change the outcome, the fit is weak.
- **failure_type** — the epistemological/relational nature of the failure: optimizing
  within the wrong model, precision mistaken for accuracy, right data in the wrong
  language for the room. (Not "they got the math wrong.")
- **counterfactual** — the concrete, specific move a principled pragmatist could have
  made instead. Must be actionable, not "be wiser." (*ask how the other side defines
  winning and bring in regional historians; reframe the O-ring risk as institutional
  liability and find who had the standing to stop the launch.*)
- **flag** — the honest limitation the episode reveals that principled pragmatism
  itself does not resolve (*ego; raw organizational power structure*). Prefer a *fresh*
  flag over re-surfacing ones already common in `used_cases`.
- **sources** — 3–6 real, verifiable sources, each with a verification status recorded
  after the verify step.

## Metadata (carried into the case front-matter)

- **region** — the case's region.
- **scale** — `individual` | `community` | `international`.
- **recency** — `recent` (key decision 2010 or later) | `historical` (older landmark).
- **year** — year of the key decision.

## Drop criteria (the gate)

Drop the candidate if you cannot fill, crisply and truthfully, any of:
`trusted_model`, `missing_column`, `counterfactual`, or `flag`. A tidy story with no
honest flag, or a vague "they should have known better" counterfactual, is a sign the
episode doesn't actually instantiate the pattern.
