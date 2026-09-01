def summarize_scores(scores):
    total_count = len(scores)
    total_score = sum(scores)
    passing_count = sum(1 for score in scores if score >= 50)
    failing_count = total_count - passing_count
    average_score = total_score / total_count

    return {
        "total_count": total_count,
        "total_score": total_score,
        "passing_count": passing_count,
        "failing_count": failing_count,
        "average_score": average_score,
    }
