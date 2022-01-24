
# GAME MENU

from subprocess import call

def option(op):
    if op == "a":
        call(["python", "roosterGame.py"])
        # rooster.start()
    elif op == "b":
        call(["python", "four_rowGame.py"])
        # four_row.start()
    elif op == "c":
        call(["python", "hangmanGame.py"])
        # hangman.start()
    elif op == "d":
        print(":: \n:: Game is currently in development")
    elif op == "e":
        exit()
    else:
        print(":: Selected option is invalid")


# ///////////////////////////////////////////////// Start Live Code ////////////////////////////////////////////////////
if __name__ == '__main__':
    while True:
        try:
            print("\n:: ////////////// ! GAME MENU ! //////////////\n::")
            op = str(input(":: Select what you want to play:\n:: (a) Rooster Game\n:: (b) Four in a Row\n:: (c) Hangman\n:: (d) Minesweeper\n::\n:: (e) Exit\n::\n:: -> "))
        except ValueError:
            print("\n:: Select a valid option\n")
            continue

        option(op)
        continue
