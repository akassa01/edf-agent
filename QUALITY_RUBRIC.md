# QUALITY_RUBRIC.md — v1

**rubric_version: 1**

`RUBRIC.md` decides *which* case gets written. This decides *how good the written case is*.
It is the rubric the agent scores itself against, and the one that evolves — see
`LEARNING.md` for the amendment protocol.

Every score requires an **evidence anchor**: the exact sentence from the case that earns or
loses the point. A score without an anchor is void. This is the whole mechanism — it makes
the self-score auditable in seconds and makes disagreement precise rather than vibes-based.

---

## Criteria

Score each 1–5. Weighted total out of 110.

| # | Criterion | Weight | 1 | 3 | 5 |
|---|---|---|---|---|---|
| 1 | **Tri-perspective integrity** | 3 | One perspective; the other two are absent or named in passing | All three appear, but one is a token paragraph | All three genuinely see something the others miss; the reader understands why each is insufficient alone |
| 2 | **Diagnosis of the problem space** | 3 | Facts and values blurred together | Scientific and social facts distinguished; political realities thin | Scientific facts, social facts, and political realities each named; uncertainty distinguished from ambiguity |
| 3 | **Decision pathway** | 3 | "They should have been wiser" | A direction, but not a move anyone could execute | One clear move (Implement/Redesign/Expand/Reframe), with who acts, for whom, through what process |
| 4 | **Where is X** | 2 | No intervention point named | A general period or phase | A precise fulcrum — a moment, clause, or room — with the leverage argued |
| 5 | **The 18th camel** | 2 | A compromise between the two stated options | A third option, asserted but not defended | A genuine third thing, with why it beats both, or a defended argument that none existed |
| 6 | **Tools** | 2 | Listed, generic | Named and purposed | Each tool explains how it changes interaction, learning, or coordination |
| 7 | **Metrics** | 2 | Absent or unmeasurable | Measurable but detached from the pathway | Measurable, trackable, method stated, visibly linked to the pathway |
| 8 | **Stress-test honesty** | 2 | Stress test is a formality; problem definition unchanged | Some real risks surfaced | The five questions land hard and the problem definition genuinely moves |
| 9 | **Honest flag** | 1 | Absent, or a re-run of ego / organizational power | A real limitation, but familiar | A fresh limitation of principled pragmatism, sharply stated |
| 10 | **Prose** | 2 | Report-ish; no cold open; over or under length | Readable; cold open present but soft | Specific person, specific moment, date and place; narrative, precise, unsentimental; 700–1000 words |
| 11 | **Sourcing** | 2 | Any unverifiable or invented claim | Sources present, some load-bearing claims thin | 3–6 verified sources; every load-bearing claim traceable (or `composite`, correctly labeled with no sources claimed) |

**Hard fail, regardless of total:** an invented source or fabricated quote; a `documented`
case with unverifiable load-bearing claims; a missing perspective in criterion 1.

---

## Scoring output

The agent writes `evals/<date>-selfscore.md` in this shape, one block per case:

```
## <case_id> — self-score (rubric v1)

| # | Criterion | Self | Anchor | Human (Arman) | Human (SI) |
|---|---|---|---|---|---|
| 1 | Tri-perspective integrity | 4 | "The engineer's instinct is pragmatic: rather than treating the flaw as a catastrophe, treat it as a boundary condition." |  |  |
| ... |

Self total: __ / 110
```

The two rightmost columns are left blank for the humans to fill. That is the feedback form —
overriding a number takes seconds, and blank means agreement.
