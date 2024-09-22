# Convert a string to a tuple and print out the result.
# What do you see?
# What happens if you try to iterate over your tuple of characters?
# Do you notice any difference to iterating over the string?

string = "codingnomads"

string_tup = tuple(string)

print(string_tup)

for i in string_tup:
    print(i)