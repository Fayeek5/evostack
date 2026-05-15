
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


from pathlib import Path
import ast


SUPPORTED_EXTENSIONS = [".py"]


def analyze_semantics(repo_path: str):
    repo = Path(repo_path)

    total_functions = 0
    total_classes = 0
    async_functions = 0

    large_functions = []

    decorator_usage = {}

    for file_path in iter_repository_files(repo):
        if file_path.suffix not in SUPPORTED_EXTENSIONS:
            continue

        try:
            code = file_path.read_text(encoding="utf-8")

            tree = ast.parse(code)

            for node in ast.walk(tree):

                if isinstance(node, ast.FunctionDef):
                    total_functions += 1

                    function_length = (
                        node.end_lineno - node.lineno
                        if node.end_lineno
                        else 0
                    )

                    if function_length > 150:
                        large_functions.append({
                            "name": node.name,
                            "lines": function_length,
                            "file": str(file_path.relative_to(repo))
                        })

                    for decorator in node.decorator_list:
                        if isinstance(decorator, ast.Name):
                            decorator_usage[decorator.id] = (
                                decorator_usage.get(decorator.id, 0) + 1
                            )

                elif isinstance(node, ast.AsyncFunctionDef):
                    async_functions += 1
                    total_functions += 1

                elif isinstance(node, ast.ClassDef):
                    total_classes += 1

        except Exception:
            pass

    top_decorators = dict(
        sorted(
            decorator_usage.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
    )

    return {
        "functions": total_functions,
        "classes": total_classes,
        "async_functions": async_functions,
        "large_functions": large_functions[:10],
        "top_decorators": top_decorators
    }
