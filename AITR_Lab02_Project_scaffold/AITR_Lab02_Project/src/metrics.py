"""Evaluation helpers for multi-class hallucination/evidence labels."""
from __future__ import annotations
from typing import Any, Sequence
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, f1_score

DEFAULT_LABELS = ("supported", "contradicted", "insufficient_evidence")


def evaluate_predictions(y_true: Sequence[str], y_pred: Sequence[str], labels: Sequence[str] = DEFAULT_LABELS) -> dict[str, Any]:
    """Return structured metrics for completed predictions; this does not run a model."""
    if len(y_true) == 0:
        raise ValueError("y_true and y_pred must be non-empty")
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have the same length")
    label_list = list(labels)
    return {
        "n_examples": int(len(y_true)),
        "labels": label_list,
        "macro_f1": float(f1_score(y_true, y_pred, labels=label_list, average="macro", zero_division=0)),
        "confusion_matrix": confusion_matrix(y_true, y_pred, labels=label_list).tolist(),
        "classification_report": classification_report(y_true, y_pred, labels=label_list, output_dict=True, zero_division=0),
    }


def metrics_to_jsonable(metrics: dict[str, Any]) -> dict[str, Any]:
    """Convert common NumPy values into JSON-compatible Python values."""
    def convert(value: Any) -> Any:
        if isinstance(value, dict):
            return {str(k): convert(v) for k, v in value.items()}
        if isinstance(value, (list, tuple)):
            return [convert(v) for v in value]
        if isinstance(value, np.ndarray):
            return value.tolist()
        if isinstance(value, np.generic):
            return value.item()
        return value
    return convert(metrics)
