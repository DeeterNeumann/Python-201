# Write a script that takes in a string from the user.
# Using the `split()` method, create a list of all the words in the string
# and print back the most common word in the text.s

sentence = input("Type a sentence here: ")

broken_sentence = sentence.lower().split()

broken_sentence.sort()

mode = broken_sentence[0]

current_max = 0

word_count = 0

last_word = ""

for word in broken_sentence:
    word_count += 1
    if word_count >= current_max:
        current_max = word_count
        mode = last_word
    if word != last_word:
        word_count = 0
    last_word = word

print(broken_sentence)
print(mode)