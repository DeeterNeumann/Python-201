# Adapt your file counter script so that it records more different file types
# in your CSV file. Remember that the format of your output needs to be
# consistent across multiple runs of your script. This means you'll need to
# make a compromise and choose which file types you want to record beforehand.


import pathlib
import csv

file_counter = {"": 0, ".csv": 0, ".md": 0, ".png": 0, ".pdf": 0, ".doc": 0}

directory_to_count = pathlib.Path("/Users/drneu/Documents/CodingNomads/Python 201")

for file in directory_to_count.iterdir():
    if file.suffix in file_counter:
        file_counter[file.suffix] += 1

drneu = pathlib.Path("/Users/drneu/Documents/CodingNomads/Python 201/morefilecounts.csv")

with drneu.open(mode = "a", newline = "") as csvfile:
    countwriter = csv.writer(csvfile)
    countwriter.writerow(["Type", "Count"])
    for ext, count in file_counter.items():
        countwriter.writerow([ext, count])

print(file_counter)