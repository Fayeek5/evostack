import ast
from pathlib import Path

SUPPORTED_EXTENSIONS = [".py"]


def analyze_dependencies(repo_path: str):
    repo = Path(repo_path)

    dependency_map = []

    for file_path in repo.rglob("*"):
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
