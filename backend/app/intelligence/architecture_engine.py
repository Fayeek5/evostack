from pathlib import Path


def analyze_architecture(
    repo_path,
    semantic_analysis,
    dependency_analysis
):
    repo = Path(repo_path)

    frameworks = []

    python_files = list(repo.rglob("*.py"))
    js_files = list(repo.rglob("*.js"))
    ts_files = list(repo.rglob("*.ts"))
    jsx_files = list(repo.rglob("*.jsx"))
    tsx_files = list(repo.rglob("*.tsx"))

    total_files = (
        len(python_files)
        + len(js_files)
        + len(ts_files)
        + len(jsx_files)
        + len(tsx_files)
    )

    async_functions = semantic_analysis.get(
        "async_functions",
        0
    )

    if python_files:
        primary_language = "Python"

    elif ts_files or tsx_files:
        primary_language = "TypeScript"

    elif js_files or jsx_files:
        primary_language = "JavaScript"

    else:
        primary_language = "Unknown"

    all_files = list(repo.rglob("*"))

    for file in all_files:
        filename = file.name.lower()

        if "fastapi" in filename:
            frameworks.append("FastAPI")

        if "django" in filename:
            frameworks.append("Django")

        if "package.json" == filename:
            frameworks.append("Node.js")

        if "requirements.txt" == filename:
            frameworks.append("Python Environment")

    frameworks = list(set(frameworks))

    if async_functions > 100:
        architecture_style = (
            "Async Service Architecture"
        )

    else:
        architecture_style = (
            "Standard Application Architecture"
        )

    test_files = [
        file for file in all_files
        if "test" in file.name.lower()
    ]

    testing_density = (
        "High"
        if len(test_files) > total_files * 0.2
        else "Moderate"
    )

    if python_files and async_functions > 100:
        repository_type = "Backend API"

    elif tsx_files or jsx_files:
        repository_type = "Frontend Application"

    else:
        repository_type = "General Software Project"

    return {
        "primary_language": primary_language,
        "repository_type": repository_type,
        "frameworks_detected": frameworks,
        "architecture_style": architecture_style,
        "testing_density": testing_density
    }
