from pathlib import Path

IMPORTANT_EXTENSIONS = {
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".py",
    ".go",
    ".java",
    ".rs",
}

MAX_FILES = 250


def get_priority_files(repo_path):

    selected_files = []

    priority_keywords = [
        "src",
        "app",
        "core",
        "server",
        "api",
        "lib",
        "main",
    ]

    for file_path in Path(repo_path).rglob("*"):

        if not file_path.is_file():
            continue

        if file_path.suffix not in IMPORTANT_EXTENSIONS:
            continue

        path_string = str(file_path).lower()

        priority_score = 0

        for keyword in priority_keywords:

            if keyword in path_string:
                priority_score += 1

        selected_files.append(
            (priority_score, file_path)
        )

    selected_files.sort(
        key=lambda x: x[0],
        reverse=True
    )

    return [
        file_path
        for _, file_path in selected_files[:MAX_FILES]
    ]
