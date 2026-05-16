from backend.app.intelligence.complexity_engine import analyze_complexity
from backend.app.intelligence.dependency_engine import analyze_dependencies
from backend.app.intelligence.architecture_engine import detect_architecture
from backend.app.intelligence.semantic_engine import analyze_semantics

from backend.app.services.health_scoring import calculate_health_score
from backend.app.services.recommendation_engine import generate_recommendations
from backend.app.services.repository_ingestion import ingest_repository

from pathlib import Path


LIGHTWEIGHT_REPO_THRESHOLD = 800


def count_repository_files(repo_path):
    return sum(
        1
        for p in Path(repo_path).rglob("*")
        if p.is_file()
    )


class EvolutionPipeline:

    def run(self, repo_url: str):

        ingestion_result = ingest_repository(repo_url)

        repo_path = ingestion_result["repository_path"]

        file_count = count_repository_files(repo_path)

        lightweight_mode = file_count > LIGHTWEIGHT_REPO_THRESHOLD

        print(f"Lightweight mode: {lightweight_mode}")

        architecture_analysis = detect_architecture(repo_path)

        complexity_analysis = analyze_complexity(repo_path)

        if lightweight_mode:

            dependency_analysis = {
                "status": "Skipped in lightweight mode"
            }

            semantic_analysis = {
                "status": "Skipped in lightweight mode"
            }

        else:

            dependency_analysis = analyze_dependencies(repo_path)

            semantic_analysis = analyze_semantics(repo_path)

        health_score = calculate_health_score(analysis_results)
            complexity_analysis,
            dependency_analysis
        )

        recommendations = generate_recommendations(
            complexity_analysis,
            dependency_analysis,
            health_score
        )

        return {
            "repository": repo_url,
            "lightweight_mode": lightweight_mode,
            "repository_size": file_count,
            "architecture_analysis": architecture_analysis,
            "complexity_analysis": complexity_analysis,
            "dependency_analysis": dependency_analysis,
            "semantic_analysis": semantic_analysis,
            "health_score": health_score,
            "recommendations": recommendations,
        }
