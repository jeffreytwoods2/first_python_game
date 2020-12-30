from sys import exit
import time

def start():
    print("You find yourself in a dark, musty cavern.")
    print("Your cough reverberates through the echoey chamber.")
    print("At the far end of the expanse, you see two doors, lit dimly by torches mounted on the wall.")
    print("You approach the ominous doors. Which will you open?")

    while True:
        choice = input("left or right:\n> ")

        if choice == "left":
            davy_jones()

        elif choice == "right":
            puzzle_room()
        else:
            print("Please answer the question.")


def davy_jones():
    print("You enter a smaller chamber.")
    time.sleep(1)
    print("Suddenly, the Flying Dutchman appears!")
    time.sleep(1)
    print("What do you do?")
    fd_moved = False

    while True:
        choice = input("confront, run away, or proceed:\n> ")

        if choice == "run away":
            dead("The Flying Dutchman flattens you against the cavern floor.")

        elif choice == "confront" and not fd_moved:
            print("The Flying Dutchman commends your bravery and moves out of the way.")
            fd_moved = True

        elif choice == "confront" and fd_moved:
            dead("The Flying Dutchman grows weary of your games and banishes you to the shadow realm.")

        elif choice == "proceed" and not fd_moved:
            print("The Flying Dutchman flings you effortlessly back to the entrance.")

        elif choice == "proceed" and fd_moved:
            gold_room()



def puzzle_room():
    print("You enter a small chamber with no way out.")
    print("The door shuts behind you.")
    time.sleep(1)
    print("A riddle appears on the wall:\n\"What occurs twice in a week, once in a year, but never in a day?\"")

    choice = input("Your answer:\n> ")

    if choice == "e" or choice == "E":
        gold_room()
    else:
        print("An onslaught of arrows shoots forth from the wall.")
        dead("The world slowly fades to black.")


def gold_room():
    print("You enter a room filled to the ceiling with bricks of gold.")
    print("Load some into my truck, and let's get out of here!")
    exit(0)

def dead(why):
    print(why, "\nGame over.")
    exit(0)

start()
