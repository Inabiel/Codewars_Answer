def openOrSenior(data):
    return [
        "Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data
    ]

