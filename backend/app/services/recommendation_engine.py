def generate_recommendations(
    semantic_data,
    score_data
):

    recommendations = []

    try:

        risky_files = semantic_data.get(
            "top_risky_files",
            []
        )

        imports = semantic_data.get(
            "imports",
            0
        )

        has_tests = semantic_data.get(
            "has_tests",
            False
        )

        scanned_files = semantic_data.get(
            "scanned_files",
            0
        )

        # High risk orchestration files

        if risky_files and len(risky_files) > 0:

            top_file = risky_files[0]

            risk_score = top_file.get(
                "risk_score",
                0
            )

            if risk_score > 20:

                recommendations.append({

                    "type": "warning",

                    "title": (
                        "Large orchestration layer detected"
                    ),

                    "description": (

                        f"{top_file.get('file', 'Unknown file')} "

                        "has elevated engineering complexity "
                        "and should be modularized."
                    )
                })

        # Testing maturity

        if not has_tests:

            recommendations.append({

                "type": "warning",

                "title": (
                    "Testing maturity is weak"
                ),

                "description": (

                    "No significant test coverage "
                    "was detected in the repository."
                )
            })

        # Dependency concentration

        if imports > 40:

            recommendations.append({

                "type": "warning",

                "title": (
                    "High dependency concentration"
                ),

                "description": (

                    "The repository exhibits "
                    "heavy dependency usage."
                )
            })

        # Large repository signal

        if scanned_files > 120:

            recommendations.append({

                "type": "info",

                "title": (
                    "Large-scale repository detected"
                ),

                "description": (

                    "Consider introducing "
                    "domain-driven modularization."
                )
            })

        # Maintainability

        if score_data.get(
            "maintainability",
            0
        ) >= 80:

            recommendations.append({

                "type": "success",

                "title": (
                    "Architecture appears maintainable"
                ),

                "description": (

                    "The repository demonstrates "
                    "healthy maintainability patterns."
                )
            })

        # Complexity

        if score_data.get(
            "complexity",
            100
        ) < 70:

            recommendations.append({

                "type": "warning",

                "title": (
                    "Complexity risk detected"
                ),

                "description": (

                    "Several files exhibit "
                    "elevated complexity characteristics."
                )
            })

    except Exception as e:

        recommendations.append({

            "type": "warning",

            "title": "Recommendation engine warning",

            "description": str(e)
        })

    return recommendations
