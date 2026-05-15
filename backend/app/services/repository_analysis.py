
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


import os


class RepositoryAnalyzer:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    async def analyze(self):
        issues = []
        total_files = 0
        todo_count = 0

        for root, _, files in os.walk(self.repo_path):
            for file in files:
                total_files += 1

                filepath = os.path.join(root, file)

                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                        if "TODO" in content:
                            todo_count += 1
                            issues.append(
                                f"TODO detected in {file}"
                            )

                        if "FIXME" in content:
                            issues.append(
                                f"FIXME detected in {file}"
                            )

                except:
                    pass

        complexity_score = max(
            1,
            100 - (todo_count * 5)
        )

        return {
            "repository": self.repo_path,
            "total_files": total_files,
            "complexity_score": complexity_score,
            "issues": issues[:20]
        }
