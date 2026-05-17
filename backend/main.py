from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.recommendation_engine import generate_recommendations
from app.services.evolution_pipeline import EvolutionPipeline

from app.database.init_db import (
    initialize_database
)

from app.database.history_service import (
    get_repository_history,
    get_latest_snapshot,
    get_all_repositories
)

from app.database.trend_service import (
    calculate_repository_trends
)

app = FastAPI()

initialize_database()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = EvolutionPipeline()


@app.get("/")
def health():

    return {
        "status": "healthy",
        "service": "EvoStack API"
    }


@app.post("/analyze")
def analyze(repo_url: str):

    try:

        result = pipeline.analyze_repository(repo_url)

        return result

    except Exception as e:

    return {
            "status": "error",
            "message": str(e)
        }


@app.get("/history")
def history(repo_url: str):

    return get_repository_history(
        repo_url
    )


@app.get("/latest")
def latest(repo_url: str):

    return get_latest_snapshot(
        repo_url
    )


@app.get("/repositories")
def repositories():

    return get_all_repositories()


@app.get("/trends")
def trends(repo_url: str):

    return calculate_repository_trends(
        repo_url
    )
