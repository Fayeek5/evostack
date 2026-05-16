from backend.app.services.repo_manager import clone_repository
from backend.app.intelligence.semantic_engine import analyze_semantics
from backend.app.services.recommendation_engine import generate_recommendations


class EvolutionPipeline:

    def analyze_repository(self, repo_url: str):

        repo_path = clone_repository(repo_url)

        semantic_data = analyze_semantics(repo_path)

        functions = semantic_data.get(
            "functions",
            0
        )

        react_components = semantic_data.get(
            "react_components",
            0
        )

        complexity_score = max(
            30,
            100 - int(functions * 0.15)
        )

        dependency_score = max(
            40,
            100 - int(react_components * 0.8)
        )

        technical_debt_score = int(
            (complexity_score + dependency_score) / 2
        )

        overall_score = int(
            (
                complexity_score +
                dependency_score +
                technical_debt_score
            ) / 3
        )

        detected_languages = semantic_data.get(
            "detected_languages",
            []
        )

        if len(detected_languages) == 0:

            language = "Unknown"

        else:

            language = detected_languages[0]

        health_score = {
            "overall": overall_score,
            "complexity_score": complexity_score,
            "dependency_score": dependency_score,
            "technical_debt_score": technical_debt_score,
            "maintainability_rating": (
                "A" if overall_score >= 80
                else "B" if overall_score >= 60
                else "C"
            )
        }

        recommendations = generate_recommendations(
            complexity_analysis={},
            dependency_analysis={},
            health_score=health_score,
            semantic_analysis=semantic_data
        )

        return {
            "status": "success",
            "repository": repo_url,

            "health_score": health_score,

            "analysis": {

                "architecture": {
                    "primary_language": language,
                    "repository_type": "Modern Repository"
                },

                "semantics": semantic_data
            },

            "recommendations": recommendations
        }
