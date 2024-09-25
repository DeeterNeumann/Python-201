# The import below gives you a new random list of numbers,
# called `randlist`, every time you run the script.
#
# Write a script that takes this list of numbers and:
#     - sorts the numbers
#     - stores the numbers in tuples of two in a new list
#     - prints each tuple
#
# If the list has an odd number of items,
# add the last item to a tuple together with the number `0`.
#
# Note: This lab might be challenging! Make sure to discuss it 
# with your mentor or chat about it on our forum.

from resources import randlist

print(randlist)

# Write your code below here

randlist.sort() #.sort doesn't return anything

print(randlist)

sorted = randlist

if len(sorted) % 2 != 0:
    sorted.append(0)

tuples_of_two = []

pair = []

for index in range(0, len(sorted), 2):
    pair = sorted[index:index+2]
    # if len(pair) != 2:
    #     pair.append(0)
    pair = tuple(pair)
    tuples_of_two.append(pair)

print(tuples_of_two)