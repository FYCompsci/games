# -*- coding: utf-8 -*-

#Text-Based Slot Machine
#By Zack Nathan

from random import choice
from time import sleep
import sys

#Every spin of the slot machine runs this function once
def spin():
    global wins, losses

    #Pick a random character for each of the 9 boxes
    for i in range(9):
        boxes[i] = choice(characters)

    #To pick the characters, I separated them into lines, because python prints line by line, not side by side
    print """\n                              .-------. """
    print """                              |Jackpot| """
    print """                  ____________|_______|____________ """
    print """                 |★                               ★| """
    print """                 |★  ____  __      __  ____  ___  ★| """
    print """                 |★ / ___)(  )   /  \(_  _)/ ___) ★| """
    print """                 |★ \___ \/ (_/\( () ) )(  \___ \ ★| """
    print """                 |★ (____/\____/ \__/ (__) (____/ ★| """
    print """                 |★                               ★| """
    print """                 |===_______===_______===_______===| """
    print """                 ||★|%s|★|%s|★|%s|★|| """ % (boxes[0][0], boxes[1][0], boxes[2][0])
    print """                 ||★|%s|★|%s|★|%s|★|| """ % (boxes[0][1], boxes[1][1], boxes[2][1])
    print """                 ||★|%s|★|%s|★|%s|★|| """ % (boxes[0][2], boxes[1][2], boxes[2][2])
    print """                 ||★|%s|★|%s|★|%s|★|| __ """ % (boxes[0][3], boxes[1][3], boxes[2][3])
    print """                 ||★|_______|★|_______|★|_______|★||(__) """
    print """                 |===_______===_______===_______===| || """
    print """                 ||★|%s|★|%s|★|%s|★|| || """ % (boxes[3][0], boxes[4][0], boxes[5][0])
    print """                 ||★|%s|★|%s|★|%s|★|| || """ % (boxes[3][1], boxes[4][1], boxes[5][1])
    print """                 ||★|%s|★|%s|★|%s|★|| || """ % (boxes[3][2], boxes[4][2], boxes[5][2])
    print """                 ||★|%s|★|%s|★|%s|★|| || """ % (boxes[3][3], boxes[4][3], boxes[5][3])
    print """                 ||★|_______|★|_______|★|_______|★||_// """
    print """                 |===_______===_______===_______===|_/ """
    print """                 ||★|%s|★|%s|★|%s|★|| """ % (boxes[6][0], boxes[7][0], boxes[8][0])
    print """                 ||★|%s|★|%s|★|%s|★|| """ % (boxes[6][1], boxes[7][1], boxes[8][1])
    print """                 ||★|%s|★|%s|★|%s|★|| """ % (boxes[6][2], boxes[7][2], boxes[8][2])
    print """                 ||★|%s|★|%s|★|%s|★|| """ % (boxes[6][3], boxes[7][3], boxes[8][3])
    print """                _||★|_______|★|_______|★|_______|★||_ """
    print """               (_____________________________________) \n""",

    #By default, win is false
    win = False

    #If one of the victory conditions are met, change victory to true

    #Horizontal
    for i in [0, 3, 6]:
        if boxes[i] == boxes[i+1] == boxes[i+2]:
            win = True

    #Vertical
    for i in [0, 1, 2]:
        if boxes[i] == boxes[i+3] == boxes[i+6]:
            win = True

    #Diagonal
    if boxes[0] == boxes[4] == boxes[8]:
        win = True
    if boxes[2] == boxes[4] == boxes[6]:
        win = True

    #Loser
    if win == False:
        losses += 1
        print 'You Lost',

    #Winner
    elif win == True:
        wins += 1
        print 'You Won!',

    sys.stdout.flush()

def game():
    global duck, glass, bar, mallet, seven, bell, characters, boxes, wins, losses

    #Welcome message
    print """
       _____ _      ____ _______   __  __          _____ _    _ _____ _   _ ______
      / ____| |    / __ \__   __| |  \/  |   /\   / ____| |  | |_   _| \ | |  ____|
     | (___ | |   | |  | | | |    | \  / |  /  \ | |    | |__| | | | |  \| | |__
      \___ \| |   | |  | | | |    | |\/| | / /\ \| |    |  __  | | | | . ` |  __|
      ____) | |___| |__| | | |    | |  | |/ ____ \ |____| |  | |_| |_| |\  | |____
     |_____/|______\____/  |_|    |_|  |_/_/    \_\_____|_|  |_|_____|_| \_|______|\n"""

    #Declare variables
    wins = 0
    losses = 0

    #Each of the 7 characters, divided into individual lines for printing
    duck = ["  _    "," =')   ","  /_///"," (____>"]
    glass = ["  ___  ","  \ /  ", "   Y   ","  _|_  "]
    bar = [" _____ ","|     |","|*BAR*|","|_____|"]
    mallet = ["  ___  "," (|||) ","   |   ","   |   "]
    seven = ["  ___  "," |_  | ","  / /  ", " /_/   "]
    bell = ["  _o_  "," (   ) "," )   ( ","'-'o'-'"]

    #The spin function chooses a random one of these
    characters = [duck, glass, bar, mallet, seven, bell]

    boxes = ['', '', '', '', '', '', '', '', '']

    sleep(2)

    #Guide
    print """
    Welcome to the slot machine!

    In this machine, there are six characters.

    Duck      Glass     Bar       Mallet    Seven     Bell
      _        ___      _____      ___       ___       _o_
     =')       \ /     |     |    (|||)     |_  |     (   )
      /_///     Y      |*BAR*|      |        / /      )   (
     (____>    _|_     |_____|      |       /_/      '-'o'-'

    The board of the slot machine is 3 by 3.
    To win, the same character must appear 3 times in a row, horizontally, vertically, or diagonally.

    Lose:		   Win:

     7 │ 7 │         7 │   │        │   │        │ 7 │
    ───┼───┼───     ───┼───┼───  ───┼───┼───   ──┼───┼───
       │   │ 7         │ 7 │        │   │        │ 7 │
    ───┼───┼───     ───┼───┼───  ───┼───┼───  ───┼───┼───
       │   │           │   │ 7    7 │ 7 │ 7      │ 7 │

    While playing the slots, press the enter key to spin.
    At the end of a round, type 'q' before you press the enter key to quit.\n"""

    #Mainloop
    while True:

        a = raw_input()

        #If user decides to quit
        if a == 'q':

            #Add wins and losses to leaderboard file
            leaderboard = open('slotsscore.txt', 'r')
            line1 = leaderboard.readline()
            line2 = leaderboard.readline()
            wins += int(line1)
            losses += int (line2)
            leaderboard.close()

            leaderboard = open('slotsscore.txt', 'w')
            leaderboard.write(str(wins)+'\n'+str(losses))
            leaderboard.close()

            break

        else:
            spin()
            
  game()
