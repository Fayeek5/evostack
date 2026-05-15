
PRIORITY_DIRECTORIES = [
    "src",
    "app",
    "backend",
    "frontend",
    "api",
    "services",
]
from pathlib import Path
import json
from collections import Counter


LANGUAGE_EXTENSIONS = {
    ".py": "Python",
    ".js": "JavaScript",
    ".jsx": "React",
    ".ts": "TypeScript",
    ".tsx": "React TypeScript",
    ".java": "Java",
    ".go": "Go",
    ".rs": "Rust",
    ".php": "PHP",
    ".rb": "Ruby",
    ".cs": "C#",
    ".cpp": "C++",
    ".c": "C",
    ".swift": "Swift",
    ".kt": "Kotlin",
    ".scala": "Scala",
    ".yaml": "YAML",
    ".yml": "YAML",
    ".tf": "Terraform",
    ".sh": "Shell",
}


def detect_architecture(repo_path: str):
    repo = Path(repo_path)

    languages = Counter()

    frameworks = set()

    ci_cd = set()

    cloud = set()

    infrastructure = set()

    repository_type = "General Software Project"

    # ------------------------
    # LANGUAGE DETECTION
    # ------------------------

    for file_path in repo.rglob("*"):

        if file_path.is_file():

            ext = file_path.suffix.lower()

            if ext in LANGUAGE_EXTENSIONS:
                languages[LANGUAGE_EXTENSIONS[ext]] += 1

            # Docker detection
            if file_path.name == "Dockerfile":
                infrastructure.add("Docker")

            # GitHub Actions
            if ".github/workflows" in str(file_path):
                ci_cd.add("GitHub Actions")

            # Kubernetes
            if "k8s" in str(file_path).lower():
                infrastructure.add("Kubernetes")

            # Terraform
            if ext == ".tf":
                infrastructure.add("Terraform")

    # ------------------------
    # PACKAGE.JSON ANALYSIS
    # ------------------------

    package_json_files = list(repo.rglob("package.json"))

    for pkg in package_json_files:

        try:
            data = json.loads(pkg.read_text())

            deps = {
                **data.get("dependencies", {}),
                **data.get("devDependencies", {})
            }

            dep_keys = deps.keys()

            if "next" in dep_keys:
                frameworks.add("Next.js")

            if "react" in dep_keys:
                frameworks.add("React")

            if "express" in dep_keys:
                frameworks.add("Express.js")

            if "nestjs" in dep_keys:
                frameworks.add("NestJS")

            if "vue" in dep_keys:
                frameworks.add("Vue")

            if "angular" in dep_keys:
                frameworks.add("Angular")

            if "vite" in dep_keys:
                frameworks.add("Vite")

            if "jest" in dep_keys:
                frameworks.add("Jest")

            if "tailwindcss" in dep_keys:
                frameworks.add("TailwindCSS")

        except:
            pass

    # ------------------------
    # PYTHON REQUIREMENTS
    # ------------------------

    requirements_files = list(repo.rglob("requirements.txt"))

    for req in requirements_files:

        try:
            content = req.read_text().lower()

            if "fastapi" in content:
                frameworks.add("FastAPI")

            if "django" in content:
                frameworks.add("Django")

            if "flask" in content:
                frameworks.add("Flask")

            if "pytest" in content:
                frameworks.add("Pytest")

            if "celery" in content:
                frameworks.add("Celery")

        except:
            pass

    # ------------------------
    # CLOUD DETECTION
    # ------------------------

    if list(repo.rglob("vercel.json")):
        cloud.add("Vercel")

    if list(repo.rglob("render.yaml")):
        cloud.add("Render")

    if list(repo.rglob("docker-compose.yml")):
        infrastructure.add("Docker Compose")

    # ------------------------
    # REPOSITORY TYPE
    # ------------------------

    if "Next.js" in frameworks and "FastAPI" in frameworks:
        repository_type = "Fullstack AI Platform"

    elif "Next.js" in frameworks:
        repository_type = "Frontend Application"

    elif "FastAPI" in frameworks or "Express.js" in frameworks:
        repository_type = "Backend API"

    elif len(package_json_files) > 1:
        repository_type = "Monorepo"

    primary_language = (
        languages.most_common(1)[0][0]
        if languages
        else "Unknown"
    )

    total_files = sum(languages.values())

    language_distribution = {}

    for lang, count in languages.items():

        percentage = (
            round((count / total_files) * 100, 2)
            if total_files > 0
            else 0
        )

        language_distribution[lang] = percentage

    return {
        "repository_type": repository_type,
        "primary_language": primary_language,
        "languages": language_distribution,
        "frameworks": sorted(list(frameworks)),
        "ci_cd": sorted(list(ci_cd)),
        "cloud": sorted(list(cloud)),
        "infrastructure": sorted(list(infrastructure))
    }
