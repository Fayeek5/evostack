def calculate_health_score(
    complexity_analysis,
    dependency_analysis,
    analysis_results
):
    avg_complexity = complexity_analysis.get(
        "average_complexity",
        0
    )

    high_risk_count = complexity_analysis.get(
        "high_risk_count",
        0
    )

    connected_modules = dependency_analysis.get(
        "most_connected_modules",
        []
    )

    issues = analysis_results.get("issues", [])

    complexity_score = max(
        0,
        100 - int(avg_complexity * 8) - int(high_risk_count * 0.3)
    )

    dependency_score = max(
        0,
        100 - len(connected_modules)
    )

    technical_debt_score = max(
        0,
        100 - len(issues) * 3
    )

    overall = int(
        (
            complexity_score * 0.4
            + dependency_score * 0.3
            + technical_debt_score * 0.3
        )
    )

    if overall >= 85:
        rating = "A"

    elif overall >= 70:
        rating = "B"

    elif overall >= 50:
        rating = "C"

    else:
        rating = "D"

    return {
        "overall": overall,
        "complexity_score": complexity_score,
        "dependency_score": dependency_score,
        "technical_debt_score": technical_debt_score,
        "maintainability_rating": rating
    }
