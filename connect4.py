# -*- coding: utf-8 -*-

#Text-Based Connect 4 Game
#By Zack Nathan

from time import sleep
from random import random
import sys

#Bold and colours
class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    b = '\033[1m'
    e = '\033[0m'
    cyan = '\033[96m' + '\033[1m'
    magenta = '\033[95m' + '\033[1m'
    blue = '\033[94m' + '\033[1m'
    yellow = '\033[93m' + '\033[1m'
    green = '\033[92m' + '\033[1m'
    red = '\033[91m' + '\033[1m'
    grey = '\033[90m' + '\033[1m'
    brown = '\033[31m' + '\033[1m'
    black = '\033[1m'

    colours = ['red', 'green', 'blue', 'yellow', 'magenta', 'cyan', 'black', 'grey', 'brown']

#Function to neatly print the array
def printboard(otherplayer, choice):
    print ''
    print color.BOLD + 'Turn %s' % turn + color.END
    print '┌───┬───┬───┬───┬───┬───┬───┐'
    print '│ 1 │ 2 │ 3 │ 4 │ 5 │ 6 │ 7 │'
    print '├───┼───┼───┼───┼───┼───┼───┤'
    for x in range(0, 6):
        print '│ %s │ %s │ %s │ %s │ %s │ %s │ %s │' % (array[7*x+0], array[7*x+1], array[7*x+2], array[7*x+3], array[7*x+4], array[7*x+5], array[7*x+6])#Row in the array
        print '├───┼───┼───┼───┼───┼───┼───┤'
    print '│ %s │ %s │ %s │ %s │ %s │ %s │ %s │' % (array[42], array[43], array[44], array[45], array[46], array[47], array[48])#Bottom row
    print '└───┴───┴───┴───┴───┴───┴───┘'
    if turn > 1:
        print 'Player %s chose column %s' % (otherplayer, choice)
    print ''

#Fuction to process column choice
def place(choice, char):
    column = choice-1
    if array[column+42] == ' ':
        array[column+42] = char
        placeloop = False
    elif array[column+35] == ' ':
        array[column+35] = char
        placeloop = False
    elif array[column+28] == ' ':
        array[column+28] = char
        placeloop = False
    elif array[column+21] == ' ':
        array[column+21] = char
        placeloop = False
    elif array[column+14] == ' ':
        array[column+14] = char
        placeloop = False
    elif array[column+7] == ' ':
        array[column+7] = char
        placeloop = False
    elif array[column] == ' ':
        array[column] = char
        placeloop = False
    else:
        print color.BOLD + 'Column %s is full, pick a different column' % choice + color.END
        placeloop = True
        #Tell the player the column is full, and they will choose a new column

#Function to detect if somebody has won
def windetect(player, char):
    global gameloop

    #Vertical
    for y in range(28):#Iterate through the first 4 rows of the array
        if array[y] == char and array[y+7] == char and array[y+14] == char and array[y+21] == char:#Check if space(y) and the 3 below it are the same
            print ''#Print the message telling who won the game, and where
            print color.BOLD + 'Player %s (%s) Wins In %s Turns' % (player, char, str(turn)) + color.END
            print color.BOLD + 'Vertical, Column %s, Row %s And Down' % ((y%7)+1, (y/7)+1) + color.END
            gameloop = False#Exit the loop to finish the game

    #Horizontal
    for i in range(0, 46):#Iterate through the entire array except for the last 3 spaces
        if i%7 == 0 or i%7 == 1 or i%7 == 2 or i%7 == 3:#Using the modulo operator, only check the first 4 columns
            if array[i] == char and array[i+1] == char and array[i+2] == char and array[i+3] == char:#Check if space(i) and the three to it's right are the same
                print ''#Print the message telling who won the game, and where
                print color.BOLD + 'Player %s (%s) Wins In %s Turns' % (player, char, str(turn)) + color.END
                print color.BOLD + 'Horizontal, Row %s' % ((i/7)+1) + color.END
                gameloop = False#Exit the loop to finish the game

    #Diagonal
    for j in range(21, 49):#Iterate through the bottom 4 rows of the array

        #Northeast
        if j%7 == 0 or j%7 == 1 or j%7 == 2 or j%7 == 3:#Using the modulo operator, only check the first 4 columns
            if array[j] == char and array[j-6] == char and array[j-12] == char and array[j-18] == char:#Check if space(j) and the three to it's upper right (6 spaces back in the array) are the same
                print ''#Print the message telling who won the game, and where
                print color.BOLD + 'Player %s (%s) Wins In %s Turns' % (player, char, str(turn)) + color.END
                print color.BOLD + 'Diagonally (Up and to the Right), Columns %s to %s' % (((j%7)+1), ((j%7)+4)) + color.END
                gameloop = False#Exit the loop to finish the game

        #Northwest
        if j%7 == 3 or j%7 == 4 or j%7 == 5 or j%7 == 6:#Using the modulo operator, only check the first 4 columns
            if array[j] == char and array[j-8] == char and array[j-16] == char and array[j-24] == char:#Check if space(j) and the three to it's upper left (8 spaces back in the array) are the same
                print ''#Print the message telling who won the game, and where
                print color.BOLD + 'Player %s (%s) Wins In %s Turns' % (player, char, str(turn)) + color.END
                print color.BOLD + 'Diagonally (Up and to the Left), Columns %s to %s' % (((j%7)-3), ((j%7)+1)) + color.END
                gameloop = False#Exit the loop to finish the game

