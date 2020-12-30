def trick():
    print("You approach the coveted artifact.")
    time.sleep(0.5)
    print("A trap door opens where you stand!")
    print("You fall into another chamber!")
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
        elif action == "proceed" or "Proceed":
            trick()
        else:
            print("Huh?")
