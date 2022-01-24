
# ROOSTER GAME

import json
import os

def winner(result=0, player=1, board=[]):
    # ///////////////////////////////////////////////////////////////////////////////////////////////// Checks Rows
    for k in range(3):
        if k == 1:
            k = k + 2  # Search second row
        elif k == 2:
            k = k + 4  # Search third row

        if board[k] == "X" and board[k+1] == "X" and board[k+2] == "X":
            result = 1
        elif board[k] == 0 and board[k+1] == 0 and board[k+2] == 0:
            result = 2


    #///////////////////////////////////////////////////////////////////////////////////////////////// Checks Columns
    for k in range(3):
        if board[k] == "X" and board[k+3] == "X" and board[k+6] == "X":
            result = 1
        elif board[k] == 0 and board[k+3] == 0 and board[k+6] == 0:
            result = 2


    # ////////////////////////////////////////////////////////////////////////////////////////////// Checks verticals
    for k in range(1):
        if board[k] == "X" and board[k + 4] == "X" and board[k + 8] == "X":
            result = 1
        elif board[k] == 0 and board[k + 4] == 0 and board[k + 8] == 0:
            result = 2
        k = 2
        if board[k] == "X" and board[k + 2] == "X" and board[k + 4] == "X":
            result = 1
        elif board[k] == 0 and board[k + 2] == 0 and board[k + 4] == 0:
            result = 2


    if result == 1 or result == 2:
        scorePlayerOne, scorePlayerTwo = loadScore()
        if result == 1:
            print("\n:: Player 1 is the winner!")
            scorePlayerOne = scorePlayerOne + 1
        elif result == 2:
            print("\n:: Player 2 is the winner!")
            scorePlayerTwo = scorePlayerTwo + 1
        else:
            print(":: Unexpected Error - there will be no saved progress, to not corrup files")
            exit()

        TAB()
        print("\n:: Current Board:", board)
        print()
        print(":: Player turn: Player", player)
        print(":: Player 1 score:", scorePlayerOne)
        print(":: Player 2 score:", scorePlayerTwo)

        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player = 1
        saveGame(player, scorePlayerOne, scorePlayerTwo, result, board)

        playAgain()

    elif result == 3:  # Pause
        scorePlayerOne, scorePlayerTwo = loadScore()
        saveGame(player, scorePlayerOne, scorePlayerTwo, result, board)

        print("\n:: Current Board:", board)
        print()
        print(":: Player turn: Player", player)
        print(":: Player 1 score:", scorePlayerOne)
        print(":: Player 2 score:", scorePlayerTwo)

        exit()


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
            os.remove('rooster.json')
            print("\n:: File deleted successfully\n")
            break

        except (FileNotFoundError, Exception):
            print("\n:: There isn't a file to delete\n")
            break


def pause(player = 1):
    result = 3
    winner(result, player, board)


