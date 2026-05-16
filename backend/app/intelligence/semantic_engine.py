import esprima

from backend.app.intelligence.smart_file_selector import (
    get_priority_files,
)


def analyze_semantics(repo_path):

    result = {
        "functions": 0,
        "classes": 0,
        "async_functions": 0,
        "react_components": 0,
        "hooks": 0,
        "imports": 0,
    }

    priority_files = get_priority_files(repo_path)

    for file_path in priority_files:

        try:

            code = file_path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            tree = esprima.parseModule(
                code,
                tolerant=True
            )

            visit(tree, result)

        except Exception:
            continue

    return result


def visit(node, result):

    if isinstance(node, list):

        for item in node:
            visit(item, result)

        return

    if not hasattr(node, "type"):
        return

    node_type = node.type

    if node_type == "FunctionDeclaration":
        result["functions"] += 1

    elif node_type == "ClassDeclaration":
        result["classes"] += 1

    elif node_type == "ImportDeclaration":
        result["imports"] += 1

    elif node_type == "ArrowFunctionExpression":
        result["functions"] += 1

    if hasattr(node, "async") and node.async:
        result["async_functions"] += 1

    if hasattr(node, "id") and node.id:

        try:

            name = node.id.name

            if name.startswith("use"):
                result["hooks"] += 1

            if len(name) > 0 and name[0].isupper():
                result["react_components"] += 1

        except Exception:
            pass

    for attr in dir(node):

        if attr.startswith("_"):
            continue

        try:

            child = getattr(node, attr)

            visit(child, result)

        except Exception:
            continue
