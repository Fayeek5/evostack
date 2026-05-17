import requests


def fetch_github_metadata(repo_url):

    try:

        repo_path = (
            repo_url
            .replace(
                "https://github.com/",
                ""
            )
            .strip("/")
        )

        api_url = (
            f"https://api.github.com/repos/"
            f"{repo_path}"
        )

        response = requests.get(api_url)

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

            "created_at": data.get(
                "created_at",
                ""
            ),

            "updated_at": data.get(
                "updated_at",
                ""
            )
        }

    except Exception:

        return {

            "stars": 0,

            "forks": 0,

            "open_issues": 0,

            "watchers": 0,

            "language": "Unknown",

            "created_at": "",

            "updated_at": ""
        }
