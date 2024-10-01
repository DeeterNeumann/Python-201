# Write a script that takes a sentence from the user and returns:

# the number of lower case letters
# the number of uppercase letters
# the number of punctuations characters
# the total number of characters
# Use a dictionary to store the count of each of the above.

# Note: ignore all spaces.

# Example input:

# I love to work with dictionaries!

# Example output:

# Upper case: 1
# Lower case: 26
# Punctuation: 1
# Total chars: 28

sentence = input("Type a sentence: ")

sentence_analysis = {}

for char in sentence:
    if char.isupper():
        sentence_analysis["Upper case"] = sentence_analysis.get("Upper case", 0) + 1
    if char.islower():
        sentence_analysis["Lower case"] = sentence_analysis.get("Lower case", 0) + 1
    if not char.isalnum() and not char.isspace():
        sentence_analysis["Punctuation"] = sentence_analysis.get("Punctuation", 0) + 1
    sentence_analysis["Total chars"] = len(sentence.replace(" ", ""))

order = ["Upper case", "Lower case", "Punctuation", "Total chars"]

for title in order:
    print(f"{title}: {sentence_analysis.get(title, 0)}")