# Write a script that reads in the contents of `words.txt`
# and writes the contents in reverse to a new file `words_reverse.txt`.


words = []

with open("all_words.txt", "r") as fin:
    for word in fin.readlines():
        word = word.rstrip()
        words.append(word)

# print(words)

words.reverse() # why can't I assign this to a new variable? e.g., words_reversed = words.reverse()

# print(words)

with open("all_words_reverse.txt", "w+") as fout:
    fout.write("\n".join(words))