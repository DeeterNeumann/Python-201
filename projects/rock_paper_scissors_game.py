# Code a game of rock paper scissors.

# Instructions
# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner

# def get_hand(hand):
#     # 0 = scissor, 1 = rock, 2 = paper

#     # for example if the variable hand is 0, it should return the string "scissor"
#     pass

#rock_paper_scissors game

import random

def get_hand(number_zero_to_two):
    if number_zero_to_two == 0:
        return "scissor"
    elif number_zero_to_two == 1:
        return "rock"
    elif number_zero_to_two == 2:
        return "paper"
    else:
        return "Please enter a number 0, 1, or 2."

def determine_winner(player, computer):
    if player == computer:
        return "You tied"
    if (player == 1 and computer == 0) or (player == 2 and computer == 1) or (player == 0 and computer == 2):
        return "You win!"
    else:
        return "You lose!"

# rock (1) beats scissors (0)
# scissors (0) beats paper (2)
# paper (2) beats rock (1)

comp_shoot = random.randint(0,2)

shoot = input("Enter a number 0 through 2 to indicate your throw (0 = scissor, 1 = rock, 2 = paper): ")

if not shoot.isdigit():
    print("You entered a character. That's invalid.")
    quit()

shoot = int(shoot)

if shoot >= 0 and shoot <=2:
    print(f"The player threw: {get_hand(shoot)}")
    print(f"The computer threw: {get_hand(comp_shoot)}")
    print(determine_winner(shoot, comp_shoot))
else:
    print("Enter a number 0, 1, or 2")



# if shoot.isdigit() and int(shoot) >= 0 and int(shoot) <=2:
#     print(f"The player threw: {get_hand(int(shoot))}")
#     print(f"The computer threw: {get_hand(comp_shoot)}")
#     print(determine_winner(int(shoot), comp_shoot))
# else:
#     print("Enter a number 0, 1, or 2")




