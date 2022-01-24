
# HANGMAN GAME

import random
import json
import os

# In Portuguese (remove the # and add it to the front of the next languague pack)
# word_animals = ["gato", "cao", "esquilo", "tubarao", "girafa", "raposa", "tigre", "abelha", "mosquito", "melga"]
# word_names = ["pedro", "luis", "manuel", "joana", "manela", "marta", "carolina", "marisa", "joao", "tiago"]
# word_objects = ["teclado", "mesa", "computador", "televisor", "mochila", "cadeira", "livro", "garrafa", "auscultadores"]
# word_geography = ["portugal", "america", "inglaterra", "australia", "canada", "faro", "tavira", "lagos", "sintra"]

# In English (remove the # and add it to the front of the previous languague pack)(you can add more words in front of the previous word seperated by a ' , ' and inside these " ")
word_animals = ["cat", "dog", "shark", "squirrel", "giraffe", "fox", "tiger", "bee", "mosquito", "rhino"]
word_names = ["peter", "jack", "john", "joe", "marie", "joane", "caroline", "carol", "andrew", "jeff"]
word_objects = ["keyboard", "table", "computer", "television", "backpack", "chair", "book", "water", "earphones", "headphones"]
word_geography = ["portugal", "america", "england", "australia", "canada", "london", "tavira", "chicago", "lisbon"]


def deleteGame():
    while True:
        op = str(input(":: Are you sure that you want to delete any saved data? y/n -> "))

        if op == "y":
            pass
        elif op == "n":
            break
        else:
            print("\n:: Select a valid option")
            continue

        try:
            os.remove('hangman.json')
            print("\n:: File deleted successfully\n")
            break

        except (FileNotFoundError, Exception):
            print("\n:: There isn't a file to delete\n")
            break


