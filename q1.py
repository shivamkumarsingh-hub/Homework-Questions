import csv
from collections import defaultdict

top_scores = defaultdict(lambda: {"name": "", "marks": -1})

with open("marks.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        subject = row["subject"]
        marks = int(row["marks"])
        if marks > top_scores[subject]["marks"]:
            top_scores[subject] = {"name": row["name"], "marks": marks}

for subject, info in top_scores.items():
    print(f"Subject: {subject} -> {info['name']} ({info['marks']})") 