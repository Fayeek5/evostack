import os
import tempfile
import shutil
from git import Repo, GitCommandError


class RepositoryIngestionService:
    def __init__(self, clone_path):
        self.clone_path = clone_path

    def clone_repository(self, repo_url, branch="master"):
        try:
            temp_dir = tempfile.gettempdir()

            clone_path = os.path.join(temp_dir, self.clone_path)

            if os.path.exists(clone_path):
                shutil.rmtree(clone_path)

            Repo.clone_from(
                repo_url,
                clone_path,
                branch=branch
            )

            return clone_path

        except GitCommandError as e:
            raise Exception(
                f"Failed to clone repository from {repo_url}: {e}"
            )
