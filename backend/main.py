from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.services.evolution_pipeline import EvolutionPipeline

app = FastAPI(
    title="EvoStack API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

pipeline = EvolutionPipeline()


@app.get("/")
def root():
    return {
        "status": "healthy",
        "service": "EvoStack API"
    }


@app.post("/analyze")
def analyze(repo_url: str):

    result = pipeline.analyze_repository(repo_url)

    return result


@app.get("/history")
def history(repo_url: str):

    return pipeline.get_history(repo_url)


@app.get("/latest")
def latest():

    return pipeline.get_latest()


@app.get("/repositories")
def repositories():

    return pipeline.get_repositories()


@app.get("/trends")
def trends(repo_url: str):

    return pipeline.get_trends(repo_url)