def saveGame(player = 1, scorePlayerOne = 0, scorePlayerTwo = 0, result = 0, board = 0):
    if result == 1 or result == 2:
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    elif result == 3:
        pass

    try:
        data_dict["tab"] = board
        data_dict["playerTurn"] = player
        data_dict["playerOneScore"] = scorePlayerOne
        data_dict["playerTwoScore"] = scorePlayerTwo

        with open('rooster.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    except Exception as e:
        print(":: Error:", e)

    print("\n:: Game saved successfully!")

def loadScore():
    try:
        with open('rooster.json') as jsonLoadFile:
            data_dict = json.load(jsonLoadFile)

            scorePlayerOne = data_dict["playerOneScore"]
            scorePlayerTwo = data_dict["playerTwoScore"]

    except (FileNotFoundError, TypeError):
        print("\n:: File doesn't exist. A new file will be created(rooster.json)\n")

        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player = 1
        scorePlayerOne = 0
        scorePlayerTwo = 0
        data_dict = {}

        data_dict["tab"] = board
        data_dict["playerTurn"] = player
        data_dict["playerOneScore"] = scorePlayerOne
        data_dict["playerTwoScore"] = scorePlayerTwo

        with open('rooster.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    return scorePlayerOne, scorePlayerTwo

def loadGame():
    try:
        with open('rooster.json') as jsonLoadFile:
            data_dict = json.load(jsonLoadFile)

            board = data_dict["tab"]
            player = data_dict["playerTurn"]
            scorePlayerOne = data_dict["playerOneScore"]
            scorePlayerTwo = data_dict["playerTwoScore"]

    except (FileNotFoundError, TypeError):
        print("\n:: File doesn't exist. A new file will be created(rooster.json)\n")

        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player = 1
        scorePlayerOne = 0
        scorePlayerTwo = 0
        data_dict = {}

        data_dict["tab"] = board
        data_dict["playerTurn"] = player
        data_dict["playerOneScore"] = scorePlayerOne
        data_dict["playerTwoScore"] = scorePlayerTwo

        with open('rooster.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    return board, player, scorePlayerOne, scorePlayerTwo


def TAB(board):  # Shows the current board
    cont = 1
    print("\n:::::::::::::::::: ! BOARD ! ::::::::::::::::::\n")
    print(":::::::::::::::::::::::::::::::::::::::::::::::")

    for i in range(len(board)):
        if i == 0 or i == 3 or i == 6:  # does an "enter" from 3 to 3
            print("::::::::::::::: ", end=' ')

        if board[i] == 'X':
            print("  X", end=' ')
        elif board[i] == 0:
            print("  0", end=' ')
        else:
            print(" ", cont, end=' ')   # print(" _ ", end=' ') -> it's pretier

        if i == 2 or i == 5 or i == 8:  # does an "enter" from 3 to 3
            print("   :::::::::::::::", end=' ')
            print()
        cont = cont + 1

    print(":::::::::::::::::::::::::::::::::::::::::::::::")


def playAgain():
    op = input("\n:: Do you want to play again? y/n -> ")
    if op == "y":
        start(again=1)
    elif op == "n":
        exit()
    else:
        print("\n:: Selected option is invalid. Exiting the game...")
        exit()


# ///////////////////////////////////////////////// Start Live Code ////////////////////////////////////////////////////

def start(again=0):
    global board
    global player

    if again == 1:  # if the option to play again was selected(this is used to skip the menu bellow)
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        player = 1
    elif again == 0:
        pass

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player = 1
scorePlayerOne = 0
scorePlayerTwo = 0
data_dict = {}
result = 0

while True:
    try:    # MENU
        print("::::::::::::: ! Select a Option ! :::::::::::::")
        print("::                                           ::")
        print("::         (a) Load previous round           ::")
        print("::         (b) Start new round               ::")
        print("::         (c) Delete saved game             ::")
        print("::                                           ::")
        print(":::::::::::::::::::::::::::::::::::::::::::::::\n")

        op = input(":: -> ")
        op.lower()

        if op == "a":  # Continues previous saved game(was in pause)
            board, player, scorePlayerOne, scorePlayerTwo = loadGame()
            print("\n:: Current Board:", board)
            print()
            print(":: Player turn: Player", player)
            print(":: Player 1 score:", scorePlayerOne)
            print(":: Player 2 score:", scorePlayerTwo)

            tabu = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            if board == tabu:
                print("\n:: There isn't any game in progress saved(pause)\n")
            else:
                break

        elif op == "b":  # Starts new game with a clean board but with same
            scorePlayerOne, scorePlayerTwo = loadScore()
            print("\n:: Current Board:", board)
            print()
            print(":: Player turn: Player", player)
            print(":: Player 1 score:", scorePlayerOne)
            print(":: Player 2 score:", scorePlayerTwo)
            break
        elif op == "c":
            deleteGame()
            continue

    except ValueError:
        print(":: Error - Select a valid position!\n\n")
        continue

while True:
    TAB(board)
    try:
        print("\n:: (999, to pause and go to the Game Menu)")
        play = int(input(":: Player {} - > Select a number between 1 & 9(999 to pause and save): ".format(player)))
        if play == 999:
            pause(player)
    except ValueError:
        print("\n:: Select a valid number(1 to 9)")
        continue


    if play > 9 or play < 1:
        print("\n:: Select a valid number(1 to 9)")
        continue

    if board[play - 1] == "X" or board[play - 1] == "0":    # Checks if the place of the play is empty
        print()
        print("\n:: Position selected is already in use, select another posicions\n")
        continue

    if player == 1:   # Writes to the list and changes player turn
        board[play - 1] = 'X'
        winner(result, player, board)
        player = 2
    elif player == 2:
        board[play - 1] = 0
        winner(result, player, board)
        player = 1
