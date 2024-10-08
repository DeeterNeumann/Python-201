# Write a program that reads in `words.txt` and prints only the words
# that have more than 20 characters (not counting whitespace).

words = []

with open("words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

more_than_20 = []

for w in words:
    if len(w) > 20:
        more_than_20.append(w)

with open("words.txt", "w") as fout:
    fout.write("\n".join(more_than_20))