# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"

string_tup = tuple(string)

print(string_tup)

string_list = list(string_tup)

print(string_list)

string_list[0] = "k"

print(string_list)

string_tup2 = tuple(string_list)

print(string_tup2)