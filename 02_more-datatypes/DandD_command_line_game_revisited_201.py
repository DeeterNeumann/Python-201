# Here are the tasks that you'll code up for this project. You'll read them below in a list form, and as a first step, you can again copy that content over into a new Python file as pseudocode:

# Save the user input options you allow, e.g., in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items. (dict.clear())
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

import requests
from pprint import pprint

player_inputs = {"left", "right", "yes", "no", "stay", "return", "fight", "safety"}
direction_inputs = {"left", "right", "straight", "trap"}

inventory = {"weapons" : [], "potions" : {"health" : 0, "death": 0}, "food": {}}

def player_choice(message, *choices):
    current_choice = ""
    while not current_choice in choices:
        current_choice = input(message)
        if not current_choice in choices:
            print("wrong choice")
    return current_choice

def name_generator():
    name = input("Who has the pleasure of playing this game? Please provide your name: \n")
    if len(name) >=2 and len(name) <=40:
        minimum_length = len(name)
        maximum_length = len(name)
        name_url = f"https://uzby.com/api.php?min={minimum_length}&max={maximum_length}"
        response = requests.get(name_url)
        if response.status_code == 200:
            game_name = response.text
            print(f"Welcome {name}, to the command-line world of Dungeons and Dragons! For this game, you have been assigned the name: {game_name}.\n")
        else:
            print(f"Welcome {name}, to the command-line world of Dungeons and Dragons!\n")
    else:
        print("The name you enter must be between 2 and 40 characters long.")
        quit()

def joker():
    joke_url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit&type=single"
    response = requests.get(joke_url)
    joke = response.json()
    print(f"You have awakened the prisoner, and in a strained voice, they mutter, '{joke['joke']}.'")

# Ask the player for their name.
# name = input("Who has the pleasure of playing this game? Please provide your name: \n")
name_generator()

# Display a message that greets them and introduces them to the game world.
# print(f"Welcome {name}, to the command-line world of Dungeons and Dragons!\n")

#room assignment: "c" = corridor; "l" = left (empty) room; "r" = right (dragon) room; "m" = middle (potions) room; "t" = trap door (joker) 
player_pos = "c"

#possess sword?
sword = False

#dragon status
dragon_dead = False

while dragon_dead == False:
## Present them with a choice between two doors.
    player_pos = "c"
    while player_pos == "c":
        door_choice = player_choice("As you enter into the dungeon and navigate its dark corridor,\nyou come accross four doors. Which will you enter? 'straight', 'left', 'right', or 'trap' door: ", *direction_inputs)
        ## If they choose the left door, they'll see an empty room
        if door_choice == "left":
            player_pos = "l"
            print("You have entered into a dark and seemingly empty room.\n")
        # If they choose the middle door, enter potion master's room 
        if door_choice == "straight":
            player_pos = "m"
            print("You entered the potion master's room.")
        ## If they choose the right door, then they encounter a dragon.
        if door_choice == "right":
            player_pos = "r"
            print("You have entered into the lair of an ornery dragon!\n")
        if door_choice == "trap":
            player_pos = "t"
    while player_pos == "l":
        ## When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword. They can choose to take it or leave it.
        if player_pos == "l":
            look_around = input("Do you want to further explore the seemingly empty room? yes or no: \n")
            if look_around == "yes":
                take_sword = input("You have found a sword! Do you wish to take the sword? yes or no: \n")
                if take_sword == "yes":
                    inventory["weapons"].append("sword")
                    sword = True
                else:
                    sword = False
            left_to_hall = input("Do you want to remain in this room or return to the corridor? Please enter stay or return: \n")
            if left_to_hall == "return":
                player_pos = "c"
            else:
                print("Well, this is fun.\n")
                continue
    while player_pos == "m":
        pick_up_potion = input("There are racks filled with potions. Would you like to take one? yes or no? \n")
        if pick_up_potion == "yes":
            inventory["potions"]["health"] += 1
            print("You have obtained a health potion!")
        middle_to_hall = input("Do you want to reamin in this room or return to the corridor? Enter stay or return: ")
        if middle_to_hall == "return":
            player_pos = "c"
        else:
            print("Well, this is fun")
            continue      
    while player_pos == "r":
        ## When encountering the dragon, they have the choice to fight it.
        if player_pos == "r":
            fight_safety = input("Do you wish to fight the dragon or return to the safety of the corridor? Enter fight or safety: \n")
            has_sword = "sword" in inventory["weapons"]
            if fight_safety == "fight" and has_sword:
                dragon_dead = True
                break
        # If they don't have the sword, then they will be eaten by the dragon and lose the game
            elif fight_safety == "fight":
                inventory.clear()
                print("You made a poor decision. Fighting the dragon without a weapon resulted in your death. You lose.\n")
                quit()
            elif fight_safety == "safety":
                player_pos = "c"
                print("You safely regressed back to the corridor and out of danger from the dragon.\n")
    while player_pos == "t":
        wake_up = input("You slipped down the trap door beneath your feet and come across a weak and starved individual sleeping. Do you wish to wake them? yes or no: ")
        if wake_up == 'yes':
            joker()
            up_to_corridor = input('Well there is clearly nothing beneficial down here. Do you wish to return to the corridor above? yes or no: ')
            if up_to_corridor == 'yes':
                player_pos = 'c'
            else:
                print('Well, this is fun')       
        elif wake_up == 'no':
            up_to_corridor = input('Do you wish to return to the corridor above? yes or no: ')
            if up_to_corridor == 'yes':
                player_pos = 'c'
            else:
                print('Well, this is fun')

print("You found the sword and chose to fight the dragon, which you successfully slayed. Congratulations - you win!")


# functions checking inputs available in set



