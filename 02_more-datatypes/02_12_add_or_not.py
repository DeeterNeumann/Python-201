# MEMORY GAME WITH SETS
# Continuously collect number input from a user with a `while` loop.
# Confirm that the input can be converted to an integer,
# then add it to a Python `set()`.
# If the element was already in the set, notify the user that their
# their input is a duplicate and deduct a point.
# If the user loses 5 points, quit the program.
# They win if they manage to create a set that has more than 10 items.

points = 5

int_set = set()

# while points > 0:
#     if len(int_set) == 0:
#         num_entered = input("Let's play memory! Please enter a number (e.g., 1, 4, 6, 14): ")
#         try:
#             num_entered = int(num_entered)
#         except ValueError:
#             print("Please enter your number as a digit")
#         int_set.add(num_entered)
#     else:
#         num_entered = input("Please enter another number (e.g., 1, 4, 6, 14): ")
#         try:
#             num_entered = int(num_entered)
#         except ValueError:
#             print("Please enter your number as a digit")
#         if num_entered in int_set:
#             print("The number entered is a duplicate. You lose a point.")
#             points -= 1
#         else:
#             int_set.add(num_entered)
#     if len(int_set) > 10:
#         print("Congrats! You created a set that contains more than 10 items before losing 5 points")
#         print(int_set)


num_entered = input("Let's play memory! Please enter a number (e.g., 1, 4, 6, 14): ")

while points > 0 and len(int_set) <= 10:
    try:
        num_entered = int(num_entered)
        if num_entered in int_set:
            print("The number entered is a duplicate. You lose a point.")
            points -= 1
        else:
            int_set.add(num_entered)
    except ValueError:
        print("Please enter your number as a digit")
    if len(int_set) > 10:
        print("Congrats! You created a set that contains more than 10 items before losing 5 points")
        print(int_set)
    elif points > 0:
        num_entered = input("Please enter another number (e.g., 1, 4, 6, 14): ")
    else:
        print("Better have your memory checked. Game over")