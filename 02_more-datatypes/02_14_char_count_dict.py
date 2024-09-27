# Write a script that takes a text input from the user
# and creates a dictionary that maps the letters in the string
# to the number of times they occur. For example:
#
# user_input = "hello"
# result = {"h": 1, "e": 1, "l": 2, "o": 1}

word = input("Please type a word here: ")

splits = list()

letter_count = {}

for char in word:
    splits.append(char)
    if char not in letter_count:
        letter_count[char] = 1
    else:
        letter_count[char] += 1

print(letter_count)


# letter_count = {}

# iterate over word
# add individual character as dict key in letter_count
# count the number of times each character appears in the word and add as dictionary value to respective character

# for char in word:
#     letter_count[] = char

# print(letter_count)