def saveGame(palav, lives, wonGames, lostGames, word):
    try:
        data_dict["myWord"] = palav
        data_dict["lives"] = lives
        data_dict["wonGames"] = wonGames
        data_dict["lostGames"] = lostGames
        data_dict["word"] = word

        with open('hangman.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    except Exception as e:
        print(":: Error:", e)

    print("\n:: Game saved successfully!")

def loadScore():
    try:
        with open('hangman.json') as jsonLoadFile:
            data_dict = json.load(jsonLoadFile)

            wonGames = data_dict["wonGames"]
            lostGames = data_dict["lostGames"]

    except (FileNotFoundError, TypeError):
        print("\n:: File doesn't exist. A new file will be created(hangman.json)\n")

        palav = []
        lives = 6
        wonGames = 0
        lostGames = 0
        data_dict = {}

        data_dict["myWord"] = palav
        data_dict["lives"] = lives
        data_dict["wonGames"] = wonGames
        data_dict["lostGames"] = lostGames

        with open('hangman.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    return wonGames, lostGames



def loadGame():
    try:
        with open('hangman.json') as jsonLoadFile:
            data_dict = json.load(jsonLoadFile)

            palav = data_dict["myWord"]
            lives = data_dict["lives"]
            wonGames = data_dict["wonGames"]
            lostGames = data_dict["lostGames"]
            word = data_dict["word"]

    except (FileNotFoundError, TypeError):
        print("\n:: File doesn't exist. A new file will be created(hangman.json)\n")

        palav = []
        lives = 6
        wonGames = 0
        lostGames = 0
        word = ""
        data_dict = {}

        data_dict["myWord"] = palav
        data_dict["lives"] = lives
        data_dict["wonGames"] = wonGames
        data_dict["lostGames"] = lostGames
        data_dict["word"] = word

        with open('hangman.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    return palav, lives, wonGames, lostGames, word


def pause():
    saveGame(palav, lives, wonGames, lostGames, word)
    exit()


def playAgain():
    while True:
        op = input(":: Do you want to play again? y/n -> ")
        if op == "y":
            break
        elif op == "n":
            saveGame(palav, lives, wonGames, lostGames, word)
            exit()
        else:
            print("\n:: Selected option is invalid. Exiting game...")
            continue


# ///////////////////////////////////////////////// Start Live Code ////////////////////////////////////////////////////
def start():
    pass


palav = []
lives = 6
word = ""
wonGames = 0
lostGames = 0
data_dict = {}

skip = 0


while True:
    try:
        print("::::::::::::: ! Select a Option ! :::::::::::::")
        print("::                                           ::")
        print("::         (a) Load previous Round           ::")
        print("::         (b) Start new Round               ::")
        print("::         (c) Delete saved game             ::")
        print("::                                           ::")
        print(":::::::::::::::::::::::::::::::::::::::::::::::\n")

        op = input(":: -> ")
        op.lower()

        if op == "a":  # Continues previous saved game(pause)
            palav, lives, wonGames, lostGames, word = loadGame()
            print("\n:: Current Word:", palav)
            print(":: Lives Remaing:", lives)
            print(":: Won Games:", wonGames)
            print(":: Lost Games:", lostGames)
            print()
            print(":: ", end=' ')
            for k in palav:
                print(k, end=' ')

            if lives >= 1:
                skip = 1
                break
            elif lives == 0:
                print("\n:: There isn't any game in progress saved(pause)\n")
                skip = 0
                continue

        elif op == "b":  # Starts new game with clean word, but scores remains
            palav = []
            lives = 6
            word = ""
            wonGames, lostGames = loadScore()
            print("\n:: Current Word: ------")
            print(":: Lives Remaing:", lives)
            print(":: Won Games:", wonGames)
            print(":: Lost Games:", lostGames)
            print()

            skip = 0
            break
        elif op == "c":
            deleteGame()
            continue

    except ValueError:
        print(":: Error - Select a valid option!\n\n")
        continue

keepGoing = True
while True:
    while keepGoing:
        if skip == 0:
            print("\n:: Words Group\n:: (1) Animals\n:: (2) Names\n:: (3) Objects\n:: (4) Geography\n")
            while True:
                try:
                    op = input(":: Select what genre of the word group you want to play with: ")
                    print()
                except ValueError:
                    print("\n:: Select a valid option\n")
                    skip = 0
                    continue

                if op == "1":
                    word = random.choice(word_animals)
                elif op == "2":
                    word = random.choice(word_names)
                elif op == "3":
                    word = random.choice(word_objects)
                elif op == "4":
                    word = random.choice(word_geography)
                else:
                    print(":: Selected option is invalid!!")
                    continue

                for j in word:
                    if j == " ":
                        palav.append(' ')
                    else:
                        palav.append('_')  # this is so that you can have a '_' where the missing letter is
                skip = 1

                print(":: Word(remove this in the code with a #):", word)  # This shows what words is being played with(hide this with a # in front of it)
                break
        elif skip == 1:
            pass


        check = 1  # will be used to decide if its a win(1/0)
        try:
            print("\n:: /////////////////////\n:: (999, to pause and go to the Game Menu)")
            result = str(input(":: Select a letter(999 to pause and save): "))
            if result == "999":
                pause()
            elif result == "":
                print(":: There was nothing selected. Try again...\n\n")
                continue
        except ValueError:
            print("\n:: Select a valid character(a-z / A-Z)\n")
            continue

        result = result.lower()  # transform all letters to small caps
        for i in range(0, len(word)):
            if word[i] == result:
                palav[i] = result
                check = 0
                print(":: Corret Letter!")

        if check == 1:
            lives = lives - 1
            print(":: Wrong Letter!")
            if lives == 0:
                print(":: You Lost!!")
                print("..____________")
                print("||          |")
                print("||         (\")")
                print("||         /|\ ")
                print("||         / \ ")
                print("||______________")
                print("||______________")

                wonGames, lostGames = loadScore()
                lostGames = lostGames + 1
                saveGame(palav, lives, wonGames, lostGames, word)
                break

        print(":: lives restantes:", lives, "\n")
        if lives == 6:
            print(":: ..____________")
            print(":: ||          |")
            print(":: ||")
            print(":: ||")
            print(":: ||")
            print(":: ||______________")
            print(":: ||______________\n")
        elif lives == 5:
            print("..____________")
            print("||          |")
            print("||         (\")")
            print("||")
            print("||")
            print("||______________")
            print("||______________\n")
        elif lives == 4:
            print("..____________")
            print("||          |")
            print("||         (\")")
            print("||          | ")
            print("||")
            print("||______________")
            print("||______________\n")
        elif lives == 3:
            print("..____________")
            print("||          |")
            print("||         (\")")
            print("||         /|")
            print("||")
            print("||______________")
            print("||______________\n")
        elif lives == 2:
            print("..____________")
            print("||          |")
            print("||         (\")")
            print("||         /|\ ")
            print("||")
            print("||______________")
            print("||______________\n")
        elif lives == 1:
            print("..____________")
            print("||          |")
            print("||         (\")")
            print("||         /|\ ")
            print("||         /")
            print("||______________")
            print("||______________\n")
            print()

        countErro = 0
        print(":: ", end=' ')
        for k in palav:
            print(k, end=' ')
            if k != "_":  # Checks if there is still any letter missing to win
                countErro = countErro + 1

            if countErro == len(palav):
                print("\n\n:: You Won!!")

                wonGames, lostGames = loadScore()
                wonGames = wonGames + 1
                lives = 0
                saveGame(palav, lives, wonGames, lostGames, word)

                keepGoing = False
        print()

    playAgain()
    skip = 0
    word = ""
    palav = []
    lives = 6
    keepGoing = True
    continue
