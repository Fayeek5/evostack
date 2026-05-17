from sqlalchemy import desc

from backend.app.database.database import (
    SessionLocal
)

from backend.app.database.models import (
    RepositoryAnalysis
)


def get_repository_history(
    repo_url: str
):

    db = SessionLocal()

    try:

        rows = (
            db.query(RepositoryAnalysis)
            .filter(
                RepositoryAnalysis.repository_url == repo_url
            )
            .order_by(
                desc(RepositoryAnalysis.created_at)
            )
            .all()
        )

        return [

            {
                "id": row.id,
                "repository_url": row.repository_url,
                "overall_score": row.overall_score,
                "primary_language": row.primary_language,
                "framework_stack": row.framework_stack,
                "created_at": str(row.created_at)
            }

            for row in rows
        ]

    finally:

        db.close()


def get_latest_snapshot(
    repo_url: str
):

    db = SessionLocal()

    try:

        row = (
            db.query(RepositoryAnalysis)
            .filter(
                RepositoryAnalysis.repository_url == repo_url
            )
            .order_by(
                desc(RepositoryAnalysis.created_at)
            )
            .first()
        )

        if not row:
            return None

        return {

            "id": row.id,
            "repository_url": row.repository_url,
            "overall_score": row.overall_score,
            "primary_language": row.primary_language,
            "framework_stack": row.framework_stack,
            "created_at": str(row.created_at)
        }

    finally:

        db.close()


def get_all_repositories():

    db = SessionLocal()

    try:

        rows = (
            db.query(
                RepositoryAnalysis.repository_url
            )
            .distinct()
            .all()
        )

        return [
            row[0]
            for row in rows
        ]

    finally:

        db.close()
