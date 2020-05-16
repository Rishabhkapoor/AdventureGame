import time
import random


def print_pause(msg_to_print):
    print(msg_to_print)
    time.sleep(2)


def introduction():
    print_pause("You find yourself standing in an open field, filled "
                "with long grown grass.\n")
    Devil_list = ['Cruel King', 'Old Witch', 'ManEater']
    Devil = random.choice(Devil_list)
    time.sleep(3)
    print_pause("Rumor has it that a " + devil + " is somewhere around "
                "here.\n")
    print_pause("You see a cave on your right side and a shady hut infront of the mountains on the left side.\n")
    
def dilema(items):
    
    print_pause("What would you like to do?")
    direction = input("1. Go left\n2. Go right\n")
    while direction != "1" and direction != "2":
        direction = input("Please enter 1 or 2.\n")
    if direction == "1":
        hut(items)
    elif direction == "2":
        cave(items)
        
def hut(items, devil):
    drawer = [" a  rusty dagger", " a shining sword"]
    print_pause("You enter the hut and it is empty and only has an almirah.")
    print_pause("You one the Almirah and see that there are lots of skulls kept in it, your eye goes towards a long wooden box.\n")
    if len(items) == 0:
        print_pause("You open the box!")
        items.append(random.choice(drawer))
        print_pause("You find a " + items[0] + "lying in the box!")
    print_pause("You can't find anything else so you return to the fields.")
    dilema(items)    
    
def Cave(items, devil):
    print_pause(" You stand in front of the cave and try to peak inside but since it is very dark you are unable to see anything.\n")
    print_pause(" So you enter the cave")
    print_pause("\n Once you go inside the cave"
                "You see a " + devil + "lying on a bed and relaxing")
    print_pause("\nEep! here he is the " + option + "!")
    print_pause("\nThe " + option + " sees and and gets up to attack you!\n")
    if " a shining sword" not in item:
        print_pause("You feel scared and unprepared for this,\n")
    while True:
        choice2 = input("Would you like to (1) fight or (2) "
                        "run away?")
        if choice2 == "1":
            if "a shining sword" in item:
                print_pause("\n As the " + devil + " moves to attack, "
                            "you take out the sword.")
                print_pause("\nThe Sword of Valeria shines brightly "
                            "as you prepare yourself for the "
                            "attack.")
                print_pause("\n You rush to stab the" + devil + "and he takes out his weapon"
                            "But he doesn't stand in front of your shiny new sword.")
                print_pause("\nYou have rid the town of the " + devil +
                            ". You are victorious!\n")
            else:
                print_pause("\nYou fight...")
                print_pause("but you are too week to fight with someone as skilled as "
                            + devil + ".")
                print_pause("\nYou have been Killed and defeated!\n")
            game_over()
            break
        if choice2 == "2":
            print_pause("\n You run back towards the field. "
                        "\nLuckily, you have not been "
                        "followed.\n")
            dilema(items, devil)
            break

def game_over():
    print_pause("Game Over")
    game_again()
            
def play_again():
    again = input("Would you like to play again? (y/n)").lower()
    if again == "y":
        print_pause("\n\n\nExcellent! Restarting the game ...  All the Best!\n\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\n\nThanks for playing! See you next time.\n\n\n")
    else:
        play_again()


def play_game():
    items = []
    introduction()
    dilema(items)


play_game()
