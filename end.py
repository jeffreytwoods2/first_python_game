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
        else:
            print("What?")
