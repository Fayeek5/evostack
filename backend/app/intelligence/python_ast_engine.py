import ast


def analyze_python_complexity(file_path):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as f:

            source = f.read()

        tree = ast.parse(source)

        function_count = 0

        complexity_score = 0

        nested_depth = 0

        for node in ast.walk(tree):

            if isinstance(
                node,
                ast.FunctionDef
            ):

                function_count += 1

                node_complexity = len(
                    list(ast.walk(node))
                )

                complexity_score += (
                    node_complexity / 10
                )

            if isinstance(
                node,
                (
                    ast.If,
                    ast.For,
                    ast.While,
                    ast.Try
                )
            ):

                nested_depth += 1

        return {

            "functions": function_count,

            "complexity": round(
                complexity_score,
                1
            ),

            "nested_depth": nested_depth
        }

    except Exception:

        return {

            "functions": 0,

            "complexity": 0,

            "nested_depth": 0
        }
