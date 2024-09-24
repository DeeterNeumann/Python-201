# Write a script that takes a string from the user
# and creates a list that contains a tuple for each word.
# For example:

# input = "hello world"
# result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

sentence = input("Type a sentence here: ")

splits = []

for word in sentence.split():
    word_split = tuple(word)
    splits.append(word_split)

print(splits)