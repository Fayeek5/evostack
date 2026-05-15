from pathlib import Path
from radon.complexity import cc_visit

SUPPORTED_EXTENSIONS = [".py"]


def analyze_complexity(repo_path: str):
    results = []
    total_complexity = 0
    total_blocks = 0

    repo = Path(repo_path)

    for file_path in repo.rglob("*"):
        if file_path.suffix not in SUPPORTED_EXTENSIONS:
            continue

        try:
            code = file_path.read_text(encoding="utf-8")

            complexity_blocks = cc_visit(code)

            file_complexity = 0

            for block in complexity_blocks:
                file_complexity += block.complexity
                total_complexity += block.complexity
                total_blocks += 1

            results.append({
                "file": str(file_path.relative_to(repo)),
                "complexity": file_complexity,
                "functions": len(complexity_blocks)
            })

        except Exception as e:
            print(f"Error analyzing {file_path}: {e}")

    average_complexity = (
        total_complexity / total_blocks
        if total_blocks > 0
        else 0
    )

    high_risk_files = sorted(
        [file for file in results if file["complexity"] > 20],
        key=lambda x: x["complexity"],
        reverse=True
    )

    return {
        "average_complexity": round(average_complexity, 2),
        "high_risk_count": len(high_risk_files),
        "top_risky_files": high_risk_files[:10]
    }
