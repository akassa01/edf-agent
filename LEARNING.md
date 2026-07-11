# LEARNING.md — how the rubric evolves

## The design constraint

The obvious version of "have the agent score itself and adjust the rubric" fails in an
obvious way: the agent grades its own homework, and the rubric drifts toward whatever the
agent is already good at. Every criterion it does well on gets weighted up; every criterion
it struggles with gets quietly softened. After ten weeks you have a rubric that certifies
the agent's current behavior as excellent.

The fix is a single rule:

> **The rubric never learns from the agent's scores. It learns from the *gap* between the
> agent's score and the humans' scores.**

The agent's self-score is not a judgment. It is a *prediction* of what the humans will say.
A criterion where the agent reliably predicts the human score is working. A criterion where
it reliably doesn't is **badly defined**, and that — not the agent's dissatisfaction with
its own marks — is what licenses an edit.

This also keeps the system honest about what the Nature paper says AI cannot yet do. Its
closing line is that the decisive creative leaps are still made by humans and the real
promise lies in partnership. AlphaEvolve's propose–test–refine loop works because its
evaluator is *objective*. Ours is not. So the humans are the evaluator, and the agent's job
is to converge on them.

---

## Ground truth

**Two scorers: Arman and Prof. Islam.** Both are ground truth.

- Where they agree (within 1 point), that is the human score.
- Where **they disagree by ≥ 2 points**, the datapoint is **discarded, not averaged.**
  Sustained disagreement between the two humans means the *criterion itself is contested or
  ambiguous* — which is a finding, not training data. Log it in
  `rubric/CONTESTED.md` and surface it in the weekly report. Two experts who cannot agree
  on what a 4 means have found a hole in the rubric's language, and that hole should be
  fixed by them, not inferred by the agent.
- Where only one has scored, use that score, flagged as single-source.

Cadence: Arman scores weekly. Prof. Islam scores whenever he reviews — likely monthly, in
batch. The agent tolerates gaps and never blocks on missing feedback.

---

## The loop

1. **Predict.** Agent self-scores each case against `QUALITY_RUBRIC.md`, with an evidence
   anchor per criterion. → `evals/<date>-selfscore.md`
2. **Correct.** Humans override the numbers they disagree with and add a freeform note.
   → `feedback/<date>.md`
3. **Calibrate.** Agent appends `(case_id, criterion, self, human_arman, human_si)` rows to
   `calibration.json` and recomputes per-criterion mean signed gap and sample count.
4. **Amend — at most one change per week, and only on a trigger.**

---

## The four triggers (and what each licenses)

| Trigger | Condition | The correct fix |
|---|---|---|
| **Systematic divergence** | \|mean signed gap\| ≥ 1.0 on a criterion, n ≥ 3 | **Rewrite the 1/3/5 anchors**, using the human scores as ground truth. Not the weight — the *language*. The agent and the humans mean different things by that criterion. This is the highest-value edit and should be the most common. |
| **Uncaptured feedback** | The same freeform complaint appears in ≥ 2 feedback files and no existing criterion covers it | **Propose a new criterion**, with a name, 1/3/5 anchors, and a weight. Quote both instances of the complaint. |
| **Weight miscalibration** | Human totals rank cases in a consistently different order than the weighted rubric does, n ≥ 3 | **Propose a weight change.** Only after ruling out anchor divergence — bad anchors look like bad weights. |
| **Dead criterion** | A criterion scores 4–5 on every case for ≥ 5 weeks | It isn't discriminating. **Sharpen the anchors, or propose retirement.** |

If none of these fire: **change nothing**, and say so in the report. Weeks with no
amendment are the normal case, not a failure.

---

## Guardrails

- **The Stage-1 fit-test gate in `RUBRIC.md` is frozen.** The agent may never amend it.
- **Minimum sample.** No amendment on fewer than 3 scored cases. Two cases a week means the
  data is thin; act accordingly.
- **One change per week, maximum.** And never the same criterion two weeks running.
- **Back-test required.** Every proposed amendment must be tested against 3 past cases:
  re-score them under the old and new rubric. If no verdict, ranking, or score moves by
  more than a point, the change is **cosmetic — reject it.** A rubric change that would not
  have changed any past judgment is not a change.
- **No self-deletion.** The agent may not remove or down-weight below 1 any criterion that
  human feedback has ever explicitly invoked.
- **No lowering the bar.** Amendments may not remove a hard-fail condition.
- **Log everything.** Every amendment gets a `rubric/CHANGELOG.md` entry:

```
## v2 — 2026-07-24
Changed: criterion 5 (18th camel), anchors rewritten.
Trigger: systematic divergence, mean gap +1.3 over n=4 (agent scores itself high).
Quoted feedback: "this isn't an 18th camel, it's just picking the cheaper option" (SI, 2026-07-17)
Back-test: re-scored inderlok-dmrc (5→3), hawaii-false-alert (4→4), mcnamara-vietnam (5→5).
Verdict: ranking moves. Change is substantive. Applied.
```

- **Version stamp.** Bump `rubric_version` and stamp it into every case's front-matter, so
  you can always ask which rubric a case was written under.

---

## The by-product

`calibration.json` accumulates a record of exactly where an AI system's judgment diverges
from an expert's on a values-laden rubric, and how that gap closes (or doesn't) over time.
That is not plumbing. That is a finding, and probably a chapter.

---

## Feedback file template (`feedback/<date>.md`)

```
# Feedback — <date>
Scorer: Arman | Shafiqul Islam
Cases reviewed: <case_id>, <case_id>

## Score overrides
Paste the self-score table with your numbers in the Human column.
Blank = you agree with the agent.

## What the rubric failed to capture
Anything you reacted to that no criterion asks about. Be blunt; repeated complaints
here are what create new criteria.

## Verdict
Publish as-is | Publish with edits | Swap in a runner-up | Reject
```
