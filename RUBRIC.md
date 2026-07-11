# RUBRIC.md — Case Selection (v2)

**Purpose.** Decide *which* episodes the routine writes up. Two stages: a frozen binary
gate, then a weighted ranking.

This is the artifact the Nature paper (Burtsev et al. 2026) calls for when it proposes AI
systems that *sort and prioritize potential problems using criteria selected by
researchers*. The criteria are Prof. Islam's and Arman's. The agent applies them; it does
not own them.

---

## What changed in v2, and why

v1 was reverse-engineered from McNamara and Challenger, and its gate encoded a single
thesis: *a competent technical actor failed because they treated a human problem as
technical.* That thesis is a **scientist-archetype filter**. Tested against the four newer
seed cases, the v1 gate rejects three of them — Emma/Daniel and Raj have no "trusted
model" and no "sound analysis" to speak of, and Hawaii has no individual actor at a
decisive moment. The archetype monoculture was not a content gap. It was the gate.

v2 replaces "the actor trusted a model that lacked a column" with the more general
Engineering Diplomacy claim: **one mode was over-weighted and crowded out the others.**
Thinking (Scientist), feeling (Humanist), doing (Engineer). All six seed cases pass.

---

## Stage 1 — Fit-test (all seven must pass; FROZEN)

The agent may not amend this section. Only Prof. Islam changes it.

1. **Real, and verifiable or honestly labeled.** Either a documented episode with 3–6
   verifiable sources (`case_type: documented`), or an explicitly labeled illustrative
   teaching composite (`case_type: composite`, permitted at `individual` scale only, no
   invented sources). Never a documented case with fabricated sourcing.

2. **A genuine decision under uncertainty, with contested facts *and* contested values.**
   Not a puzzle with a right answer that someone simply got wrong. If better data alone
   would have resolved it, it is an engineering problem, not an engineering diplomacy one.

3. **One mode was over-weighted, crowding out the others.** There is an identifiable
   dominant mode — thinking, feeling, or doing — that the actor or system leaned on to the
   exclusion of the rest. *(McNamara: thinking crowds out motive and history. Emma: feeling
   and a binary framing crowd out actionability. Hawaii: doing — speed — crowds out
   recovery. Inderlok: doing-now crowds out long-horizon thinking. Raj: feeling crowds out
   the very pragmatism he offered Farhan.)*

4. **The crowded-out mode was causally decisive.** If including it would not have changed
   the outcome, the fit is weak. Discard.

5. **X is locatable.** You can name a specific intervention point — a moment, a decision,
   a room, a clause — not "they should have been wiser." *(Hawaii: the 38 minutes between
   knowing and correcting. Inderlok: the terminal-platform geometry, a single station that
   gates an entire corridor.)*

6. **An 18th camel exists — or its absence is the lesson.** Either a real option outside
   the apparent binary, or a defensible argument that none was available and the trade-off
   was genuine. A compromise between the two stated options is *not* an 18th camel.

7. **An honest flag exists.** Something the episode reveals that principled pragmatism
   itself does not resolve *(ego; raw organizational power)*. A case with no flag is
   suspiciously tidy. Look harder before you accept it.

---

## Stage 2 — Fertility ranking (score survivors 1–5, weighted)

| Criterion | Weight | What a 5 looks like |
|---|---|---|
| **Generalizability** | 3 | The blind spot abstracts into a transferable principle, not a one-off. |
| **Corpus gap fill** | 3 | Fills the thinnest cell of the scale × archetype matrix. Penalizes a fourth scientist-overruled-by-management story. |
| **Novelty / non-canonical** | 2 | Not the case everyone already cites. The seeds are canonical *as templates*; new output should beat them here. |
| **Pathway concreteness** | 2 | The decision pathway and tools are specific and executable — one clear move (Implement / Redesign / Expand / Reframe), with tools that visibly change interaction, learning, or coordination. |
| **Cold-open vividness** | 2 | A specific person at a specific decisive moment, with date and place. |
| **Flag freshness** | 1 | Surfaces a *new* limitation of the framework, not a re-run of ego/power. These accumulate into the patterns digest. |
| **Documentation depth** | 1 | Rich enough record that the writeup is defensible and reads well. |

**Score** = Σ (score × weight). Ties broken toward corpus gap fill, then novelty.

The agent **may** propose amendments to these weights and to the criteria descriptors, via
the protocol in `LEARNING.md`. It may not touch Stage 1.

---

## Validation against the seed corpus

| Case | Archetype | Over-weighted mode | Crowded out | Scale | Type |
|---|---|---|---|---|---|
| McNamara / Vietnam | Scientist | thinking | motive, history | international | documented |
| Challenger / O-ring | Scientist–Engineer | thinking (evidentiary mode) | institutions, standing | individual | documented |
| Emma & Daniel | Humanist | feeling + binary framing | actionability under limited authority | individual | composite |
| Hawaii false alert | Engineer | doing (speed) | recovery; the felt experience of fear | community | documented |
| Raj (Solomon Paradox) | Humanist | feeling (no self-distance) | the pragmatism he gave Farhan | individual | composite |
| Inderlok / DMRC | Engineer | doing (optimize the present) | long-horizon thinking; shared question | community | documented |

All six clear Stage 1. Archetypes balance 2 / 2 / 2.

**Scale does not:** individual 3, community 2, international 1. The quota slot is therefore
bound to `international` on the next run.

---

## Open questions for Prof. Islam

1. **Composite cases.** Two of the six seeds (Emma/Daniel, Raj) are illustrative, not
   documented. v2 permits them, at individual scale, if labeled. Is that right — or should
   the agent's own output be documented-only, with composites reserved for human authors?
2. **Weights.** Generalizability and corpus balance currently outrank novelty, pathway
   concreteness, and vividness. Right ordering for the book?
3. **Prospective cases.** Every 4th week the agent will attempt a live anchor problem in
   the workshop's forward format (Ganges as the model). Keep, expand, or cut?
4. **Scale.** Coverage is now enforced as a hard quota rather than a preference. Is even
   coverage the goal, or should international dominate given the book's subject?
