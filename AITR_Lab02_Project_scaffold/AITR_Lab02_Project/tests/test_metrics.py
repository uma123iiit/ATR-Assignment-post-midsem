import pytest
from src.metrics import evaluate_predictions, metrics_to_jsonable


def test_perfect_predictions_have_macro_f1_one():
    labels = ["supported", "contradicted", "insufficient_evidence"]
    result = evaluate_predictions(labels, labels)
    assert result["n_examples"] == 3
    assert result["macro_f1"] == pytest.approx(1.0)
    assert result["confusion_matrix"] == [[1, 0, 0], [0, 1, 0], [0, 0, 1]]


def test_length_mismatch_raises():
    with pytest.raises(ValueError, match="same length"):
        evaluate_predictions(["supported"], ["contradicted", "supported"])


def test_empty_input_raises():
    with pytest.raises(ValueError, match="non-empty"):
        evaluate_predictions([], [])


def test_unknown_label_not_added_to_fixed_matrix():
    result = evaluate_predictions(["supported"], ["unknown"])
    assert result["confusion_matrix"] == [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def test_metrics_jsonable_conversion():
    assert metrics_to_jsonable({"value": 1.0, "matrix": [[1, 0]]}) == {"value": 1.0, "matrix": [[1, 0]]}
