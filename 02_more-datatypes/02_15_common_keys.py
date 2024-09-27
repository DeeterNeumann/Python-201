# Write a script that takes the following two dictionaries
# and creates a new dictionary by combining the common keys
# and adding the values of duplicate keys together.
# Use `for` loops to iterate over these dictionaries
# to accomplish this task.
#
# Example output:
# result = {"a": 3, "b": 2, "c": 7 , "d": 2}

dict_1 = {"a": 1, "b": 2, "c": 3}
dict_2 = {"a": 2, "c": 4 , "d": 2}

combined_dict = {}

for letter in dict_1:
    if letter in dict_2:
        combined_dict[letter] = dict_1[letter] + dict_2[letter]
    elif letter not in dict_2:
        combined_dict[letter] = dict_1[letter]
    else:
        combined_dict[letter] = dict_2[letter]

for letter in dict_2:
    if letter in combined_dict:
        continue
    if letter not in combined_dict:
        combined_dict[letter] = dict_2[letter]

print(combined_dict)