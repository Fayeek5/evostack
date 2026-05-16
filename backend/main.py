from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.app.services.evolution_pipeline import EvolutionPipeline

app = FastAPI()


# VERY IMPORTANT
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {
        "status": "healthy",
        "service": "EvoStack API"
    }


@app.post("/analyze")
async def analyze(repo_url: str):

    pipeline = EvolutionPipeline()

    result = pipeline.run(repo_url)

    return result
