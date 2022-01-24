
# FOUR-IN-A-ROW GAME

import json
import os

# //////////////////////////////////////////////////// Functions ///////////////////////////////////////////////////////
def won(playerG, result):
    count = 0  # will hold Player 1 points to win(needs 4)
    cont = 0  # will hold Player 2 points to win(needs 4)

    if result == 2:
        checkwin(board, playerG, count, cont, result)

    # ///////////////////////////////////////////////////////////////////////////////////////////////// Checks Rows
    for j in range(6):
        for k in range(7):
            if board[k+j] == "X":
                cont = 0  # goes back to zero because it got interrupted on a row
                count = count + 1
            elif board[k+j] == 0:
                count = 0  # goes back to zero because it got interrupted on a row
                cont = cont + 1
            else:  # it's equal to _
                count = 0
                cont = 0
            # print(count, cont)  # this will show what is happening behind when counting points(it will confuse you)
            checkwin(board, playerG, count, cont, result=1)
        count = 0
        cont = 0


    # //////////////////////////////////////////////////////////////////////////////////////////////// Checks Columns
    for z in range(7):
        aux = 0
        for x in range(6):
            if board[z+aux] == "X":
                cont = 0  # goes back to zero because it got interrupted on a column
                count = count + 1
            elif board[z+aux] == 0:
                count = 0  # goes back to zero because it got interrupted on a column
                cont = cont + 1
            else:  # it's equal to _
                count = 0
                cont = 0

            aux = aux + 7
            # print(count, cont)  # this will show what is happening behind when counting points(it will confuse you)
            checkwin(board, playerG, count, cont, result=1)
        count = 0
        cont = 0


    # ////////////////////////////////////////////////////////////////////////////////////////////// Checks Vericals
    for checkB in range(21):

        # /////////////////////////////////////////////////////////////////////////////////////////////////// Player 1
        if checkB >= 18:  # From right to left
            pass
        elif checkB != 4 or checkB != 11 or checkB != 5 or checkB != 6 or checkB != 12 or checkB != 13:
            if board[checkB] == "X" and board[checkB + 8] == "X" and board[checkB + 16] == "X" and board[checkB + 24] == "X":
                checkwin(board, playerG, count=4, cont=0, result=1)

        if checkB == 21:  # From left to right
            pass
        elif checkB != 2 or checkB != 9 or checkB != 16 or checkB != 0 or checkB != 1 or checkB != 2 or checkB != 7 or checkB != 8 or checkB != 14 or checkB != 15:
            if board[checkB] == "X" and board[checkB + 6] == "X" and board[checkB + 12] == "X" and board[checkB + 18] == "X":
                checkwin(board, playerG, count=4, cont=0, result=1)


        # /////////////////////////////////////////////////////////////////////////////////////////////////// Player 2
        if checkB >= 18:  # From right to left
            pass
        elif checkB != 4 or checkB != 11 or checkB != 5 or checkB != 6 or checkB != 12 or checkB != 13:
            if board[checkB] == 0 and board[checkB + 8] == 0 and board[checkB + 16] == 0 and board[checkB + 24] == 0:
                checkwin(board, playerG, count=0, cont=4, result=1)

        if checkB == 21:  # From left to right
            pass
        elif checkB != 2 or checkB != 9 or checkB != 16 or checkB != 0 or checkB != 1 or checkB != 2 or checkB != 7 or checkB != 8 or checkB != 14 or checkB != 15:
            if board[checkB] == 0 and board[checkB + 6] == 0 and board[checkB + 12] == 0 and board[checkB + 18] == 0:
                checkwin(board, playerG, count=0, cont=4, result=1)


