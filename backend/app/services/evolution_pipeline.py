import asyncio

from backend.app.intelligence.complexity_engine import analyze_complexity
from backend.app.intelligence.dependency_engine import analyze_dependencies
from backend.app.intelligence.semantic_engine import analyze_semantics
from backend.app.intelligence.architecture_engine import detect_architecture

from .repository_ingestion import RepositoryIngestionService
from .repository_analysis import RepositoryAnalyzer
from .health_scoring import calculate_health_score
from .recommendation_engine import generate_recommendations


class EvolutionPipeline:
    def __init__(self, clone_path=None):
        self.clone_path = clone_path

    async def run(self, repo_url, branch=None):
        ingestion_service = RepositoryIngestionService()

        cloned_repo_path = await asyncio.to_thread(
            ingestion_service.clone_repository,
            repo_url,
            branch
        )

        analyzer = RepositoryAnalyzer(cloned_repo_path)

        analysis_results = await analyzer.analyze()

        complexity_results = analyze_complexity(cloned_repo_path)

        dependency_results = analyze_dependencies(cloned_repo_path)

        semantic_results = analyze_semantics(cloned_repo_path)

        architecture_analysis = detect_architecture(cloned_repo_path)

        health_score = calculate_health_score(
            complexity_results,
            dependency_results,
            analysis_results
        )

        recommendations = generate_recommendations(
            complexity_results,
            dependency_results,
            health_score
        )

        ingestion_service.cleanup()

        return {
            "repo_url": repo_url,
            "branch": branch,
            "analysis_results": analysis_results,
            "complexity_analysis": complexity_results,
            "dependency_analysis": dependency_results,
            "semantic_analysis": semantic_results,
            "architecture_analysis": architecture_analysis,
            "health_score": health_score,
            "recommendations": recommendations
        }
