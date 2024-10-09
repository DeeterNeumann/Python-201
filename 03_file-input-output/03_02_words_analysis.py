# Read in all the words from the `words.txt` file.
# Then find and print:

# 1. The shortest word (if there is a tie, print all)
# 2. The longest word (if there is a tie, print all)
# 3. The total number of words in the file.

words = []

with open("all_words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

# print(words)

min_len = len(min(words, key = len))

shortest = []

max_len = len(max(words, key = len))

longest = []

count = 0

for w in words:
    if len(w) == min_len:
        shortest.append(w)
    elif len(w) == max_len:
        longest.append(w)
    count += 1

print("The list of shortest words: ", shortest)

print("The list of longest words: ", longest)

print("Total number of words: ", count)