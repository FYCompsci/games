# -*- coding: utf-8 -*-

#Text-Based Blackjack game
#By Zack Nathan

from random import randint, choice
from time import sleep

class color:
    BOLD = '\033[1m'
    END = '\033[0m'
    b = '\033[1m'
    e = '\033[0m'
    red = '\033[91m'
    rb = '\033[91m'+'\033[1m'
    g = '\033[92m'

#After each turn, start with a blank hand
def resethand():
    global hand, line1, line2, line3, line4, line5, line6, line7
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    line5 = ''
    line6 = ''
    line7 = ''

#Pick a random card from the deck and add it to the hand
def getcard():
    global hand, line1, line2, line3, line4, line5, line6, line7, cards, suits

    #Random numbers for suit and value
    suit = randint(0, 3)
    suit = suits[suit]
    card = randint(0, 12)
    card = cards[card]

    #Print red and black cards
    if suit == color.rb + '♦' + color.e or suit == color.rb + '♥' + color.e:
        printcard = color.rb + card + color.e
    else:
        printcard = color.b + card + color.e

    '''
    The hand is split in to 2 parts.

    The first part is the hand variable, which is a list.
    Each element in the list is the value of one of the cards in the hand, and sum(hand) is its value

    The second part is for printing the hand, and only for graphics.
    It is split into 7 different lines because python prints from top to bottom.
    For example, line4 will contain the 4th lines of all the cards.
    '''

    #The top 2 and bottom 2 rows are almost identical in every card. This method is more efficient and easier
    #The printcard variable is the colourized number which appears in the corners of the card
    if card != '10':
        line1 += ".------."
        line2 += "|%s.--. |" % printcard

        line6 += "| '--'%s|" % printcard
        line7 += "`------'"

    else:
        line1 += ".------."
        line2 += "|%s--. |" % printcard

        line6 += "| '--%s|" % printcard
        line7 += "`------'"

    #Depending on the card, set the middle 3 lines
    if card == '2':
        line3 += "| |  | |"
        line4 += "| |%s%s| |" % (suit, suit)
        line5 += "| |  | |"
        hand.append(2)

    elif card == '3':
        line3 += "| |%s%s| |" % (suit, suit)
        line4 += "| |  | |"
        line5 += "| |%s | |" % suit
        hand.append(3)

    elif card == '4':
        line3 += "| |%s%s| |" % (suit, suit)
        line4 += "| |  | |"
        line5 += "| |%s%s| |" % (suit, suit)
        hand.append(4)

    elif card == '5':
        line3 += "| |%s%s| |" % (suit, suit)
        line4 += "| |%s%s| |" % (suit, suit)
        line5 += "| |%s | |" % suit
        hand.append(5)

    elif card == '6':
        line3 += "| |%s%s| |" % (suit, suit)
        line4 += "| |%s%s| |" % (suit, suit)
        line5 += "| |%s%s| |" % (suit, suit)
        hand.append(6)

    elif card == '7':
        line3 += "| %s%s%s| |" % (suit, suit, suit)
        line4 += "| |%s%s| |" % (suit, suit)
        line5 += "| |%s%s| |" % (suit, suit)
        hand.append(7)

    elif card == '8':
        line3 += "| %s%s%s| |" % (suit, suit, suit)
        line4 += "| %s%s%s| |" % (suit, suit, suit)
        line5 += "| |%s%s| |" % (suit, suit)
        hand.append(8)

    elif card == '9':
        line3 += "| %s%s%s| |" % (suit, suit, suit)
        line4 += "| %s%s%s| |" % (suit, suit, suit)
        line5 += "| %s%s%s| |" % (suit, suit, suit)
        hand.append(9)

    elif card == '10':
        line3 += "| %s%s%s%s |" % (suit, suit, suit, suit)
        line4 += "| %s%s%s%s |" % (suit, suit, suit, suit)
        line5 += "| |%s%s| |" % (suit, suit)
        hand.append(10)

    elif card == 'A':
        line3 += "| |  | |"
        line4 += "| |%s | |" % suit
        line5 += "| |  | |"
        hand.append(11)

    #Jack, Queen, and King have identical middle lines
    else:
        line3 += "| |  | |"
        line4 += "| |%s%s| |" % (suit, suit)
        line5 += "| |  | |"
        hand.append(10)

    line1 += '    '
    line2 += '    '
    line3 += '    '
    line4 += '    '
    line5 += '    '
    line6 += '    '
    line7 += '    '

#Function for printing the hand
def printhand():
    global hand
    print line1
    print line2
    print line3
    print line4
    print line5
    print line6
    print line7

#Pick 2 cards for the dealer, with one of them being revealed, just like in real blackjack
def dealershand():
    dealer = choice(values)
    #Don't print 'a ace' or 'a 8'
    if dealer != 11 and dealer != 8:
        print 'The dealer\'s hand is showing a %s' % dealer
    elif dealer == 11:
        print 'The dealer\'s hand is showing an ace'
    else:
        print 'The dealer\'s hand is showing an 8'
    dealer += choice(values)
    return dealer

