from app.services.repo_manager import (
    clone_repository
)

from app.intelligence.semantic_engine import (
    analyze_semantics
)

from app.database.persistence import (
    save_analysis_snapshot
)

from app.services.scoring_engine import (
    calculate_engineering_score
)

from app.services.recommendation_engine import (
    generate_recommendations
)

from app.services.summary_engine import (
    generate_repository_summary
)


class EvolutionPipeline:

    def analyze_repository(self, repo_url: str):

        repo_path = clone_repository(
            repo_url
        )

        semantic_data = analyze_semantics(
            repo_path
        )

        score_data = calculate_engineering_score(
            semantic_data
        )

        overall_score = score_data["overall"]

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

        recommendations = generate_recommendations(
            semantic_data,
            score_data
        )

        executive_summary = (
            generate_repository_summary(
                semantic_data,
                score_data
            )
        )

        result = {

            "status": "success",

            "repository": repo_url,

            "health_score": {

                "overall": overall_score,

                "maintainability": score_data["maintainability"],

                "complexity": score_data["complexity"],

                "architecture": score_data["architecture"],

                "dependencies": score_data["dependencies"],

                "testing": score_data["testing"],

                "maintainability_rating": (
                    "A"
                    if overall_score >= 85
                    else "B"
                )
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
            },

            "recommendations": recommendations,

            "executive_summary": executive_summary
        }

        save_analysis_snapshot(
            result
        )

        return result
