import sys

total_score = 0.0
total_credit = 0.0

score = {
    "A+": 4.5, "A0": 4.0,
    "B+": 3.5, "B0": 3.0,
    "C+": 2.5, "C0": 2.0,
    "D+": 1.5, "D0": 1.0,
    "F": 0.0
}

for line in sys.stdin:
    _, credit, grade = line.split()
    credit = float(credit)

    if grade == "P":
        continue

    total_score += credit * score[grade]
    total_credit += credit

print(total_score / total_credit)
