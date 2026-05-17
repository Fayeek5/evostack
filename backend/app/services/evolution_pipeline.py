from app.services.repo_manager import (
    clone_repository
)

from app.intelligence.semantic_engine import (
    analyze_semantics
)

from app.database.persistence import (
    save_analysis_snapshot
)


class EvolutionPipeline:

    def analyze_repository(self, repo_url: str):

        repo_path = clone_repository(
            repo_url
        )

        semantic_data = analyze_semantics(
            repo_path
        )

        overall_score = 100

        if semantic_data["functions"] == 0:
            overall_score = 45

        frameworks = semantic_data.get(
            "frameworks",
            []
        )

        primary_language = "Unknown"

        if "React" in frameworks:
            primary_language = "TypeScript"

        elif "FastAPI" in frameworks:
            primary_language = "Python"

        elif "Go HTTP Framework" in frameworks:
            primary_language = "Go"

        result = {

            "status": "success",

            "repository": repo_url,

            "health_score": {

                "overall": overall_score,

                "maintainability_rating": "A"
            },

            "analysis": {

                "architecture": {

                    "primary_language": primary_language,

                    "repository_type": (
                        "Large Monolith"
                        if semantic_data["scanned_files"] > 120
                        else "Modular Repository"
                    ),

                    "frameworks": frameworks
                },

                "semantics": semantic_data
            }
        }

        save_analysis_snapshot(
            result
        )

        return result
