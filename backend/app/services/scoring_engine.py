def calculate_engineering_score(semantic_data):

    scanned_files = semantic_data.get(
        "scanned_files",
        0
    )

    functions = semantic_data.get(
        "functions",
        0
    )

    components = semantic_data.get(
        "react_components",
        0
    )

    imports = semantic_data.get(
        "imports",
        0
    )

    risky_files = len(
        semantic_data.get(
            "top_risky_files",
            []
        )
    )

    # Maintainability

    maintainability = max(
        40,
        100 - (risky_files * 4)
    )

    # Complexity

    complexity = max(
        30,
        100 - ((functions + imports) / 3)
    )

    # Architecture

    architecture = min(
        100,
        60 + (components * 2)
    )

    # Dependencies

    dependencies = max(
        40,
        100 - imports
    )

    # Testing

    testing = 45

    if semantic_data.get("has_tests"):
        testing = 85

    modularity_bonus = 0

    if semantic_data.get(
        "hooks_layer",
        0
    ) > 0:

        modularity_bonus += 2

    if semantic_data.get(
        "service_layer",
        0
    ) > 0:

        modularity_bonus += 2

    if semantic_data.get(
        "components_layer",
        0
    ) > 0:

        modularity_bonus += 2

    overall_score = round(

        (
            maintainability * 0.25 +
            complexity * 0.20 +
            architecture * 0.20 +
            dependencies * 0.15 +
            testing * 0.20
        ) + modularity_bonus,

        1
    )

    overall_score = min(
        overall_score,
        100
    )


    grade = "C"

    if overall_score >= 90:
        grade = "A+"

    elif overall_score >= 80:
        grade = "A"

    elif overall_score >= 70:
        grade = "B"

    elif overall_score >= 60:
        grade = "C"



    return {

        "overall": overall_score,

        "grade": grade,

        "maintainability": round(
            maintainability,
            1
        ),

        "complexity": round(
            complexity,
            1
        ),

        "architecture": round(
            architecture,
            1
        ),

        "dependencies": round(
            dependencies,
            1
        ),

        "testing": round(
            testing,
            1
        )
    }
