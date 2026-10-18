# AITR Lab 02 — Reproducible Research Project

> **Status: scaffold and protocol only.** No experimental results are claimed until the proposed experiments have actually been run and checked.

## Research question

Does a taxonomy-guided, evidence-aware evaluation pipeline identify and categorize factual hallucinations in LLM responses more transparently than a response-level binary detector?

The taxonomy labels must be mapped to the source paper before annotation begins. This is a proposed question, not an established finding.

## Subquestions

1. How does claim-level classification perform across supported, contradicted, and insufficient-evidence cases?
2. Does evidence retrieval improve detection compared with a no-retrieval baseline?
3. Which error categories show the most frequent confusions?
4. How often does the supplied evidence actually support an automated decision?

## Hypotheses to test

- **H1:** Claim-level and category-level reporting will reveal error patterns hidden by a single aggregate score.
- **H2:** Retrieval may improve evidence coverage, but irrelevant passages may introduce false positives.
- **H3:** Evaluation quality will vary by error category and evidence availability.

These hypotheses are untested until the protocol is executed.

## Proposed workflow

1. Define operational labels from the source taxonomy and document overlaps and edge cases.
2. Select a dataset with compatible access terms; record provenance and licensing in `data/README.md`.
3. Freeze split identifiers and random seeds in `configs/`; avoid source-document leakage where possible.
4. Compare a transparent no-retrieval baseline with a documented evidence-aware verifier.
5. Report per-class precision, recall, F1, macro-F1, confusion matrix, sample counts, and uncertainty intervals where feasible.
6. Audit false positives, false negatives, and evidence quality with human review.
7. Save config, package/model versions, commands, logs, and genuine metric outputs under `results/`.
8. Record every deviation and write up only measured results.

## Directory map

- `requirements.txt` — pinned scaffold dependencies; end-to-end stack not yet validated.
- `configs/` — experiment settings and seed templates.
- `data/README.md` — data access and schema; no restricted raw data.
- `notebooks/` — exploration and runnable notebooks (must be rerun cleanly before calling verified).
- `src/` — reusable utilities and metrics.
- `scripts/` — training, inference, and evaluation entrypoints.
- `results/` — genuine run metrics, logs, and figures only.
- `paper/` — LaTeX source, bibliography, and final figures.
- `research_decisions.md` — links literature decisions to experiments.
- `baseline_validation.md` — reproduction checklist and deviations.
- `ai_assistance_log.md` — significant AI use and human verification.

## Setup

Recommended: Python 3.11.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pytest
```

Windows PowerShell activation: `.venv\Scripts\Activate.ps1`.

## Reproducibility requirements

For each run record the Git commit, date, Python/package versions, dataset/version/split, model identifier/version, prompts, decoding/retrieval parameters, random seeds, command, exit status, logs, and output paths. Never commit credentials, private data, or restricted datasets. Do not fabricate scores, result files, logs, plots, or claims of reproduction. Keep planned hypotheses separate from findings and preserve failed runs/deviations.

## Current status

- [x] Research protocol and scaffold drafted
- [x] Initial metric helper and unit tests added
- [ ] Confirm taxonomy mapping against the source paper
- [ ] Select and document dataset and license
- [ ] Implement/validate claim segmentation and evidence retrieval
- [ ] Run and verify baseline experiments
- [ ] Generate genuine metric files, logs, figures
- [ ] Complete human evidence audit
- [ ] Finalize paper after experiments

No research baseline has yet been reproduced and no experiment metrics are available in this scaffold. Cite the source taxonomy paper, datasets, models, and libraries before submission.
