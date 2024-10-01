# Write code that creates a list of all unique values in a list.
# For example:
#
# list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
# unique_list = [55, 'hi', 4, 13]

list_of_interest = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]

unique_or_not = {}

# last_value = ""

for value in list_of_interest:
    if value in unique_or_not:
        unique_or_not[value] += 1
    else:
        unique_or_not[value] = 1

unique_list = []

for value in list_of_interest:
    if unique_or_not[value] == 1:
        unique_list.append(value)

print(unique_list)