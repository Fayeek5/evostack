from pathlib import Path
import json


def detect_architecture(repo_path: str):
    repo = Path(repo_path)

    detected = {
        "repository_type": "General Software Project",
        "primary_language": "Unknown",
        "architecture_style": "Standard Application Architecture",
        "frameworks": [],
        "testing_density": "Low"
    }

    package_json = list(repo.rglob("package.json"))
    requirements = list(repo.rglob("requirements.txt"))
    docker_files = list(repo.rglob("Dockerfile"))

    # ------------------------
    # NODE / TYPESCRIPT DETECTION
    # ------------------------

    if package_json:
        detected["primary_language"] = "TypeScript/JavaScript"

        for pkg in package_json:
            try:
                data = json.loads(pkg.read_text())

                deps = {
                    **data.get("dependencies", {}),
                    **data.get("devDependencies", {})
                }

                dep_keys = deps.keys()

                if "next" in dep_keys:
                    detected["frameworks"].append("Next.js")
                    detected["repository_type"] = "Frontend Application"

                if "react" in dep_keys:
                    detected["frameworks"].append("React")

                if "express" in dep_keys:
                    detected["frameworks"].append("Express.js")
                    detected["repository_type"] = "Backend API"

                if "nestjs" in dep_keys:
                    detected["frameworks"].append("NestJS")

                if "typescript" in dep_keys:
                    detected["primary_language"] = "TypeScript"

                if "jest" in dep_keys:
                    detected["testing_density"] = "High"

            except:
                pass

    # ------------------------
    # PYTHON DETECTION
    # ------------------------

    if requirements:
        detected["primary_language"] = "Python"

        for req in requirements:
            try:
                content = req.read_text().lower()

                if "fastapi" in content:
                    detected["frameworks"].append("FastAPI")
                    detected["repository_type"] = "Backend API"

                if "django" in content:
                    detected["frameworks"].append("Django")

                if "flask" in content:
                    detected["frameworks"].append("Flask")

                if "pytest" in content:
                    detected["testing_density"] = "High"

            except:
                pass

    # ------------------------
    # INFRASTRUCTURE DETECTION
    # ------------------------

    if docker_files:
        detected["frameworks"].append("Docker")

    detected["frameworks"] = list(set(detected["frameworks"]))

    return detected
