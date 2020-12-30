from sys import exit
import random
import time

level = [1]
point = 1
roll = random.randint(1, 10)
p1_health = [100]
troll_health = [100]
troll_art = open("troll_art.txt")

def troll_room():
    print(troll_art.read())
    troll_art.close()
    print("A cave troll appears!")
    time.sleep(0.5)
    print("An elven broadsword appears in your hand.")
    time.sleep(1)
    print("It's as light as a feather.")
    fight()

def fight():
    while True:
        if p1_health[-1] > 0 and troll_health[-1] > 0:
            move = input("attack or flee:\n>")
            if move == "attack":
                roll = random.randint(1, 10)
                if roll <= 4:
                    print("You missed!")
                    p1_health.append(p1_health[-1] - 20)
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
            else:
                print("Input invalid. Please type again.")
        elif p1_health[-1] == 0 and troll_health[-1] > 0:
            dead()
        elif p1_health[-1] > 0 and troll_health[-1] == 0:
            win()
        else:
            print("Huh?")
