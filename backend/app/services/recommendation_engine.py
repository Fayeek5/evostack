def generate_recommendations(
    complexity_analysis,
    dependency_analysis,
    health_score,
    semantic_analysis=None
):
    recommendations = []

    overall = health_score.get("overall", 0)

    complexity = health_score.get(
        "complexity_score",
        0
    )

    dependency = health_score.get(
        "dependency_score",
        0
    )

    debt = health_score.get(
        "technical_debt_score",
        0
    )

    functions = 0
    react_components = 0

    if semantic_analysis:

        functions = semantic_analysis.get(
            "functions",
            0
        )

        react_components = semantic_analysis.get(
            "react_components",
            0
        )

    high_risk_files = complexity_analysis.get(
        "top_risky_files",
        []
    )

    if high_risk_files:

        risky = high_risk_files[0]

        recommendations.append(
            f"⚠ {risky['file']} has elevated complexity and should be modularized."
        )

    dependency_hotspots = dependency_analysis.get(
        "most_connected_modules",
        []
    )

    if dependency_hotspots:

        hotspot = dependency_hotspots[0]

        recommendations.append(
            f"⚠ {hotspot['file']} shows high architectural coupling."
        )

    if functions > 300:

        recommendations.append(
            "⚡ Large function surface area detected. Consider domain-driven modularization."
        )

    elif functions > 150:

        recommendations.append(
            "⚡ Medium-scale repository detected with growing semantic complexity."
        )

    if react_components > 50:

        recommendations.append(
            "⚡ Large React component ecosystem detected. Lazy loading and component segmentation recommended."
        )

    if complexity < 70:

        recommendations.append(
            "⚠ Code complexity indicators suggest maintainability risks."
        )

    if dependency < 70:

        recommendations.append(
            "⚠ Dependency graph density is increasing architectural coupling."
        )

    if debt < 70:

        recommendations.append(
            "⚠ Technical debt indicators suggest refactoring opportunities."
        )

    if overall >= 85:

        recommendations.append(
            "✅ Repository architecture appears highly maintainable."
        )

    elif overall >= 60:

        recommendations.append(
            "⚡ Repository is stable but showing moderate engineering risk."
        )

    else:

        recommendations.append(
            "🚨 Repository health is degrading and requires architectural intervention."
        )

    return recommendations
