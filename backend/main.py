from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.app.services.evolution_pipeline import EvolutionPipeline
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/analyze")
async def analyze(repo_url: str):
    try:
        temp_dir = "temp_repo_dir"

        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)

        pipeline = EvolutionPipeline(temp_dir)

        analysis_report = await pipeline.run(repo_url)

        return analysis_report

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
