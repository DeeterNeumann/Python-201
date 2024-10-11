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


# for filepath in drneu.iterdir():
#     if filepath.suffix not in file_counter:
#         file_counter[filepath.suffix] = []
#     file_counter[filepath.suffix].append(filepath)

# for file_type, file_list in file_counter.items():
#     if len(file_list) >= 5:
#         new_folder_path = drneu.joinpath(file_type)
#         new_folder_path.mkdir(exist_ok=True)
#         for file in file_list:
#             new_file_path = new_folder_path.joinpath(file.name)
#             file.replace(new_file_path)

# with open("all_words.txt", "r") as fin:
#     for word in fin.readlines():
#         word = word.rstrip()
#         words.append(word)

# # print(words)

# words.reverse() # why can't I assign this to a new variable? e.g., words_reversed = words.reverse()

# # print(words)

# with open("all_words_reverse.txt", "w+") as fout:
#     fout.write("\n".join(words))