def checkwin(board, playerG=1, count=0, cont=0, result=0):   # Shows the winner and some details

    if result == 1:
        scorePlayerOne, scorePlayerTwo = loadScore()
        if count == 4:
            print("\n\n:: Player 1 Won!!")
            playerG = 1
            scorePlayerOne = scorePlayerOne + 1
        elif cont == 4:
            print("\n\n:: Player 2 Won!!")
            playerG = 2
            scorePlayerTwo = scorePlayerTwo + 1
        else:
            return

        TAB(board)
        print("\n:: Current Board:", board)
        print()
        print(":: Player turn:", playerG)
        print(":: Player 1 score:", scorePlayerOne)
        print(":: Player 2 score:", scorePlayerTwo)

        board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42]
        playerG = 1
        saveGame(scorePlayerOne, scorePlayerTwo, playerG, board)
        playAgain()

    elif result == 2:  # Pause
        scorePlayerOne, scorePlayerTwo = loadScore()
        saveGame(scorePlayerOne, scorePlayerTwo, playerG, board)

        print("\n:: Current Board:", board)
        print()
        print(":: Player turn:", playerG)
        print(":: Player 1 score:", scorePlayerOne)
        print(":: Player 2 score:", scorePlayerTwo)

        exit()

def playAgain():
    op = input("\n:: Do you want to play again? y/n -> ")
    if op == "y":
        again = 1
        start(again)
    elif op == "n":
        exit()
    else:
        print("\n:: Selected option is invalid. Exiting the game...")
        exit()

def loadScore():
    try:
        with open('four_row.json') as jsonLoadFile:
            data_dict = json.load(jsonLoadFile)

            scorePlayerOne = data_dict["playerOneScore"]
            scorePlayerTwo = data_dict["playerTwoScore"]

    except (FileNotFoundError, TypeError):
        print("\n:: File doesn't exist. A new file will be created(four_row.json)\n")

        board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42]
        playerG = 1
        scorePlayerOne = 0
        scorePlayerTwo = 0
        data_dict = {}

        data_dict["tab"] = board
        data_dict["playerTurn"] = playerG
        data_dict["playerOneScore"] = scorePlayerOne
        data_dict["playerTwoScore"] = scorePlayerTwo

        with open('four_row.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    return scorePlayerOne, scorePlayerTwo


def TAB(board):  # Shows the current board but inverted, so that when looping, the 0 starts from the down-right instead of the up-left(later when you select column 1, it's converted to 7 and so on)
    print("\n:::::::::::::::: ! BOARD ! ::::::::::::::::\n")
    print(":::::::::::::::::::::::::::::::::::::::::::::::")

    for i in reversed(range(42)):
        if i == 6 or i == 13 or i == 20 or i == 27 or i == 34 or i == 41:  # does an "enter" from 3 to 3
            print(":::::::  ", end=' ')
        if board[i] == "X":
            print(" X ", end=' ')
        elif board[i] == 0:
            print(" 0 ", end=' ')
        else:
            print(" _ ", end=' ')
        if i == 0 or i == 7 or i == 14 or i == 21 or i == 28 or i == 35:  # does an "enter" from 3 to 3
            print("  :::::::", end=' ')
            print()


    print(":::::::    -------------------------    :::::::\n:::::::    1   2   3   4   5   6   7    :::::::")
    print(":::::::::::::::::::::::::::::::::::::::::::::::")



def writeplay(player, play):    # Function so that there is no need to repeat if statement on the code line 373"
    global playerG
    if player == "X":
        board[play - 1] = player
        playerG = 2
    elif player == 0:
        board[play - 1] = player
        playerG = 1
    return playerG


def saveGame(scorePlayerOne=0, scorePlayerTwo=0, playerG=0, board=0):

    try:
        data_dict["tab"] = board
        data_dict["playerTurn"] = playerG
        data_dict["playerOneScore"] = scorePlayerOne
        data_dict["playerTwoScore"] = scorePlayerTwo

        with open('four_row.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    except Exception as e:
        print(":: Error:", e)

    print("\n:: Game saved successfully!")



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
            os.remove('four_row.json')
            print("\n:: File deleted successfully\n")
            break

        except (FileNotFoundError, Exception):
            print("\n:: There isn't a file to delete\n")
            break


def loadGame():
    try:
        with open('four_row.json') as jsonLoadFile:
            data_dict = json.load(jsonLoadFile)

            board = data_dict["tab"]
            playerG = data_dict["playerTurn"]
            scorePlayerOne = data_dict["playerOneScore"]
            scorePlayerTwo = data_dict["playerTwoScore"]

    except (FileNotFoundError, TypeError):
        print("\n:: File doesn't exist. A new file will be created(four_row.json)\n")

        board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42]
        playerG = 1
        scorePlayerOne = 0
        scorePlayerTwo = 0
        data_dict = {}

        data_dict["tab"] = board
        data_dict["playerTurn"] = playerG
        data_dict["playerOneScore"] = scorePlayerOne
        data_dict["playerTwoScore"] = scorePlayerTwo

        with open('four_row.json', 'w', encoding='utf-8') as file:
            json.dump(data_dict, file, ensure_ascii=False, indent=2)

    return board, playerG, scorePlayerOne, scorePlayerTwo


def pause(playerG=1):
    result = 2
    won(playerG, result)


# ///////////////////////////////////////////////// Start Live Code ////////////////////////////////////////////////////
def start(again=0):
    global board
    global playerG

    if again == 1:  # if the option to play again was selected(this is used to skip the menu bellow)
        board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42]
        playerG = 1
        pass
    elif again == 0:
        pass

