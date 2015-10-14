# -*- coding: utf-8 -*-

#Text-Based Roulette Game
#By Zack Nathan

from random import randint
from time import sleep

class color:
    b = '\033[1m'
    e = '\033[0m'
    red = '\033[91m'
    g = '\033[92m'

#Print the roulette board at the start of every turn. Also display the current number of chips
def printboard():
    print '\n┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬───────┐'
    print '│    │ '+color.red+'3'+color.e+'  │ 6  │ '+color.red+'9'+color.e+'  │ '+color.red+'12'+color.e+' │ 15 │ '+color.red+'18'+color.e+' │ '+color.red+'21'+color.e+' │ 24 │ '+color.red+'27'+color.e+' │ '+color.red+'30'+color.e+' │ 33 │ '+color.red+'36'+color.e+' │ Row 1 │'
    print '│ '+color.g+'0'+color.e+'  ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───────┤'
    print '├────┤ 2  │ '+color.red+'5'+color.e+'  │ 8  │ 11 │ '+color.red+'14'+color.e+' │ 17 │ 20 │ '+color.red+'23'+color.e+' │ 26 │ 29 │ '+color.red+'32'+color.e+' │ 35 │ Row 2 │'
    print '│ '+color.g+'00'+color.e+' ├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼───────┤'
    print '│    │ '+color.red+'1'+color.e+'  │ 4  │ '+color.red+'7'+color.e+'  │ 10 │ 13 │ '+color.red+'16'+color.e+' │ '+color.red+'19'+color.e+' │ 22 │ '+color.red+'25'+color.e+' │ 28 │ 31 │ '+color.red+'34'+color.e+' │ Row 3 │'
    print '└────┼────┴────┴────┴────┼────┴────┴────┴────┼────┴────┴────┴────┼───────┘'
    print '     │      1st 12       │      2nd 12       │      3rd 12       │     '
    print '     ├─────────┬─────────┼─────────┬─────────┼─────────┬─────────┤     '
    print '     │ 1 to 18 │  Even   │   '+color.red+'Red'+color.e+'   │  Black  │   Odd   │19 to 36 │     '
    print '     └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘     '
    print color.b + '                      You currently have %s chips' % chips + color.e
    print '\nTo place your bet, type the name of the space exactly as it appears on the board'

#Picks a random number off of the roulette board (0 - 36 and 00)
def random():
    num = randint(0, 37)
    if num == 37:
        num = '00'
    return num

