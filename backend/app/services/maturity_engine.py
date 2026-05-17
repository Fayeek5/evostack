def calculate_maturity(score: float):

    if score >= 95:

        return {
            "grade": "A+",
            "label": "Enterprise Ready"
        }

    elif score >= 85:

        return {
            "grade": "A",
            "label": "Production Mature"
        }

    elif score >= 70:

        return {
            "grade": "B",
            "label": "Scalable Foundation"
        }

    elif score >= 50:

        return {
            "grade": "C",
            "label": "Growing Architecture"
        }

    return {
        "grade": "D",
        "label": "Early Engineering"
    }
