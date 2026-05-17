import os
import requests


def fetch_github_metadata(repo_url: str):

    repo_path = (
        repo_url
        .replace("https://github.com/", "")
        .strip("/")
    )

    api_url = (
        f"https://api.github.com/repos/{repo_path}"
    )

    headers = {}

    token = os.getenv(
        "GITHUB_TOKEN"
    )

    if token:

        headers["Authorization"] = (
            f"Bearer {token}"
        )

    response = requests.get(
        api_url,
        headers=headers
    )

    if response.status_code != 200:

        return {

            "stars": 0,
            "forks": 0,
            "open_issues": 0,
            "watchers": 0,
            "language": "Unknown",
            "last_activity": "Unknown"
        }

    data = response.json()

    return {

        "stars": data.get(
            "stargazers_count",
            0
        ),

        "forks": data.get(
            "forks_count",
            0
        ),

        "open_issues": data.get(
            "open_issues_count",
            0
        ),

        "watchers": data.get(
            "subscribers_count",
            0
        ),

        "language": data.get(
            "language",
            "Unknown"
        ),

        "last_activity": data.get(
            "updated_at",
            "Unknown"
        )[:10]
    }
