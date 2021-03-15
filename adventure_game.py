import time
import random


def print_pause(message_to_print, delay=1):
    print(message_to_print)
    time.sleep(delay)


def intro(selected_ennemy):
    print_pause("You find yourself standing in an open field,", 0)

    print_pause("filled with grass and yellow wildflowers.")
    print_pause(
        f"Rumor has it that a {selected_ennemy}"
        " is somewhere around here"
        " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause(
        "In your hand you hold your trusty"
        " (but not very effective) dagger.")


def enter_choice(selected_ennemy, has_sword):
    print_pause("Enter 1 to knock on the door of the house.", 0)
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do ?")
    choice = valid_input("Please enter 1 or 2\n", ["1", "2"])
    if "1" == choice:
        knock(selected_ennemy, has_sword)
    else:
        cave(selected_ennemy, has_sword)


def knock(selected_ennemy, has_sword):
    print_pause("You approach the door of the house.")
    print_pause(
        "You are about to knock when the door"
        f" opens and out steps a {selected_ennemy}")
    print_pause(f"Eep! This is the {selected_ennemy}'s house!")
    print_pause(f"The {selected_ennemy} attacks you!")
    if not has_sword:
        print_pause(
            "You feel a bit under-prepared for this,"
            " what with only having a tiny dagger.")
    fight_choice = valid_input(
        "Would you like to (1) fight or (2) run away?\n",
        ["1", "2"])
    if "1" == fight_choice:
        fight(selected_ennemy, has_sword)
    else:
        run(selected_ennemy, has_sword)


def cave(selected_ennemy, has_sword):
    print_pause("You peer cautiously into the cave.")
    if has_sword:
        print_pause(
            "You've been here before, and gotten all the good stuff."
            " It's just an empty cave now.")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause(
            "You discard your silly old dagger"
            " and take the sword with you.")
    print_pause("You walk back out to the field.")
    enter_choice(selected_ennemy, True)


def fight(selected_ennemy, has_sword):
    if has_sword:
        print_pause(
            f"As the {selected_ennemy} moves to attack,"
            " you unsheath your new sword.")
        print_pause(
            "The Sword of Ogoroth shines brightly in your hand"
            " as you brace yourself for the attack.")
        print_pause(
            f"But the {selected_ennemy} "
            "takes one look at your shiny new toy and runs away!")
        print_pause(
            f"You have rid the town of the {selected_ennemy}."
            " You are victorious!")
    else:
        print_pause("You do your best...")
        print_pause(f"but your dagger is no match for the {selected_ennemy}.")
        print_pause("You have been defeated!")
    retry_play_again_choice()


def retry_play_again_choice():
    restart = valid_input("Would you like to play again? (y/n) \n", ["y", "n"])
    if "y" == restart:
        print_pause("restarting the game...")
        play_game()
    else:
        print_pause("Thanks for playing! See you next time.\n", 2)
        exit()


def run(selected_ennemy, has_sword):
    print_pause(
        "You run back into the field."
        " Luckily, you don't seem to have been followed.")
    enter_choice(selected_ennemy, has_sword)


def play_game():
    ennemies = ["pirate", "dragon", "troll", "wicked fairie", "gorgon"]
    selected_ennemy = random.choice(ennemies)
    intro(selected_ennemy)
    enter_choice(selected_ennemy, False)


def valid_input(message, options):
    while True:
        choice = input(message)
        if choice in options:
            return choice
        else:
            print_pause(f"please try again, {choice} is not valid")


play_game()
