import time
import random

#Initialize Variables
villains = [
    "Pirate", "Troll", "Bandit", "Warlord",
    "Necromancer", "Sorcerer", "Assassin", "Dragon",
    "Goblin", "Vampire", "Demon", "Mercenary"
]
villain = random.choice(villains)

turns = 0
start = 0
end = 0
total_score = 0
visited = False

# This function handles the score if the score is a negative value
def score_handling():
    global total_score
    if total_score < 0:
        total_score = 0

# To pause printing for 2 seconds
def print_pause(text):
    time.sleep(2)
    print(text)

# To get the right choice from the user
def get_user_choice():
    while True:
        try:
            choice = int(input("Please choose 1 or 2: "))
            if choice in [1, 2]:
                return choice
            else:
                print("Please choose 1 or 2: ")
        except ValueError:
            print("Please choose 1 or 2: ")

#To Display the result
def display_result():
    print(f"Turns: {turns}")
    print(f"Score: {total_score}")

#calculate elapsed time
def calculate_elapsed_time():
    global end
    end = time.time()
    elapsed_time = end - start
    print(f"Elapsed Time: {elapsed_time:.2f} seconds")

# To restart the game
def restart():
    while True:
        score_handling()
        print(f"Your Score is : {total_score}")
        choice = input("Would you like to play again? (y/n)").lower()
        if choice == "y":
            print_pause("Excellent! Restarting the game ...")
            return main()
        elif choice == "n":
            print_pause("Thanks for playing! See you next time.")
            display_result()
            calculate_elapsed_time()
            break

# Script of Intro
def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty "
                "(but not very effective), magic wand.")

# What will happen in the house
def house():
    print_pause("You approach the door of the house.")
    print_pause(f"You are about to knock when the door opens "
                f"and out steps a {villain}.")
    print_pause(f"Eep! This is the {villain}'s house!")
    print_pause(f"The {villain} finds you!")
    if not visited:
        print_pause("You feel a bit under-prepared for this, "
                    "what with only having a tiny, rusty old magic wand.")
    print_pause("Would you like to (1) cast a spell or (2) run away?")
    choice = get_user_choice()
    if choice == 1:
        return defend()
    elif choice == 2:
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.")
        return field()

# What will happen in the cave
def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Wand of Ogoroth!")
    global visited
    visited = True
    print_pause("You discard your rusty old magic wand "
                "and take the Wand of Ogoroth with you.")
    print_pause("You walk back out to the field.")
    return field()

# What will happen in the field
def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = get_user_choice()
    if choice == 1:
        return house()
    elif choice == 2:
        return cave()

# What will happen when the user defends
def defend():
    score_handling()
    if visited:
        print_pause(f"As the {villain} moves to cast a spell, "
                    "you raise your new Wand of Ogoroth.")
        print_pause("The Wand of Ogoroth shines brightly in "
                    "your hand as you brace yourself for the spell.")
        print_pause(f"But the {villain} takes one look at your shiny new wand "
                    "and runs away!")
        print_pause(f"You have rid the town of the {villain}. "
                    "You are victorious!")
        global total_score
        total_score += 1
        restart()
    else:
        print_pause("You do your best...")
        print_pause("but your rusty old magic wand is "
                    "no match for the wicked fairy.")
        print_pause("You have been turned into a frog!")
        total_score -= 1
        restart()

# Main program
def main():
    global start
    global turns
    global visited
    visited = False
    start = time.time()
    intro()
    turns += 1
    global villain
    villain = random.choice(villains)
    field()

main()