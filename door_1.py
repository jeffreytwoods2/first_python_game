def door_1():
    print("You enter a small chamber with no way out.")
    print("The door shuts behind you.")
    time.sleep(1)
    print("A riddle appears on the wall:\n\"What occurs twice in a week, once in a year, but never in a day?\"")

    choice = input("Your answer:\n> ")

    if choice == "e" or choice == "E":
        door_2()
    else:
        print("An onslaught of arrows shoots forth from the wall.")
        dead("The world slowly fades to black.")

door_1()
