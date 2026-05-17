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

from app.services.maturity_engine import (
    calculate_maturity
)

from app.services.summary_engine import (
    generate_repository_summary
)

from app.services.github_metadata import (
    fetch_github_metadata
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
            semantic_data)

        maturity = calculate_maturity(
            overall_score
        )

        executive_summary = (
            generate_repository_summary(
                semantic_data,
                score_data
            )
        )

        github_metadata = (
            fetch_github_metadata(
                repo_url
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
                ),

                "maturity": maturity
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

            "executive_summary": executive_summary,

            "github_metadata": github_metadata
        }

        save_analysis_snapshot(
            result
        )

        return result

    def get_history(self, repo_url: str):

        from app.database.database import SessionLocal
        from app.database.models import RepositoryAnalysis

        db = SessionLocal()

        history = (
            db.query(RepositoryAnalysis)
            .filter(
                RepositoryAnalysis.repository_url == repo_url
            )
            .order_by(
                RepositoryAnalysis.created_at.desc()
            )
            .all()
        )

        db.close()

        return [
            {
                "score": item.overall_score,
                "language": item.primary_language,
                "created_at": str(item.created_at)
            }
            for item in history
        ]


    def get_trends(self, repo_url: str):

        history = self.get_history(repo_url)

        if len(history) < 2:

            return {
                "trend": "stable",
                "latest_score": (
                    history[0]["score"]
                    if history
                    else 0
                ),
                "score_delta": 0,
                "historical_analyses": len(history)
            }

        latest = history[0]["score"]
        previous = history[1]["score"]

        delta = round(latest - previous, 1)

        return {
            "trend": (
                "improving"
                if delta > 0
                else "declining"
                if delta < 0
                else "stable"
            ),
            "latest_score": latest,
            "score_delta": delta,
            "historical_analyses": len(history)
        }


    def get_latest(self):

        from app.database.database import SessionLocal
        from app.database.models import RepositoryAnalysis

        db = SessionLocal()

        latest = (
            db.query(RepositoryAnalysis)
            .order_by(
                RepositoryAnalysis.created_at.desc()
            )
            .first()
        )

        db.close()

        if not latest:
            return {}

        return {
            "repository": latest.repository_url,
            "score": latest.overall_score,
            "language": latest.primary_language
        }


    def get_repositories(self):

        from app.database.database import SessionLocal
        from app.database.models import RepositoryAnalysis

        db = SessionLocal()

        repositories = (
            db.query(
                RepositoryAnalysis.repository_url
            )
            .distinct()
            .all()
        )

        db.close()

        return [r[0] for r in repositories]

    def get_history(self, repo_url: str):

        from app.database.database import SessionLocal
        from app.database.models import RepositoryAnalysis

        db = SessionLocal()

        history = (
            db.query(RepositoryAnalysis)
            .filter(
                RepositoryAnalysis.repository_url == repo_url
            )
            .order_by(
                RepositoryAnalysis.created_at.desc()
            )
            .all()
        )

        db.close()

        return [
            {
                "score": item.overall_score,
                "language": item.primary_language,
                "created_at": str(item.created_at)
            }
            for item in history
        ]


    def get_trends(self, repo_url: str):

        history = self.get_history(repo_url)

        if len(history) < 2:

            return {
                "trend": "stable",
                "latest_score": (
                    history[0]["score"]
                    if history
                    else 0
                ),
                "score_delta": 0,
                "historical_analyses": len(history)
            }

        latest = history[0]["score"]
        previous = history[1]["score"]

        delta = round(latest - previous, 1)

        return {
            "trend": (
                "improving"
                if delta > 0
                else "declining"
                if delta < 0
                else "stable"
            ),
            "latest_score": latest,
            "score_delta": delta,
            "historical_analyses": len(history)
        }


    def get_latest(self):

        from app.database.database import SessionLocal
        from app.database.models import RepositoryAnalysis

        db = SessionLocal()

        latest = (
            db.query(RepositoryAnalysis)
            .order_by(
                RepositoryAnalysis.created_at.desc()
            )
            .first()
        )

        db.close()

        if not latest:
            return {}

        return {
            "repository": latest.repository_url,
            "score": latest.overall_score,
            "language": latest.primary_language
        }


    def get_repositories(self):

        from app.database.database import SessionLocal
        from app.database.models import RepositoryAnalysis

        db = SessionLocal()

        repositories = (
            db.query(
                RepositoryAnalysis.repository_url
            )
            .distinct()
            .all()
        )

        db.close()

        return [r[0] for r in repositories]
