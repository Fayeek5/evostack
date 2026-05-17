from app.database.database import (
    SessionLocal
)

from app.database.models import (
    RepositoryAnalysis
)


def save_analysis_snapshot(result):

    db = SessionLocal()

    try:

        snapshot = RepositoryAnalysis(

            repository_url=result.get(
                "repository",
                ""
            ),

            overall_score=result.get(
                "health_score",
                {}
            ).get(
                "overall",
                0
            ),

            primary_language=result.get(
                "analysis",
                {}
            ).get(
                "architecture",
                {}
            ).get(
                "primary_language",
                "Unknown"
            ),

            framework_stack=result.get(
                "analysis",
                {}
            ).get(
                "architecture",
                {}
            ).get(
                "frameworks",
                []
            ),

            hotspot_data=result.get(
                "analysis",
                {}
            ).get(
                "semantics",
                {}
            ).get(
                "top_risky_files",
                []
            ),

            file_metrics=result.get(
                "analysis",
                {}
            ).get(
                "semantics",
                {}
            ).get(
                "file_metrics",
                []
            )
        )

        db.add(snapshot)

        db.commit()

        print("SNAPSHOT SAVED SUCCESSFULLY")

    except Exception as e:

        db.rollback()

        print(f"PERSISTENCE ERROR: {str(e)}")

    finally:

        db.close()
