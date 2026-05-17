def generate_recommendations(analysis):

    recommendations = []

    hotspots = analysis.get("hotspots", [])

    for hotspot in hotspots:

        risk = hotspot.get("risk_score", 0)
        path = hotspot.get("path", "unknown")

        if risk >= 30:
            recommendations.append({
                "severity": "high",
                "title": "Large orchestration layer detected",
                "description": f"{path} has elevated engineering complexity and should be modularized."
            })

        elif risk >= 10:
            recommendations.append({
                "severity": "medium",
                "title": "Moderate engineering complexity",
                "description": f"{path} should be reviewed for maintainability improvements."
            })

    dependency_density = analysis.get("dependency_density", "low")

    if dependency_density == "high":
        recommendations.append({
            "severity": "medium",
            "title": "High dependency concentration",
            "description": "The repository exhibits heavy dependency usage."
        })

    testing = analysis.get("testing_maturity", "weak")

    if testing == "weak":
        recommendations.append({
            "severity": "medium",
            "title": "Testing maturity is weak",
            "description": "No significant test coverage was detected in the repository."
        })

    recommendations.append({
        "severity": "success",
        "title": "Architecture appears maintainable",
        "description": "The repository demonstrates healthy maintainability patterns."
    })

    return recommendations