#The function for every new hand played
def turn():
    global hand, wins, losses, draws
    ace = False

    #Reset, create, and print the hand
    resethand()
    getcard()
    getcard()
    printhand()

    #Print the total value of the hand, and if it contains an ace
    print 'Your hand totals %s' % sum(hand),
    if 11 in hand and 1 not in hand:
        ace = True
        print '(and you have an ace)'
    else:
        ace = False
        print ''
    dealer = dealershand()
    bust = False

    #Loop for asking to hit or stand
    while True:
        #If it is not a bust
        if sum(hand) < 21:
            decision = raw_input('\nWould you like to [h]it or [s]tand? ')
            print ''

            #If they said hit, get a new card
            if decision == 'h' or decision == 'hit':
                getcard()

                #If there is a bust, but the hand contains an ace, change its value from 11 to 1
                if ace == True:
                    if 11 in hand and sum(hand) > 21:
                        print 'Your hand totals %s' % sum(hand)
                        sleep(2)
                        print 'That would be a bust, but one of your cards is an ace.'
                        sleep(2)
                        print 'The ace was worth 11, but now it is worth 1.\n'
                        hand.remove(11)
                        hand.append(1)
                    else:
                        bust = True
                        break

            elif decision == 's' or decision == 'stand':
                break

            else:
                print color.b + 'Invalid selection, please try again' + color.e

            printhand()
            print 'Your hand totals %s\n' % sum(hand)

            #Bust
            if sum(hand) > 21:
                bust = True
                break

        else:
            break

    #Loop for processing who won the turn
    while True:

        sleep(1)

        #Bust
        if bust == True:
            print color.b +'BUST' + color.e
            print 'You Lose!'
            losses += 1
            break

        #Just like real blackjack, the dealer takes more cards while his hand totals less than 17
        i = 0
        while dealer < 17:
            dealer += choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])
            i += 1

        #Tell the user how many more cards the dealer took
        if i != 1:
            print 'The dealer took %s more cards' % i
        else:
            print 'The dealer took 1 more card'

        #Dealer bust
        if dealer > 21:
            print 'The dealer has %s' % dealer
            sleep(1)
            print 'The dealer busted! You Win!'
            wins += 1
            break

        #If the user's hand is 21, they will win unless the dealer also has 21, in which case it's a draw
        if hand == 21:
            print 'You have 21!'

            if dealer == 21:
                sleep(1)
                print color.b + 'But so does the dealer' + color.e
                sleep(1)
                print "It's a draw!"
                draws += 1
                break

            else:
                print 'The dealer has %s\n' % dealer
                sleep(1)
                print 'You win!'
                wins += 1
                break

        #Tell how much the dealer has
        print 'The dealer has %s\n' % dealer

        sleep(1)
        #Who has more, win, loss, or draw
        if dealer > sum(hand):
            print 'You lose!'
            losses += 1
            break
        elif sum(hand) > dealer:
            print 'You win!'
            wins += 1
            break
        else:
            print "It's a draw!"
            draws += 1
            break

#Main program function
def game():
    global line1, line2, line3, line4, line5, line6, line7, hand, cards, suits, values, wins, losses, draws

    #Welcome message
    print '\n  ____  _               _____ _  __    _         _____ _  __'
    print ' |  _ \| |        /\   / ____| |/ /   | |  /\   / ____| |/ /'
    print " | |_) | |       /  \ | |    | ' /    | | /  \ | |    | ' /"
    print ' |  _ <| |      / /\ \| |    |  < _   | |/ /\ \| |    |  <'
    print ' | |_) | |____ / ____ \ |____| . \ |__| / ____ \ |____| . \\'
    print ' |____/|______/_/    \_\_____|_|\_\____/_/    \_\_____|_|\_\\\n'

    #Declare all game variables
    wins = 0
    losses = 0
    draws = 0
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''
    line5 = ''
    line6 = ''
    line7 = ''
    hand = []
    cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [color.b + '♣' + color.e, color.rb + '♦' + color.e, color.rb + '♥' + color.e, color.b + '♠' + color.e]
    values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    mainloop = True
    while mainloop is True:
        #Empty the hand every turn
        hand = []

        sleep(1)
        turn()
        sleep(1)

        #Ask if the user wants to play again
        againloop = True
        while againloop is True:
            again = raw_input('\nWould you like to play again? (y/n) ')
            if again == 'y' or again == 'yes':
                break
            elif again == 'n' or again == 'no':
                mainloop = False

                #If they don't, add the number of wins, losses, and draws to the leaderboard file then leave
                leaderboard = open('blackjackscore.txt', 'r')
                line1 = leaderboard.readline()
                line2 = leaderboard.readline()
                line3 = leaderboard.readline()
                wins += int(line1)
                losses += int(line2)
                draws += int(line3)
                leaderboard.close()
                leaderboard = open('blackjackscore.txt', 'w')
                leaderboard.write(str(wins)+'\n'+str(losses)+'\n'+str(draws))
                leaderboard.close()

                break
            else:
                print color.b + '\nInvalid selection, please try again' + color.e
        print ''
        
  game()
