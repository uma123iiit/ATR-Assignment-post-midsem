# Data access and description

**No raw dataset is included in this repository.** This directory documents the intended data contract only; replace placeholders once a dataset is selected and access has been confirmed.

Before using a dataset, document:
- **Name and citation:** to be selected and verified.
- **Version / release / access date:** to be recorded.
- **Access URL or instructions:** to be recorded.
- **License and research-use restrictions:** verify from the authoritative dataset source.
- **Expected fields:** example ID, prompt/question, response, atomic claim or claim span, evidence passage/source, label, annotator/adjudication notes.
- **Preprocessing:** exact filters, deduplication, normalization, and exclusion counts.
- **Split strategy:** explain grouping to avoid leakage and commit a split manifest only if permitted.
- **Sensitive/restricted material:** keep outside Git unless sharing is explicitly authorized.

## Suggested normalized schema

| Field | Description |
|---|---|
| `example_id` | Stable, non-sensitive ID |
| `question` | Input prompt or query, subject to dataset license |
| `response` | Model response to be evaluated |
| `claim_id` | Stable claim identifier within an example |
| `claim_text` | Atomic factual claim |
| `evidence_text` | Permitted support/contradiction evidence, or empty if unavailable |
| `label` | Relation/category under the final documented label set |
| `split` | Train, validation, or test |
| `annotator_status` | Unreviewed, reviewed, or adjudicated |

This schema is a proposal, not the final dataset definition. Distinguish human gold labels from model predictions. Do not commit restricted raw data, private data, tokens, or copyrighted corpora unless redistribution is explicitly permitted.
