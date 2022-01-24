# GameMix
A game package with classic games self-coded, like the rooster, hangman and four in a row games.

Info:
The games were coded in my original languague and then translated to english for better understading. Because of that, some errors can occur, although i highly douth that as I thoroughly checked the code

Also, I coded these games using my own logic of understading on how to implement what I'm thinking to code. It might look sluggish or weird, but to me it's actually quite clear. But I understand that I still need to improve how I code. For now, this is it.

There are two types of files shared. There is a raw python code and also an executable that i did with pyinstaller(GameMix executable), so you don't need to have a Python interpreter installed.

- To play the game you can just open the folder GameMix executable and run the first file named main.exe(NOT main.spec)

- To see the code, you can just open the folder on your IDLE interpreter.

> Rooster Game
```

How to play:
The game board will be displayed in a square of 3x3, you will then be asked to select a number, 1 to 9.
The number will indicate a position of the square and will play an "X" or "0", dependingon wich player
is playing.

The winner will be decided if any player does three in a row horizontally, vertically or in a diagonal.

A score for each player will be saved and maintained. You can delete the save file, and lose all scores.

You can also pause the game. When it's asked of you to play, if you say "999", the current status of
the game, board, player turn, and scores will all be saved. When you start the game and select to
continue previous round(if you select start new round, you can't continue previous game) the game
will start exacly where you stoped previously.

```

> Four in a Row Game
```

How to play:
The game board will be displayed in a rectangle of 7x6, you will then be asked to select a number, 1 to 7.
The number will indicate a position of the column and will play an "X" or "0", depending on wich player
is playing. If you select a position that already has a play in it, your play will be on top of it that is
if it isn't full yet(column)

The winner will be decided if any players does four in a row horizontally, vertically or in a diagonal.

A score for each player will be saved and maintained. You can delete the save file, and lose all scores.

You can also pause the game. When it's asked of you to play, if you say "999", the current status of
the game, board, player turn, and scores will all be saved. When you start the game and select to
continue previous round(if you select start new round, you can't continue previous game) the game
will start exacly where you stoped previously.

```

> Hangman Game
```

How to play:
The game will ask what genre you what the word to be, and then will randomly select a list of words
previously inserted(that you can change) and display an underscore on representing each letter while
skipping spaces(this works with words that have spaces).

You will then play a letter and if you get it correct, it will display that letter only and the rest will
stay as underscores. If you are wrong, a hangman will happear, and if you reach 6 wrong answers you lose.

The winner will be decided if you get all letters correct with 1 or more lives remaining.

A score for you will be saved and maintained. You can delete the save file, and lose the scores.

You can also pause the game. When it's asked of you to play, if you say "999", the current status of
the game, mystery word, player turn, scores and your word hints, will all be saved. When you start
the game and select to continue previous round(if you select start new round, you can't continue
previous game) the game will start exacly where you stoped previously.

Available changes you can do:
  - Change or add more words my seperating them with a comma( , ) and between quoting marks(" ")
    like this example: word_animals = ["cat", "dog", "shark"] on the lines from 8 to 18(there is also
    words in portuguese and english). You can add words with or without spaces.

```


> Minesweeper Game
```

Currently in development

```
