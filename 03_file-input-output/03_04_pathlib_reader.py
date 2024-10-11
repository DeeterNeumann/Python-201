# Refactor your file counter script to use `pathlib` also for
# reading and writing to your CSV file. Make sure to handle the
# path in a way so that you can run the script from anywhere.

import pathlib
import csv

file_counter = {"": 0, ".csv": 0, ".md": 0, ".png": 0}

directory_to_count = pathlib.Path("/Users/drneu/Documents/CodingNomads/Python 201")

for file in directory_to_count.iterdir():
    if file.suffix in file_counter:
        file_counter[file.suffix] += 1

drneu = pathlib.Path("/Users/drneu/Documents/CodingNomads/Python 201/filecounts.csv")

with drneu.open(mode = "a", newline = "") as csvfile:
    countwriter = csv.writer(csvfile)
    countwriter.writerow(["Type", "Count"])
    for ext, count in file_counter.items():
        countwriter.writerow([ext, count])

print(file_counter)