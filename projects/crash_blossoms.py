
def titlecase(sentence):
    headline = []
    for word in sentence.split():
        capitalize = word.capitalize()
        headline.append(capitalize)
    return " ".join(headline)

user_input = input("Enter your headline (type 'exit' to quit): ")

while user_input != "exit":
    crash_blossom = titlecase(user_input)
    print(crash_blossom)
    user_input = input("Enter your headline (type 'exit' to quit): ")