board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42]
playerG = 1
playertype = "X"
scorePlayerOne = 0
scorePlayerTwo = 0
data_dict = {}

while True:
    try:
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
            board, playerG, scorePlayerOne, scorePlayerTwo = loadGame()
            print("\n:: Current Board:", board)
            print()
            print(":: Player turn:", playerG)
            print(":: Player 1 score:", scorePlayerOne)
            print(":: Player 2 score:", scorePlayerTwo)

            tabu = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 38, 39, 40, 41, 42]
            if board == tabu:
                print("\n:: There isn't any game in progress saved(pause)\n")
            else:
                break

        elif op == "b":  # Starts new game with a clean board but with same
            scorePlayerOne, scorePlayerTwo = loadScore()
            print("\n:: Current Board:", board)
            print()
            print(":: Player turn:", playerG)
            print(":: Player 1 score:", scorePlayerOne)
            print(":: Player 2 score:", scorePlayerTwo)
            break
        elif op == "c":
            deleteGame()
            continue

    except ValueError:
        print(":: Error - Select a valid option!\n\n")
        continue


while True:
    TAB(board)
    try:
        print("\n:: (999, to pause and go to the Game Menu)")
        play = int(input(":: Player {} ({})- > Select in what column do you want to play(1 to 7): ".format(playerG, playertype)))
        if play == 999:
            pause(playerG)
    except ValueError:
        print("\n:: Select a valid number(1 to 7)\n")
        continue

    if play > 7 or play < 1:
        print("\n:: Select a valid number(1 to 7)\n")
        continue

    # //////////////////////////////////////////////  Inverts the play(needed to display the game correctly)(could be made into a loop)
    if play == 1:
        play = 7
    elif play == 2:
        play = 6
    elif play == 3:
        play = 5
    elif play == 5:
        play = 3
    elif play == 6:
        play = 2
    elif play == 7:
        play = 1
    # //////////////////////////////////////////////


    # Decides the sympol each player uses
    player = 0
    if playerG == 1:
        player = "X"
    elif playerG == 2:
        player = 0

    try:  # Checks if positions is already in use(this section could be turned into a loop)
        if board[play - 1] == "X" or board[play - 1] == 0:
            play = play + 7  # +7 so the play happens in the same column but above if bellow is already in use
            if board[play - 1] == "X" or board[play - 1] == 0:
                play = play + 7
                if board[play - 1] == "X" or board[play - 1] == 0:
                    play = play + 7
                    if board[play - 1] == "X" or board[play - 1] == 0:
                        play = play + 7
                        if board[play - 1] == "X" or board[play - 1] == 0:
                            play = play + 7
                            if board[play - 1] == "X" or board[play - 1] == 0:
                                play = play + 7
                                if player == "X":
                                    play = play + 7
                                    board[play - 1] = player
                                    playerG = 2
                                elif player == 0:
                                    play = play + 7
                                    board[play - 1] = player
                                    playerG = 1
                            else:
                                writeplay(player, play)
                        else:
                            writeplay(player, play)
                    else:
                        writeplay(player, play)
                else:
                    writeplay(player, play)
            else:
                writeplay(player, play)
        else:
            writeplay(player, play)

        won(playerG, result=0)


        # //////////////////// this part is just for the looks(ignore)
        if playerG == 1:
            playertype = "X"
        elif playerG == 2:
            playertype = 0
        # ////////////////////

    except IndexError:
        print("\n:: Invalid play - Column select has no remaining spaces available")
        continue
