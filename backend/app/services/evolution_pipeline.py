from backend.app.services.repository_ingestion import ingest_repository

from backend.app.intelligence.complexity_engine import analyze_complexity
from backend.app.intelligence.dependency_engine import analyze_dependencies
from backend.app.intelligence.semantic_engine import analyze_semantics
from backend.app.intelligence.architecture_engine import detect_architecture

from backend.app.services.health_scoring import calculate_health_score


class EvolutionPipeline:

    def __init__(self):
        pass

    def run(self, repo_url: str):

        ingestion_result = ingest_repository(repo_url)

        repo_path = ingestion_result["repository_path"]

        architecture_analysis = detect_architecture(repo_path)

        complexity_analysis = analyze_complexity(repo_path)

        dependency_analysis = analyze_dependencies(repo_path)

        semantic_analysis = analyze_semantics(repo_path)

        analysis_results = {
            "architecture": architecture_analysis,
            "complexity": complexity_analysis,
            "dependencies": dependency_analysis,
            "semantics": semantic_analysis,
        }

        health_score = calculate_health_score(
            complexity_analysis,
            dependency_analysis,
            analysis_results
        )

        return {
            "status": "success",
            "repository": repo_url,
            "health_score": health_score,
            "analysis": analysis_results,
        }
