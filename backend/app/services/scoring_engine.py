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

    async_functions = semantic_data.get(
        "async_functions",
        0
    )

    risky_files = semantic_data.get(
        "top_risky_files",
        []
    )

    file_metrics = semantic_data.get(
        "file_metrics",
        []
    )

    has_tests = semantic_data.get(
        "has_tests",
        False
    )

    # -------------------------
    # Maintainability
    # -------------------------

    maintainability = 100

    maintainability -= len(risky_files) * 3

    oversized_files = 0

    for file in file_metrics:

        if file.get("loc", 0) > 250:
            oversized_files += 1

    maintainability -= oversized_files * 4

    maintainability = max(
        35,
        maintainability
    )

    # -------------------------
    # Complexity
    # -------------------------

    complexity = 100

    complexity -= (functions * 0.8)

    complexity -= (imports * 0.5)

    complexity -= (async_functions * 2)

    complexity -= (oversized_files * 5)

    complexity = max(
        25,
        complexity
    )

    # -------------------------
    # Architecture
    # -------------------------

    architecture = 55

    if semantic_data.get("components_layer", 0) > 0:
        architecture += 10

    if semantic_data.get("hooks_layer", 0) > 0:
        architecture += 10

    if semantic_data.get("service_layer", 0) > 0:
        architecture += 15

    if semantic_data.get("api_layer", 0) > 0:
        architecture += 10

    architecture += min(
        10,
        components
    )

    architecture = min(
        100,
        architecture
    )

    # -------------------------
    # Dependencies
    # -------------------------

    dependency_density = 0

    if scanned_files > 0:

        dependency_density = (
            imports / scanned_files
        )

    dependencies = 100

    dependencies -= dependency_density * 6

    dependencies = max(
        35,
        dependencies
    )

    # -------------------------
    # Testing
    # -------------------------

    testing = 40

    if has_tests:
        testing = 85

    # -------------------------
    # Overall weighted score
    # -------------------------

    overall_score = round(

        (
            maintainability * 0.25 +
            complexity * 0.25 +
            architecture * 0.20 +
            dependencies * 0.10 +
            testing * 0.20
        ),

        1
    )

    overall_score = min(
        overall_score,
        100
    )

    # -------------------------
    # Grade
    # -------------------------

    grade = "C"

    if overall_score >= 90:
        grade = "A+"

    elif overall_score >= 80:
        grade = "A"

    elif overall_score >= 70:
        grade = "B"

    elif overall_score >= 60:
        grade = "C"

    else:
        grade = "D"

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
