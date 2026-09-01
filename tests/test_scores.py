from src.scores import summarize_scores


def test_normal_scores():
    result = summarize_scores([40, 65, 95])

    assert result["total_count"] == 3
    assert result["total_score"] == 200
    assert result["passing_count"] == 2
    assert result["failing_count"] == 1
    assert result["average_score"] == 200 / 3
