from backend.app.core.repo_manager import clone_repository
from backend.app.intelligence.complexity_engine import analyze_complexity
from backend.app.intelligence.dependency_graph import build_dependency_graph
from backend.app.intelligence.semantic_engine import analyze_semantics
from backend.app.intelligence.architecture_engine import detect_architecture
from backend.app.intelligence.health_engine import calculate_health_score


class EvolutionPipeline:
    def __init__(self):
        pass

    def run(self, repo_url: str):
        cloned_repo_path = clone_repository(repo_url)

        architecture_analysis = detect_architecture(cloned_repo_path)

        complexity_analysis = analyze_complexity(cloned_repo_path)

        dependency_analysis = build_dependency_graph(cloned_repo_path)

        semantic_analysis = analyze_semantics(cloned_repo_path)

        analysis_results = {
            "architecture": architecture_analysis,
            "complexity": complexity_analysis,
            "dependencies": dependency_analysis,
            "semantics": semantic_analysis,
        }

        health_score = calculate_health_score(
            analysis_results
        )

        return {
            "status": "success",
            "repository": repo_url,
            "health_score": health_score,
            "analysis": analysis_results,
        }
