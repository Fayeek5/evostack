import os
import re

from backend.app.config import (
    IGNORE_DIRS,
    SUPPORTED_EXTENSIONS,
    MAX_FILES
)


def analyze_semantics(repo_path):

    functions = 0
    async_functions = 0
    classes = 0
    react_components = 0

    scanned_files = 0

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        for file in files:

            if scanned_files >= MAX_FILES:
                break

            ext = os.path.splitext(file)[1]

            if ext not in SUPPORTED_EXTENSIONS:
                continue

            scanned_files += 1

            try:

                path = os.path.join(root, file)

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                functions += len(
                    re.findall(
                        r'function\s+\w+|\w+\s*=\s*\(?.*\)?\s*=>',
                        content
                    )
                )

                async_functions += len(
                    re.findall(
                        r'async\s+function|async\s*\(',
                        content
                    )
                )

                classes += len(
                    re.findall(
                        r'class\s+\w+',
                        content
                    )
                )

                react_components += len(
                    re.findall(
                        r'export default function|const\s+\w+\s*=\s*\(',
                        content
                    )
                )

            except:
                pass

    return {

        "functions": functions,
        "classes": classes,
        "async_functions": async_functions,
        "react_components": react_components,
        "scanned_files": scanned_files
    }
