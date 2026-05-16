from git import Repo
from pathlib import Path
import shutil
import tempfile


def ingest_repository(repo_url: str):

    temp_dir = Path(tempfile.gettempdir()) / "temp_repo_dir"

    # cleanup old repo
    if temp_dir.exists():
        shutil.rmtree(temp_dir, ignore_errors=True)

    Repo.clone_from(
        repo_url,
        temp_dir
    )

    return {
        "repository_path": str(temp_dir)
    }
