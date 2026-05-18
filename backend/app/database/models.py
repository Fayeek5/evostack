from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    JSON
)

from datetime import datetime

from backend.app.database.database import Base


class RepositoryAnalysis(Base):

    __tablename__ = "repository_analyses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    repository_url = Column(
        String,
        nullable=False
    )

    overall_score = Column(
        Float,
        nullable=False
    )

    primary_language = Column(
        String
    )

    framework_stack = Column(
        JSON
    )

    hotspot_data = Column(
        JSON
    )

    file_metrics = Column(
        JSON
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
