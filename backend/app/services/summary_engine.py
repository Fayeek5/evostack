def generate_repository_summary(
    semantic_data,
    score_data
):

    frameworks = semantic_data.get(
        "frameworks",
        []
    )

    risky_files = semantic_data.get(
        "top_risky_files",
        []
    )

    architecture_style = (
        "modular"
        if semantic_data.get(
            "scanned_files",
            0
        ) < 120
        else "large-scale monolithic"
    )

    framework_text = (
        " + ".join(frameworks)
        if frameworks
        else "multi-framework"
    )

    summary = (

        f"This repository follows a "
        f"{architecture_style} architecture "

        f"built with {framework_text}. "
    )

    if risky_files:

        top_file = risky_files[0]

        summary += (

            f"The highest engineering risk "
            f"was detected in "

            f"{top_file.get('path', 'a core orchestration layer')} "

            f"with a risk score of "
            f"{top_file.get('risk_score', 0)}. "
        )

    complexity = score_data.get(
        "complexity",
        100
    )

    if complexity < 70:

        summary += (

            "The repository demonstrates "
            "moderate complexity accumulation "
            "and may benefit from additional "
            "service decomposition. "
        )

    maintainability = score_data.get(
        "maintainability",
        0
    )

    if maintainability >= 80:

        summary += (

            "Overall maintainability patterns "
            "appear healthy and scalable."
        )

    else:

        summary += (

            "Maintainability concerns were "
            "detected across several layers."
        )

    return summary
