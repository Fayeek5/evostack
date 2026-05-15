import os


class RepositoryAnalyzer:
    def __init__(self, repo_path):
        self.repo_path = repo_path

    async def analyze(self):
        issues = []
        total_files = 0
        todo_count = 0

        for root, _, files in os.walk(self.repo_path):
            for file in files:
                total_files += 1

                filepath = os.path.join(root, file)

                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        content = f.read()

                        if "TODO" in content:
                            todo_count += 1
                            issues.append(
                                f"TODO detected in {file}"
                            )

                        if "FIXME" in content:
                            issues.append(
                                f"FIXME detected in {file}"
                            )

                except:
                    pass

        complexity_score = max(
            1,
            100 - (todo_count * 5)
        )

        return {
            "repository": self.repo_path,
            "total_files": total_files,
            "complexity_score": complexity_score,
            "issues": issues[:20]
        }
