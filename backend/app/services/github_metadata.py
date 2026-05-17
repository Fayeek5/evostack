import requests


def fetch_github_metadata(repo_url: str):

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
            f"https://api.github.com/repos/{repo_path}"
        )

        response = requests.get(
            api_url,
            headers={
                "Accept": "application/vnd.github+json",
                "User-Agent": "EvoStack"
            },
            timeout=10
        )

        if response.status_code != 200:

            print(
                "GITHUB API ERROR:",
                response.status_code,
                response.text
            )

            return {

                "stars": 0,
                "forks": 0,
                "open_issues": 0,
                "watchers": 0,
                "language": "Unknown",
                "last_activity": ""
            }

        data = response.json()

        return {

            "stars": int(
                data.get(
                    "stargazers_count",
                    0
                )
            ),

            "forks": int(
                data.get(
                    "forks_count",
                    0
                )
            ),

            "open_issues": int(
                data.get(
                    "open_issues_count",
                    0
                )
            ),

            "watchers": int(
                data.get(
                    "subscribers_count",
                    0
                )
            ),

            "language": data.get(
                "language",
                "Unknown"
            ),

            "last_activity": data.get(
                "updated_at",
                ""
            )[:10]
        }

    except Exception as e:

        print(
            "GITHUB METADATA FAILURE:",
            str(e)
        )

        return {

            "stars": 0,
            "forks": 0,
            "open_issues": 0,
            "watchers": 0,
            "language": "Unknown",
            "last_activity": ""
        }
