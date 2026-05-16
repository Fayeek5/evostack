from pathlib import Path
import json
from backend.app.intelligence.constants import IGNORED_DIRECTORIES


FRAMEWORK_SIGNATURES = {
    "react": "React",
    "next": "Next.js",
    "express": "Express",
    "nestjs": "NestJS",
    "vue": "Vue",
    "nuxt": "Nuxt",
    "fastapi": "FastAPI",
    "django": "Django",
    "flask": "Flask",
    "spring": "Spring Boot",
    "laravel": "Laravel",
}


def detect_architecture(repo_path):

    language_stats = {}

    frameworks = set()

    total_files = 0

    for file_path in Path(repo_path).rglob("*"):

        if any(
            ignored in file_path.parts
            for ignored in IGNORED_DIRECTORIES
        ):
            continue

        if not file_path.is_file():
            continue

        suffix = file_path.suffix.lower()

        if suffix:

            language_stats[suffix] = (
                language_stats.get(suffix, 0) + 1
            )

            total_files += 1

        if file_path.name == "package.json":

            try:

                package_data = json.loads(
                    file_path.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )
                )

                dependencies = {
                    **package_data.get("dependencies", {}),
                    **package_data.get("devDependencies", {}),
                }

                for dependency in dependencies:

                    dep_lower = dependency.lower()

                    for key, framework in FRAMEWORK_SIGNATURES.items():

                        if key in dep_lower:
                            frameworks.add(framework)

            except Exception:
                pass

    language_percentages = {}

    for extension, count in language_stats.items():

        percentage = round(
            (count / total_files) * 100,
            2
        )

        language_percentages[
            extension.replace(".", "").upper()
        ] = percentage

    primary_language = "Unknown"

    if language_percentages:

        primary_language = max(
            language_percentages,
            key=language_percentages.get
        )

    return {
        "repository_type": (
            "Monorepo"
            if total_files > 100
            else "Standard Repository"
        ),
        "primary_language": primary_language,
        "languages": language_percentages,
        "frameworks": list(frameworks),
        "ci_cd": [],
        "cloud": [],
        "infrastructure": [],
    }
