import shutil
import tempfile
from git import Repo


class RepositoryIngestionService:
    def __init__(self):
        self.clone_path = tempfile.mkdtemp(prefix="evostack_repo_")

    def clone_repository(self, repo_url, branch=None):
        try:
            if branch:
                Repo.clone_from(
                    repo_url,
                    self.clone_path,
                    branch=branch
                )
            else:
                Repo.clone_from(
                    repo_url,
                    self.clone_path
                )

            return self.clone_path

        except Exception as e:
            raise Exception(
                f"Failed to clone repository from {repo_url}: {str(e)}"
            )

    def cleanup(self):
        shutil.rmtree(self.clone_path, ignore_errors=True)
