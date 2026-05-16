import shutil
import tempfile
import subprocess


def clone_repository(repo_url: str):

    temp_dir = tempfile.mkdtemp()

    try:

        subprocess.run(
            [
                "git",
                "clone",
                "--depth",
                "1",
                repo_url,
                temp_dir
            ],
            check=True,
            capture_output=True,
            text=True
        )

        return temp_dir

    except Exception as e:

        shutil.rmtree(
            temp_dir,
            ignore_errors=True
        )

        raise Exception(
            f"Repository clone failed: {str(e)}"
        )
