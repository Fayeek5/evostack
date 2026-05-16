from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.services.evolution_pipeline import EvolutionPipeline

app = FastAPI(title="EvoStack API")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health():
    return {
        "status": "healthy",
        "service": "EvoStack API"
    }


@app.post("/analyze")
def analyze_repository(repo_url: str):

    pipeline = EvolutionPipeline()

    result = pipeline.run(repo_url)

    return result
