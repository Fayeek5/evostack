
PRIORITY_DIRECTORIES = [
    "src",
    "app",
    "backend",
    "frontend",
    "api",
    "services",
]

from pathlib import Path
import os
import time

IGNORED_DIRECTORIES = {
    ".git",
    "node_modules",
    "dist",
    "build",
    ".next",
    "coverage",
    "vendor",
    "target",
    "bin",
    "obj",
    "__pycache__",
    ".venv",
    "venv",
    "docs",
    "examples",
    "tmp",
    "temp"
}

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".java",
    ".go",
    ".rs",
    ".cpp",
    ".c",
    ".cs",
    ".php",
    ".rb"
}

MAX_FILES = 2000
MAX_FILE_SIZE = 1024 * 1024


def iter_repository_files(repo_path):
    analyzed = 0
    start_time = time.time()

    for root, dirs, files in os.walk(repo_path):

        if time.time() - start_time > 30:
            return

        dirs[:] = [
            d for d in dirs
            if d not in IGNORED_DIRECTORIES
        ]

        for file in files:

            if analyzed >= MAX_FILES:
                return

            path = Path(root) / file

            if path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            try:
                if path.stat().st_size > MAX_FILE_SIZE:
                    continue
            except:
                continue

            analyzed += 1

            yield path


import ast
from pathlib import Path

SUPPORTED_EXTENSIONS = [".py"]


def analyze_dependencies(repo_path: str):
    repo = Path(repo_path)

    dependency_map = []

    for file_path in iter_repository_files(repo):
        if file_path.suffix not in SUPPORTED_EXTENSIONS:
            continue

        try:
            code = file_path.read_text(encoding="utf-8")

            tree = ast.parse(code)

            imports = []

            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for alias in node.names:
                        imports.append(alias.name)

                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imports.append(node.module)

            dependency_map.append({
                "file": str(file_path.relative_to(repo)),
                "imports_count": len(imports),
                "imports": imports[:10]
            })

        except Exception as e:
            print(f"Dependency analysis failed for {file_path}: {e}")

    most_connected = sorted(
        dependency_map,
        key=lambda x: x["imports_count"],
        reverse=True
    )

    return {
        "total_modules": len(dependency_map),
        "most_connected_modules": most_connected[:10]
    }
