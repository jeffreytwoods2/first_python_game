level = [1, 2, 3, 4, 5]

class Level:
    def __init__(self, level):
        self.level = level

    def check(self):
        print(f"You are at Level {self.level}.")

level_check = Level(level[-1])

print("hi ur in dunjin")
chk = input('chk level: ')

if chk == "yes":
    level_check.check()
else:
    print('poop')
