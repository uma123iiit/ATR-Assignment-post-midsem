# Research decisions: literature to experiment

**Status:** Initial plan. Populate citations and decisions only after reading and verifying source papers and dataset/model documentation.

| ID | Source / literature finding | Research implication | Planned experiment | Status |
|---|---|---|---|---|
| D1 | Taxonomy source paper and category definitions to be verified | Labels need operational definitions and examples | Create taxonomy-to-label map and adjudication guide | Pending source review |
| D2 | Hallucination detection/factuality literature to be selected and verified | Response-level scores may hide claim-level errors | Compare response- and claim-level reporting if data supports both | Proposed |
| D3 | Retrieval-based verification literature to be selected and verified | Retrieved passages may support checking but can be irrelevant | Compare no-retrieval and retrieval-assisted methods on a fixed split | Proposed |
| D4 | Evaluation methodology sources to be selected and verified | Class imbalance can make accuracy misleading | Report per-class precision/recall/F1, macro-F1, confusion matrix and counts | Proposed |

For each decision, record a full citation/DOI or stable URL, the exact supported claim, review date, limitations, design consequence, and resulting config/code change. Do not infer paper findings from titles alone.
