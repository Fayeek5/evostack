import os
import re

from app.config import (
    IGNORE_DIRS,
    SUPPORTED_EXTENSIONS,
    MAX_FILES
)


def analyze_semantics(repo_path):

    functions = 0
    async_functions = 0
    classes = 0
    react_components = 0
    imports = 0
    api_routes = 0
    hooks = 0
    test_files = 0

    component_dirs = 0
    service_dirs = 0
    api_dirs = 0
    hook_dirs = 0

    file_metrics = []

    frameworks = set()

    detected_languages = set()

    scanned_files = 0

    for root, dirs, files in os.walk(repo_path):

        dirs[:] = [
            d for d in dirs
            if d not in IGNORE_DIRS
        ]

        lowered_dirs = [
            d.lower()
            for d in dirs
        ]

        if "components" in lowered_dirs:
            component_dirs += 1

        if "services" in lowered_dirs:
            service_dirs += 1

        if "api" in lowered_dirs:
            api_dirs += 1

        if "hooks" in lowered_dirs:
            hook_dirs += 1

        for file in files:

            if scanned_files >= MAX_FILES:
                break

            ext = os.path.splitext(file)[1]

            if ext in [".ts", ".tsx"]:
                detected_languages.add("TypeScript")

            elif ext in [".js", ".jsx"]:
                detected_languages.add("JavaScript")

            elif ext == ".py":
                detected_languages.add("Python")

            elif ext == ".go":
                detected_languages.add("Go")

            if ext not in SUPPORTED_EXTENSIONS:
                continue

            scanned_files += 1

            try:

                path = os.path.join(root, file)

                lower_file = file.lower()

                if lower_file == "package.json":
                    frameworks.add("Node.js")

                if lower_file == "requirements.txt":
                    detected_languages.add("Python")

                if lower_file == "go.mod":
                    detected_languages.add("Go")

                if lower_file == "cargo.toml":
                    detected_languages.add("Rust")

                if lower_file == "pom.xml":
                    detected_languages.add("Java")

                with open(
                    path,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    content = f.read()

                file_functions = len(
                    re.findall(
                        r'function\s+\w+|\w+\s*=\s*\(?.*\)?\s*=>',
                        content
                    )
                )

                functions += file_functions

                file_async = len(
                    re.findall(
                        r'async\s+function|async\s*\(',
                        content
                    )
                )

                async_functions += file_async

                file_classes = len(
                    re.findall(
                        r'class\s+\w+',
                        content
                    )
                )

                classes += file_classes

                file_imports = len(
                    re.findall(
                        r'import\s+.*?from|require\(',
                        content
                    )
                )

                imports += file_imports

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

                imports += len(
                    re.findall(
                        r'import\s+.*?from|require\(',
                        content
                    )
                )

                api_routes += len(
                    re.findall(
                        r'app\.(get|post|put|delete)|router\.',
                        content
                    )
                )

                hooks += len(
                    re.findall(
                        r'use(State|Effect|Memo|Callback|Ref)',
                        content
                    )
                )

                lines_of_code = len(
                    content.splitlines()
                )

                risk_score = round(

                    (
                        file_functions * 2 +
                        file_imports * 1.5 +
                        file_async * 3 +
                        file_classes * 2
                    ),

                    2
                )

                risk_level = "low"

                if risk_score >= 80:
                    risk_level = "high"

                elif risk_score >= 40:
                    risk_level = "medium"

                file_metrics.append({

                    "path": os.path.relpath(
                        path,
                        repo_path
                    ),

                    "functions": file_functions,
                    "imports": file_imports,
                    "async_functions": file_async,
                    "classes": file_classes,

                    "lines_of_code": lines_of_code,

                    "risk_score": risk_score,
                    "risk_level": risk_level
                })

                if (
                    "test" in file.lower()
                    or "spec" in file.lower()
                ):
                    test_files += 1

                lower_content = content.lower()

                is_source_file = ext in [
                    ".js",
                    ".jsx",
                    ".ts",
                    ".tsx",
                    ".py",
                    ".go"
                ]

                if is_source_file:

                    if re.search(
                        r'import\s+react|from\s+[\'"]react[\'"]',
                        lower_content
                    ):
                        frameworks.add("React")

                    if re.search(
                        r'from\s+[\'"]next',
                        lower_content
                    ):
                        frameworks.add("Next.js")

                    if re.search(
                        r'from\s+fastapi\s+import|import\s+fastapi',
                        lower_content
                    ):
                        frameworks.add("FastAPI")

                    if re.search(
                        r'from\s+[\'"]express[\'"]|require\([\'"]express[\'"]\)',
                        lower_content
                    ):
                        frameworks.add("Express")

                    if re.search(
                        r'from\s+django|import\s+django',
                        lower_content
                    ):
                        frameworks.add("Django")

                    if re.search(
                        r'github.com/gin-gonic/gin|github.com/gorilla/mux',
                        lower_content
                    ):
                        frameworks.add("Go HTTP Framework")

            except:
                pass

    top_risky_files = sorted(

        file_metrics,

        key=lambda x: x["risk_score"],

        reverse=True

    )[:5]

    async_hotspots = sorted(

        file_metrics,

        key=lambda x: x["async_functions"],

        reverse=True

    )[:5]

    largest_modules = sorted(

        file_metrics,

        key=lambda x: x["lines_of_code"],

        reverse=True

    )[:5]

    dependency_hotspots = sorted(

        file_metrics,

        key=lambda x: x["imports"],

        reverse=True

    )[:5]

    dependency_density = round(
        imports / max(scanned_files, 1),
        2
    )

    return {

        "functions": functions,
        "classes": classes,
        "async_functions": async_functions,
        "react_components": react_components,
        "imports": imports,
        "api_routes": api_routes,
        "hooks": hooks,
        "test_files": test_files,
        "frameworks": list(frameworks),
        "detected_languages": list(detected_languages),
        "dependency_density": dependency_density,

        "component_directories": component_dirs,
        "service_directories": service_dirs,
        "api_directories": api_dirs,
        "hook_directories": hook_dirs,

        "top_risky_files": top_risky_files,

        "has_tests": has_tests,
        "async_hotspots": async_hotspots,
        "dependency_hotspots": dependency_hotspots,

        "largest_modules": largest_modules,

        "file_metrics": file_metrics,

        "scanned_files": scanned_files
    }