def game():
    global turn, array, gameloop

    print '\n    _____ ____  _   _ _   _ ______ _____ _______    _  _   '
    print '   / ____/ __ \| \ | | \ | |  ____/ ____|__   __|  | || |  '
    print '  | |   | |  | |  \| |  \| | |__ | |       | |     | || |_ '
    print '  | |   | |  | | . ` | . ` |  __|| |       | |     |__   _|'
    print '  | |___| |__| | |\  | |\  | |___| |____   | |        | |  '
    print '   \_____\____/|_| \_|_| \_|______\_____|  |_|        |_|  \n'

    array = [
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ',
    ' ', ' ', ' ', ' ', ' ', ' ', ' ']

    gameloop = True
    turn = 1
    p1col = 0
    p2col = 0

    #Player 1 picks character
    p1char = raw_input('Player 1, select your character (Number or capital letter recommended): ')
    while len(p1char) != 1 or p1char == ' ':
        p1char = raw_input(color.BOLD + 'One character only: ' + color.END)
        if len(p1char) == 1 and p1char != ' ':
            break

    #Player 1 picks colour
    while True:
        print '\nred, green, blue, yellow, magenta, cyan, brown, black, grey'
        colour = raw_input('Player 1, select your colour: ')
        if colour in color.colours:
            if colour == 'red':
                p1char = color.red + p1char + color.e
            elif colour == 'green':
                p1char = color.green + p1char + color.e
            elif colour == 'blue':
                p1char = color.blue + p1char + color.e
            elif colour == 'yellow':
                p1char = color.yellow + p1char + color.e
            elif colour == 'magenta':
                p1char = color.magenta + p1char + color.e
            elif colour == 'cyan':
                p1char = color.cyan + p1char + color.e
            elif colour == 'black':
                p1char = color.black + p1char + color.e
            elif colour == 'grey':
                p1char = color.grey + p1char + color.e
            elif colour == 'brown':
                p1char = color.brown + p1char + color.e
            else:
                print color.b + 'Error' + color.e
            break

    #Player 2 picks character
    p2char = raw_input('\nPlayer 2, select your character (Number or capital letter recommended): ')
    while len(p2char) != 1 or p2char == ' ':
        p2char = raw_input(color.BOLD + 'One character only: ' + color.END)
        if len(p2char) == 1 and p2char != ' ':
            break

    #Player 2 picks colour
    while True:
        print '\nred, green, blue, yellow, magenta, cyan, brown, black, grey'
        colour = raw_input('Player 2, select your colour: ')
        if colour in color.colours:
            if colour == 'red':
                p2char = color.red + p2char + color.e
            elif colour == 'green':
                p2char = color.green + p2char + color.e
            elif colour == 'blue':
                p2char = color.blue + p2char + color.e
            elif colour == 'yellow':
                p2char = color.yellow + p2char + color.e
            elif colour == 'magenta':
                p2char = color.magenta + p2char + color.e
            elif colour == 'cyan':
                p2char = color.cyan + p2char + color.e
            elif colour == 'black':
                p2char = color.black + p2char + color.e
            elif colour == 'grey':
                p2char = color.grey + p2char + color.e
            elif colour == 'brown':
                p2char = color.brown + p2char + color.e
            else:
                print color.b + 'Error' + color.e
            break

    #Pick a new character if player 2's character is the same as player 1's
    while p2char == p1char:
        p2char = raw_input(color.BOLD + 'Already taken, select a new character: ' + color.END)
        while len(p2char) != 1 or p2char == ' ':
            p2char = raw_input(color.BOLD + 'One character only: ' + color.END)
            if len(p2char) == 1 and p2char != ' ':
                break

    #Main loop of the game. When set to False (if somebody wins or the board fills up), the game ends
    while gameloop is True:

        #Print the board
        printboard(2, p2col)

        #Player 1's Turn
        placeloop = True
        while placeloop is True:
            p1colchoice = raw_input('Player 1 (%s): Which column? ' % p1char)
            if p1colchoice in ['1', '2', '3', '4', '5', '6', '7']:
                p1col = int(p1colchoice)
                place(p1col, p1char)
                break
            else:
                print color.BOLD + 'Column %s does not exist, pick a different column' % p1colchoice + color.END

        #Run the win detection function for player 1
        windetect(1, p1char)

        #If the board is full, end the game
        if turn == 26:
            print color.BOLD + 'Nobody Wins, the Board is Full' + color.END
            gameloop = False

        #If player 1 won the game, end it now instead of after player 2's turn
        if gameloop == False:
            break

        #Print the board
        printboard(1, p1col)

        #Player 2's Turn
        placeloop = True
        while placeloop is True:
            p2colchoice = raw_input('Player 2 (%s): Which column? ' % p2char)
            if p2colchoice in ['1', '2', '3', '4', '5', '6', '7']:
                p2col = int(p2colchoice)
                place(p2col, p2char)
                break
            else:
                print color.BOLD + 'Column %s does not exist, pick a different column' % p2colchoice + color.END

        #Run the win detection function for player 2
        windetect(2, p2char)

        turn += 1

        if gameloop == False:
            break

    #What to do after the game is over:
    print '┌───┬───┬───┬───┬───┬───┬───┐'
    for x in range(0, 6):
        print '│ %s │ %s │ %s │ %s │ %s │ %s │ %s │' % (array[7*x+0], array[7*x+1], array[7*x+2], array[7*x+3], array[7*x+4], array[7*x+5], array[7*x+6])
        print '├───┼───┼───┼───┼───┼───┼───┤'
    print '│ %s │ %s │ %s │ %s │ %s │ %s │ %s │' % (array[42], array[43], array[44], array[45], array[46], array[47], array[48])
    print '└───┴───┴───┴───┴───┴───┴───┘'
    print color.BOLD + 'GAME OVER\n' + color.END

    #Read 3 fastest wins from the file, if the current game is one of them, ask for a name to add to the list
    leaderboard = open('connect4leaderboard.txt', 'r')
    line1 = leaderboard.readline()
    line2 = leaderboard.readline()
    line3 = leaderboard.readline()
    data = [line1.split(' '), line2.split(' '), line3.split(' ')]
    leaderboard.close()

    #Create a list of values, each element is a game length
    for i in range(3):
        try:
            data[i][1] = int(data[i][1])
        except IndexError:
            data[i] = ['', 99]

    sleep(2)
    leader = False

    #New record
    if turn < data[0][1]:
        data[2] = data[1]
        data[1] = data[0]
        while True:
            print '\nCongratulations, you have won Connect 4 in the fastest time yet!'
            a = raw_input(color.b + 'Please enter your name: ' + color.e)
            if len(a) <= 12:
                data[0] = [a, turn]
                leader = True
                break
            print color.b + 'Maximum name length of 12 characters, you entered %d' % len(a) + color.e

    #New second place
    elif turn < data[1][1]:
        data[2] = data[1]
        while True:
            print '\nCongratulations, you have won Connect 4 in the second fastest time yet!'
            a = raw_input(color.b + 'Please enter your name: ' + color.e)
            if len(a) <= 12:
                data[1] = [a, turn]
                leader = True
                break
            print color.b + 'Maximum name length of 12 characters, you entered %d' % len(a) + color.e

    #New third place
    elif turn < data[2][1]:
        while True:
            print '\nCongratulations, you have won Connect 4 in the third fastest time yet!'
            a = raw_input(color.b + 'Please enter your name: ' + color.e)
            if len(a) <= 12:
                data[2] = [a, turn]
                leader = True
                break
            print color.b + 'Maximum name length of 12 characters, you entered %d' % len(a) + color.e


    #Erase the empty games so that they are not written to the file
    if data[2] == ['', 99]:
        data.pop(2)

    if data[1] == ['', 99]:
        data.pop(1)

    if data[0] == ['', 99]:
        data.pop(0)

    #If there is a change, rewrite the leaderboard file
    if leader is True:
        leaderboard = open('connect4leaderboard.txt', 'w')
        for i in range(len(data)):
            leaderboard.write(data[i][0] + ' ' + str(data[i][1]))
            if i != len(data) - 1:
                leaderboard.write('\n')
        leaderboard.close()

    #Ask the users if they want to play again
    while True:
        again = raw_input('\nWould you like to play again? (y/n) ')
        if again == 'y':
            game()
        elif again == 'n':
            break
        else:
            print color.b + '\nInvalid selection, please try again' + color.e
            
  game()
