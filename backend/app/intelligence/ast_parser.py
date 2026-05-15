import ast
import re
from pathlib import Path

PYTHON_EXTENSIONS = [".py"]

JS_TS_EXTENSIONS = [
    ".js",
    ".jsx",
    ".ts",
    ".tsx"
]


def analyze_semantics(repo_path: str):
    repo = Path(repo_path)

    total_functions = 0
    total_classes = 0
    async_functions = 0
    react_components = 0

    large_functions = []

    decorators = {}

    hooks = {
        "useState": 0,
        "useEffect": 0,
        "useMemo": 0,
        "useCallback": 0
    }

    for file_path in repo.rglob("*"):

        suffix = file_path.suffix

        try:
            code = file_path.read_text(
                encoding="utf-8"
            )

            # -------------------------
            # PYTHON ANALYSIS
            # -------------------------

            if suffix in PYTHON_EXTENSIONS:

                tree = ast.parse(code)

                for node in ast.walk(tree):

                    if isinstance(
                        node,
                        ast.FunctionDef
                    ):
                        total_functions += 1

                        function_length = (
                            node.end_lineno - node.lineno
                            if hasattr(node, "end_lineno")
                            and node.end_lineno
                            else 0
                        )

                        if function_length > 50:
                            large_functions.append({
                                "name": node.name,
                                "lines": function_length,
                                "file": str(
                                    file_path.relative_to(repo)
                                )
                            })

                        for decorator in node.decorator_list:
                            if isinstance(
                                decorator,
                                ast.Attribute
                            ):
                                decorator_name = (
                                    decorator.attr
                                )

                                decorators[
                                    decorator_name
                                ] = decorators.get(
                                    decorator_name,
                                    0
                                ) + 1

                    elif isinstance(
                        node,
                        ast.AsyncFunctionDef
                    ):
                        async_functions += 1

                    elif isinstance(
                        node,
                        ast.ClassDef
                    ):
                        total_classes += 1

            # -------------------------
            # TYPESCRIPT / JS ANALYSIS
            # -------------------------

            elif suffix in JS_TS_EXTENSIONS:

                function_matches = re.findall(
                    r'function\s+\w+|const\s+\w+\s*=\s*\(',
                    code
                )

                total_functions += len(
                    function_matches
                )

                async_matches = re.findall(
                    r'async\s+function|async\s+\(',
                    code
                )

                async_functions += len(
                    async_matches
                )

                component_matches = re.findall(
                    r'export\s+default\s+function|const\s+\w+\s*=\s*\(',
                    code
                )

                react_components += len(
                    component_matches
                )

                for hook in hooks.keys():
                    hooks[hook] += len(
                        re.findall(hook, code)
                    )

                lines = code.count("\n")

                if lines > 200:
                    large_functions.append({
                        "name": file_path.name,
                        "lines": lines,
                        "file": str(
                            file_path.relative_to(repo)
                        )
                    })

        except Exception as e:
            print(
                f"Semantic analysis failed for {file_path}: {e}"
            )

    top_decorators = dict(
        sorted(
            decorators.items(),
            key=lambda x: x[1],
            reverse=True
        )[:10]
    )

    large_functions = sorted(
        large_functions,
        key=lambda x: x["lines"],
        reverse=True
    )[:10]

    return {
        "functions": total_functions,
        "classes": total_classes,
        "async_functions": async_functions,
        "react_components": react_components,
        "large_functions": large_functions,
        "top_decorators": top_decorators,
        "hooks_detected": hooks
    }
