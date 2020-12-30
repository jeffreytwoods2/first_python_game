from sys import exit
import sys
import time
import random

level = [1]
point = 1
roll = random.randint(1, 10)
p1_health = [100]
troll_health = [100]
troll_art = open("troll_art.txt")

def level_up():
    print("You leveled up!")
    level.append(level[-1] + point)
    print(f"You are now at Level {level[-1]}.")


def start():
    print("Hint: type \"c\" at any time to check your level!")
    art = open("cave_art.txt")
    print(art.read())
    art.close()
    print("You find yourself in a dark, musty cavern.")
    print("Your cough reverberates through the echoey chamber.")
    print("At the far end of the expanse, you see a door, lit dimly by torches mounted on the wall.")
    print("You approach the ominous door.")

    while True:
        choice = input("explore, open door:\n> ")

        if choice == "explore" or choice == "Explore":
            print("There isn't much else in this area.")
        elif choice == "open door" or choice == "Open door":
            level_up()
            door_1()
        elif choice == "c":
            print(f"You are at Level {level[-1]}.")
        else:
            print("Please answer the question.")


def door_1():
    print("You enter a small chamber with no way out.")
    print("The door shuts behind you.")
    time.sleep(1)
    print("A riddle appears on the wall:\n\"What occurs twice in a week, once in a year, but never in a day?\"")

    while True:
        choice = input("Your answer:\n> ")

        if choice == "e" or choice == "E":
            level_up()
            door_2()
        elif choice == "c":
            print(f"You are at Level {level[-1]}.")
        else:
            print("An onslaught of arrows shoots forth from the wall.")
            dead("The world slowly fades to black.")


def trick():
    print("You approach the coveted artifact.")
    time.sleep(0.5)
    print("A trap door opens where you stand!")
    print("You fall into another chamber!")
    level_up()
    troll_room()


def door_2():
    print("You enter a large chamber overflowing with stalactites and stalagmites.")
    print("A path leads to the far end of the chamber, and there you see it.")
    print("The Dream Stone.")
    print("When worn around the neck, this stone guides you to safety and success in life.")

    while True:
        action = input('explore, proceed:\n> ')
        if action == "explore" or action == "Explore":
            print("You find a tiny shred of paper.")
            print("Are those...stock tickers on the edge?")
        elif action == "proceed" or action == "Proceed":
            trick()
        elif action == "c":
            print(f"You are at Level {level[-1]}.")
        else:
            print("Huh?")


def fight():
    while True:
        if p1_health[-1] > 0 and troll_health[-1] > 0:
            move = input("attack or flee:\n>")
            if move == "attack":
                roll = random.randint(1, 10)
                if roll <= 4:
                    print("You missed!")
                    p1_health.append(p1_health[-1] - 5)
                    print(f"Your health is now at {p1_health[-1]}%.")
                elif roll >= 5:
                    print("You landed a hit!")
                    troll_health.append(troll_health[-1] - 50)
                    print(f"The troll's health is now at {troll_health[-1]}%.")
                else:
                    print("Error.")
                    exit(0)
            elif move == "flee":
                print("The troll lands a hit.")
                p1_health.append(p1_health[-1] - 20)
                print(f"Your health is now at {p1_health[-1]}.")
            elif move == "c":
                print(f"You are at Level {level[-1]}.")
            else:
                print("Input invalid. Please type again.")
        elif p1_health[-1] == 0 and troll_health[-1] > 0:
            dead("Your health has reached 0%.")
        elif p1_health[-1] > 0 and troll_health[-1] == 0:
            win()
        else:
            print("Huh?")


def troll_room():
    print(troll_art.read())
    troll_art.close()
    print("A cave troll appears!")
    time.sleep(0.5)
    print("An elven broadsword appears in your hand.")
    time.sleep(1)
    print("It's as light as a feather.")
    fight()

def finale():
    print("...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    print("Grab those calls and run! You win!")
    exit(0)


def end():
    print("You open the door and enter a poorly-lit chamber.")
    print("As your eyes adjust, you notice mounds of white leaves.")
    time.sleep(0.5)
    print("Wait, those aren't leaves. Those are pieces of paper.")

    while True:
        action = input('explore, examine:\n> ')
        if action == "explore" or action == "Explore":
            print("There's nowhere else to go.")
        elif action == "examine" or action == "Examine":
            print("You pick up one of the sheets of paper.")
            print("""
            $TSLA Call
            October - $69,420
            Price: $1500
            """)
            finale()
        elif action == "c":
            print(f"You are at Level {level[-1]}.")
        else:
            print("What?")


def win():
    print("You killed the troll and leveled up!")
    level.append(level[-1] + point)
    print(f"You are now at Level {level[-1]}.")

    while True:
        cont = input("Press enter to continue through the door.")

        if cont == "":
            end()
        elif cont == "c":
            print(f"You are at Level {level[-1]}.")
        else:
            dead("I said press enter.")


def dead(why):
    print(why, "You have died.")
    exit(0)

start()
