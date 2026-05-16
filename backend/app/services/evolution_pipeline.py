from backend.app.services.repo_manager import clone_repository
from backend.app.intelligence.semantic_engine import analyze_semantics


class EvolutionPipeline:

    def analyze_repository(self, repo_url: str):

        repo_path = clone_repository(repo_url)

        semantic_data = analyze_semantics(repo_path)

        overall_score = 100

        if semantic_data["functions"] == 0:
            overall_score = 45

        return {
            "status": "success",
            "repository": repo_url,

            "health_score": {
                "overall": overall_score,
                "maintainability_rating": "A"
            },

            "analysis": {

                "architecture": {
                    "primary_language": "JavaScript",
                    "repository_type": "Modern Repository"
                },

                "semantics": semantic_data
            }
        }
