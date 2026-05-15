def generate_recommendations(
    complexity_analysis,
    dependency_analysis,
    health_score
):
    recommendations = []

    high_risk_files = complexity_analysis.get(
        "top_risky_files",
        []
    )

    if high_risk_files:
        top_file = high_risk_files[0]

        recommendations.append(
            f"{top_file['file']} has very high complexity and should be modularized."
        )

    dependency_hotspots = dependency_analysis.get(
        "most_connected_modules",
        []
    )

    if dependency_hotspots:
        hotspot = dependency_hotspots[0]

        recommendations.append(
            f"{hotspot['file']} is heavily coupled with other modules."
        )

    overall = health_score.get("overall", 0)

    if overall >= 80:
        recommendations.append(
            "Repository architecture appears healthy overall."
        )

    elif overall >= 60:
        recommendations.append(
            "Repository has moderate maintainability risks."
        )

    else:
        recommendations.append(
            "Repository shows significant architectural risk."
        )

    debt_score = health_score.get(
        "technical_debt_score",
        0
    )

    if debt_score < 70:
        recommendations.append(
            "Technical debt indicators suggest cleanup is needed."
        )

    return recommendations
