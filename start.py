def start():
    print("You find yourself in a dark, musty cavern.")
    print("Your cough reverberates through the echoey chamber.")
    print("At the far end of the expanse, you see a door, lit dimly by torches mounted on the wall.")
    print("You approach the ominous door.")

    while True:
        choice = input("explore, open door:\n> ")

        if choice == "explore" or choice == "Explore":
            print("There isn't much else in this area.")

        elif choice == "open door" or choice == "Open door":
            door_1()
        else:
            print("Please answer the question.")
