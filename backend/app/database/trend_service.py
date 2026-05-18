from app.database.history_service import (
    get_repository_history
)


def calculate_repository_trends(
    repo_url: str
):

    history = get_repository_history(
        repo_url
    )

    if len(history) < 2:

        return {
            "status": "insufficient_history"
        }

    latest = history[0]
    previous = history[1]

    score_change = (
        latest["overall_score"]
        - previous["overall_score"]
    )

    if score_change > 0:

        trend = "improving"

    elif score_change < 0:

        trend = "degrading"

    else:

        trend = "stable"

    return {

        "repository": repo_url,

        "latest_score": latest["overall_score"],

        "previous_score": previous["overall_score"],

        "score_change": round(
            score_change,
            2
        ),

        "trend": trend,

        "analysis_count": len(history)
    }
