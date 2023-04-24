import csv


csv_data = []
with open("data/topics/topics.csv", "r") as csvfile:
    reader = csv.DictReader(csvfile)
    csv_data = [row for row in reader]
