# Take in a few numbers from the user and place them in a list.
# If you want, you can instead use the provided randomly generated
# list called `randlist` to simulate the user input.
#
# Find the largest number in the list and print the result.
# Calculate the product of all of the numbers in the list.

from resources import randlist

print(randlist)

#sort random list
randlist.sort()

#print largest number
print(randlist[-1])

#for loop for finding largest number (use of none for maximum variable?)
maximum = randlist[0]

for i in randlist:
    if i > maximum:
        maximum = i

print(maximum)

product = 1 #accumulator

for i in randlist:
    product *= i

print(product)
    

    

