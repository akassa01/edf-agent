#!/usr/bin/env python3
"""Compute the Engineering Diplomacy corpus survey from the repo itself.

This is the source of truth for step 1 (SURVEY) of the routine. It replaces the
hand-maintained `used_cases` array and `week_index` counter that used to live in
state.json — those churned on every run and caused merge conflicts when weekday
runs branched from a stale main and each rewrote the whole file (see the note in
ROUTINE_PROMPT.md step 12/14).

Corpus = the immutable `seed_cases` in state.json PLUS the front-matter of every
generated case in case_studies/*.md. week_index = number of published/*.md files
(each run writes exactly one). Nothing here is stored; it is recomputed each run,
so there is no shared mutable field to conflict on.

Usage:  python3 survey.py            # human-readable report
        python3 survey.py --json     # machine-readable, for the routine to read
"""
import json
import sys
import glob
import os
from collections import Counter

REPO = os.path.dirname(os.path.abspath(__file__))
SCALES = ["individual", "community", "international"]
FIELDS = ["id", "scale", "region", "recency", "archetype_dominant",
          "crowded_out_mode", "case_type", "mode", "flag"]


def _read_front_matter(path):
    """Return the YAML front-matter dict from a markdown file (between the first
    two --- fences), or None if the file has no front-matter block."""
    import yaml
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    if not text.startswith("---"):
        return None
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None
    return yaml.safe_load(parts[1]) or None


def load_corpus():
    """Full corpus = immutable seeds + generated case_studies front-matter."""
    state = json.load(open(os.path.join(REPO, "state.json"), encoding="utf-8"))
    corpus = []
    for seed in state.get("seed_cases", []):
        corpus.append({k: seed.get(k) for k in FIELDS} | {"_source": "seed"})
    for path in sorted(glob.glob(os.path.join(REPO, "case_studies", "*.md"))):
        fm = _read_front_matter(path)
        if not fm:
            continue
        row = {k: fm.get("case_id" if k == "id" else k) for k in FIELDS}
        row["_source"] = os.path.basename(path)
        corpus.append(row)
    return state, corpus


def week_index():
    """Number of completed runs = number of published/<date>.md files."""
    return len(glob.glob(os.path.join(REPO, "published", "*.md")))


def next_quota(corpus):
    """Least-covered scale; tie broken by least-covered archetype overall."""
    by_scale = Counter(c["scale"] for c in corpus)
    fewest = min(by_scale.get(s, 0) for s in SCALES)
    contenders = [s for s in SCALES if by_scale.get(s, 0) == fewest]
    by_arch = Counter(c["archetype_dominant"] for c in corpus)
    # among cases at the contending scale(s), which archetype is least covered
    # globally — that is the tiebreak the routine documents.
    arch = min(("scientist", "humanist", "engineer"),
               key=lambda a: by_arch.get(a, 0))
    return {"scale": sorted(contenders)[0], "archetype": arch,
            "scale_counts": dict(by_scale), "archetype_counts": dict(by_arch)}


def build():
    state, corpus = load_corpus()
    wi = week_index()
    q = next_quota(corpus)
    return {
        "week_index": wi,
        "n_cases": len(corpus),
        "next_run_is_prospective": wi % 4 == 0,
        "patterns_digest_due": len(corpus) >= 8 and wi % 4 == 0,
        "quota_next": q,
        "tallies": {f: dict(Counter(c[f] for c in corpus))
                    for f in ["scale", "archetype_dominant", "region",
                              "recency", "crowded_out_mode", "case_type", "mode"]},
        "corpus": corpus,
    }


def main():
    data = build()
    if "--json" in sys.argv:
        print(json.dumps(data, indent=2, ensure_ascii=False))
        return
    print(f"week_index (completed runs) : {data['week_index']}")
    print(f"corpus size                 : {data['n_cases']} cases")
    print(f"next run prospective?       : {data['next_run_is_prospective']} "
          f"(week_index % 4 == 0)")
    print(f"patterns digest due?        : {data['patterns_digest_due']}")
    q = data["quota_next"]
    print(f"next quota slot             : {q['scale']} / {q['archetype']} archetype")
    print(f"  scale counts     : {q['scale_counts']}")
    print(f"  archetype counts : {q['archetype_counts']}")
    print("\ntallies:")
    for field, counts in data["tallies"].items():
        print(f"  {field:18}: {counts}")


if __name__ == "__main__":
    main()