#Ask the user for his bet, and process it
def choice():
    global chips, wins, losses
    winner = 0
    num = random()

    #Ask the user how many chips he is betting
    while True:
        betinput = raw_input('\nHow many chips would you like to bet? ')
        if str.isdigit(betinput):
            if 0 < int(betinput) <= chips:
                bet = int(betinput)
                break
            else:
                print color.b + 'You do not have enough chips to make that bet!' + color.e
        else:
            print color.b + 'Your bet is invalid, please enter an integer' + color.e

    #Ask where the user is placing his bet
    while True:
        choice = raw_input('\nWhere would you like to place your bet? ')
        if choice in betlist:
            break
        else:
            print color.b + 'Invalid choice, type your bet exactly how it appears on the board' + color.e

    #All of these win detection blocks are very similar
    #If you bet this:
    if choice == '00':
        #And the number was this:
        if num == '00':
            #You win back [winner] times your money
            #If the user loses, winner = 0
            winner = 36
    else:
        num = int(num)

    if choice == '1st 12':
        if 0 < num <= 12:
            winner = 3
        else:
            winner = 0

    elif choice == '2nd 12':
        if 12 < num <= 24:
            winner = 3
        else:
            winner = 0

    elif choice == '3rd 12':
        if 24 < num <= 36:
            winner = 3
        else:
            winner = 0

    elif choice == 'Even' or choice == 'even':
        if num % 2 == 0:
            winner = 2
        else:
            winner = 0

    elif choice == 'Odd' or choice == 'odd':
        if num % 2 == 1:
            winner = 2
        else:
            winner = 0

    elif choice == 'Red' or choice == 'red':
        if num in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
            winner = 2
        else:
            winner = 0

    elif choice == 'Black' or choice == 'black':
        if num in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
            winner = 2
        else:
            winner = 0

    elif choice == '1 to 18':
        if 0 < num <= 18:
            winner = 2
        else:
            winner = 0

    elif choice == '19 to 36':
        if 18 < num <= 36:
            winner = 2
        else:
            winner = 0

    elif choice == 'Row 1' or choice == 'row 1':
        if num % 3 == 0:
            winner = 3
        else:
            winner = 0

    elif choice == 'Row 2' or choice == 'row 2':
        if num % 3 == 2:
            winner = 3
        else:
            winner = 0

    elif choice == 'Row 3' or choice == 'row 3':
        if num % 3 == 1:
            winner = 3
        else:
            winner = 0
            losses += 1

    elif choice == num:
        winner = 36

    #If none of the win conditions were met
    else:
        winner = 0

    #Winner!
    if winner > 0:
        print color.b + 'Congratulations you won!' + color.e
        wins += 1
    #Loser
    else:
        print color.b + 'You lost!' + color.e
        losses += 1

    sleep(1)

    #Say what the number was
    print color.b + 'The number was %s' % str(num) + color.e

    #Adjust the number of chips based on whether the user won or lost, and how much they bet
    chips = (chips - bet) + (bet * winner)

    sleep(3)

#Main program function
def game():
    global betlist, chips, wins, losses

    #List of possible bets
    betlist = ['Row 1', 'row 1', 'Row 2', 'row 2', 'Row 3', 'row 3', '1st 12', '2nd 12', '3rd 12', '0', '00', '1 to 18', '19 to 36', 'Even', 'even', 'Odd', 'odd', 'Red', 'red', 'Black', 'black']
    #Add the single numbers to the list of possible bets
    for i in range(1, 37):
        betlist.append(str(i))

    #Declare variables
    chips = 100
    wins = 0
    losses = 0
    leave = False

    #Welcome message
    print '\n _____   ____  _    _ _      ______ _______ _______ ______ '
    print '|  __ \ / __ \| |  | | |    |  ____|__   __|__   __|  ____|'
    print '| |__) | |  | | |  | | |    | |__     | |     | |  | |__   '
    print '|  _  /| |  | | |  | | |    |  __|    | |     | |  |  __|  '
    print '| | \ \| |__| | |__| | |____| |____   | |     | |  | |____ '
    print '|_|  \_|\____/ \____/|______|______|  |_|     |_|  |______|\n'

    #Each one of these loops if one turn
    while True:

        #Print the board
        printboard()

        #If you run out of chips, restart the game
        if chips <= 0:
            print color.b + '\n       GAME OVER' + color.e
            sleep(1)
            print color.b + '\nYou have run out of money!' + color.e
            sleep(2)
            print color.b + '\nRespawning...' + color.e
            sleep(3)
            game()

        #Ask for bets, then process
        choice()

        #Would you like to play again?
        while True:
            again = raw_input('\nWould you like to play again? (y/n) ')
            if again == 'y' or again == 'yes':
                leave = False
                break
            elif again == 'n' or again == 'no':

                #Add wins and losses to leaderboard file before the user leaves
                leaderboard = open('roulettescore.txt', 'r')
                line1 = leaderboard.readline()
                line2 = leaderboard.readline()
                wins += int(line1)
                losses += int (line2)
                leaderboard.close()

                leaderboard = open('roulettescore.txt', 'w')
                leaderboard.write(str(wins)+'\n'+str(losses))
                leaderboard.close()
                
                leave = True
                break
            else:
                print color.b + '\nInvalid selection, please try again' + color.e
        
        if leave == True:
            break
            
  game()
