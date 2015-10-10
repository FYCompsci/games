__author__ = 'julian.samek'

import sys
import os
import random
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640, 660))
pygame.display.set_caption("2048")

while True:
    score = 0
    gameoverpage = False
    gamewon = False

    fileo = open("2048 highscore.txt")
    highscore = int(fileo.readline())
    fileo.close()

    col1 = ["    ", "    ", "    ", "    "]
    col2 = ["    ", "    ", "    ", "    "]
    col3 = ["    ", "    ", "    ", "    "]
    col4 = ["    ", "    ", "    ", "    "]

    row1 = ["    ", "    ", "    ", "    "]
    row2 = ["    ", "    ", "    ", "    "]
    row3 = ["    ", "    ", "    ", "    "]
    row4 = ["    ", "    ", "    ", "    "]

    # find which colours go with which tiles
    colourlist = []
    filecolours = open("2048 colours.txt")
    for line in filecolours:
        line = line.split("*")
        colour = line[1].split(",")
        for i in range(3):
            colour[i] = int(colour[i])
        colourlist.append(colour)
    filecolours.close()

    numlist = ["  2 ","  4 ","  8 "," 16 "," 32 "," 64 "," 128"," 256"," 512","1024","2048","4096","8912"]

    # create a function to print the board to the screen
    def printboard():

        # draw rectangles to form the board, with no squares on it
        pygame.draw.rect(screen,(205,192,176),(140,200,360,360),0)
        for i in range(5):
            pygame.draw.rect(screen,(139,131,120),(140 + (i * 90),200,10,360),0)
        for i in range(5):
            pygame.draw.rect(screen,(139,131,120),(140,200 + (i * 90),370,10),0)

        # type up the title for the board
        font = pygame.font.SysFont('Marker Felt', 75)
        screen.blit(font.render('2048', True, (139,119,101)), (35, 50))

        # type the message saying the instructions
        font = pygame.font.SysFont('Marker Felt', 30)
        screen.blit(font.render("Join the numbers to get the 2048 tile!", True, (139,119,101)), (90, 150))

        # create the score and high score boxes
        pygame.draw.rect(screen,(205,192,176),(230,50,150,75),0)
        pygame.draw.rect(screen,(205,192,176),(405,50,150,75),0)

        # type the score and highscore
        font = pygame.font.SysFont('Marker Felt', 20)
        screen.blit(font.render("Score", True, (211,211,211)), (285, 60))
        screen.blit(font.render("High Score", True, (211,211,211)), (440, 60))
        screen.blit(font.render(str(score), True, (255,255,255)), (240, 90))
        screen.blit(font.render(str(highscore), True, (255,255,255)), (425, 90))

        def printtiles(col,movedown):
            # now add the tiles
            # remember, each tile is now only 80 by 80, not 90 by 90
            for i in range(4):
                if col[i] != "    " and col[i] in numlist:
                    # this makes the square
                    position = numlist.index(col[i])
                    colour = colourlist[position]
                    pygame.draw.rect(screen,colour,(150 + (i * 90),(210 + movedown),80,80),0)
                    # now type in the tile's value
                    font = pygame.font.SysFont('Marker Felt', 30)
                    screen.blit(font.render(col[i], True, (139,119,101)), (155 + (i * 90), (235 + movedown)))

        printtiles(col1,0)
        printtiles(col2,90)
        printtiles(col3,180)
        printtiles(col4,270)

        # now print the final box, the new game box to the screen
        pygame.draw.rect(screen,(205,192,176),(100,580,440,60),0)
        font = pygame.font.SysFont('Marker Felt', 40)
        screen.blit(font.render("Click Here for a New Game", True, (235,235,235)), (110, 590))

    # create a function to set the row values
    #  this will be important, as when the values of the items in a column are changed, the values of the items in a row should change as well
    def setrow():
        # use global variables so that the variables may be accessed outside the function
        global row1
        global row2
        global row3
        global row4
        # reset the values of the rows to be accurate
        row1 = [col1[0], col2[0], col3[0], col4[0]]
        row2 = [col1[1], col2[1], col3[1], col4[1]]
        row3 = [col1[2], col2[2], col3[2], col4[2]]
        row4 = [col1[3], col2[3], col3[3], col4[3]]

    # re-define the values of the columns, to be accurate. This will be used when the values of the rows are changed
    def setcol():
        # use global variables so that the variables may be accessed outside the function
        global col1
        global col2
        global col3
        global col4
        col1 = [row1[0], row2[0], row3[0], row4[0]]
        col2 = [row1[1], row2[1], row3[1], row4[1]]
        col3 = [row1[2], row2[2], row3[2], row4[2]]
        col4 = [row1[3], row2[3], row3[3], row4[3]]

    def right(col):
        global newlist
        newlist = []
        for i in range(4):
            if col[i] == "    ":
                newlist.insert(0, "    ")
            else:
                newlist.append(col[i])

    def left(col):
        global newlist
        newlist = []
        newlist2 = []
        for i in range(4):
            if col[i] == "    ":
                newlist2.append("    ")
            else:
                newlist.append(col[i])
        newlist.extend(newlist2)

    def up(row):
        global newlist
        newlist = []
        newlist2 = []
        for i in range(4):
            if row[i] == "    ":
                newlist2.append("    ")
            else:
                newlist.append(row[i])
        newlist.extend(newlist2)

    def down(row):
        global newlist
        newlist = []
        for i in range(4):
            if row[i] == "    ":
                newlist.insert(0, "    ")
            else:
                newlist.append(row[i])

    def addnew():
        count = 0
        for num in range(4):
            if col1[num] == "    ":
                count += 1
        for num in range(4):
            if col2[num] == "    ":
                count += 1
        for num in range(4):
            if col3[num] == "    ":
                count += 1
        for num in range(4):
            if col4[num] == "    ":
                count += 1

        number = random.randint(0, (count - 1))

        count2 = 0
        while count2 <= number:
            for num in range(4):
                if col1[num] == "    ":
                    count2 += 1
                    if count2 == (number + 1):
                        col1[num] = "  2 "
                        count2 = 1000000
                        break

            if count2 <= number:
                for num in range(4):
                    if col2[num] == "    ":
                        count2 += 1
                        if count2 == (number + 1):
                            col2[num] = "  2 "
                            count2 = 1000000
                            break

            if count2 <= number:
                for num in range(4):
                    if col3[num] == "    ":
                        count2 += 1
                        if count2 == (number + 1):
                            col3[num] = "  2 "
                            count2 = 1000000
                            break

            if count2 <= number:
                for num in range(4):
                    if col4[num] == "    ":
                        count2 += 1
                        if count2 == (number + 1):
                            col4[num] = "  2 "
                            count2 = 1000000
                            break

    # now define the functions to add up the numbers into one larger tile
    def addtiles(col,pos1,pos2):
        global score
        global newcolumn
        newcolumn = []

        if col[pos1] == col[pos2] and col[pos1] != "    ":
            oldnum = ""
            for i in col[pos1]:
                if i != " ":
                    oldnum += i
            oldnum = int(oldnum)
            oldnum = oldnum * 2
            oldnum = str(oldnum)

            if len(oldnum) == 1:
                newcolumn.append("  %s " % oldnum)
                score += int(oldnum)

            elif len(oldnum) == 2:
                newcolumn.append(" %s " % oldnum)
                score += int(oldnum)

            elif len(oldnum) == 3:
                newcolumn.append(" %s" % oldnum)
                score += int(oldnum)

            elif len(oldnum) == 4:
                newcolumn.append("%s" % oldnum)
                score += int(oldnum)

            else:
                global gamewon
                gamewon = True

            newcolumn.append("    ")

    # now define the functions to check if the game is over
    # check to see if the board is filled
    # if it has no empty spots, then gameover = 0
    def isdone(col):
        global gameover
        for num in col:
            if num == "    ":
                gameover += 1

    # check to see if two spots can add together
    # if there are no spaces where two tiles can add together, then gameover = 0
    def canadd(col):
        global gameover
        for i in range(3):
            if col[i] == col[i + 1]:
                gameover += 1

    # this variable contains a list of the list
    allcol = [col1,col2,col3,col4]

    # pick two random spots and make them both equal 2
    # this will usually pick two different spots, but every one and a while, the same spot will be picked twice (but this is wanted)
    allcol[random.randint(0,3)][random.randint(0,3)] = "  2 "
    allcol[random.randint(0,3)][random.randint(0,3)] = "  2 "

    # now, add these changes to our rows
    setrow()

    # now print the board
    screen.fill((235,235,235))
    printboard()
    # update the screen
    pygame.display.update()

    ###################################################
    ###################################################

    # this is the game loop

    ###################################################
    ###################################################

    main_keepgoing = True
    while main_keepgoing:

        # this checks for interaction with the screen
        for event in pygame.event.get():
            if event.type == QUIT:

                # check to see if you should change the highscore
                fileo = open("2048 highscore.txt")
                old_highscore = int(fileo.readline())
                fileo.close()
                # if the new highscore is bigger, then change it
                if highscore > old_highscore:
                    fileo = open("2048 highscore.txt","w")
                    fileo.write(str(highscore))
                    fileo.close()

                sys.exit()

            elif event.type == MOUSEBUTTONDOWN:
                mousepos = pygame.mouse.get_pos()

                if gameoverpage == True:

                    if mousepos[0] >= 190 and mousepos[0] <= 465:
                        if mousepos[1] >= 335 and mousepos[1] <= 415:
                            main_keepgoing = False
                            break

                        elif mousepos[1] >= 440 and mousepos[1] <= 520:

                            # check to see if you should change the high score
                            fileo = open("2048 highscore.txt")
                            old_highscore = int(fileo.readline())
                            fileo.close()
                            # if the new highscore is bigger, then change it
                            if highscore > old_highscore:
                                fileo = open("2048 highscore.txt","w")
                                fileo.write(str(highscore))
                                fileo.close()

                            sys.exit()

            # game detection to see if the game is over
            gameover = 0

            # check to see if all the spots are filled
            isdone(col1)
            isdone(col2)
            isdone(col3)
            isdone(col4)

            # check to see if two tiles can add together anywhere
            canadd(col1)
            canadd(col2)
            canadd(col3)
            canadd(col4)
            canadd(row1)
            canadd(row2)
            canadd(row3)
            canadd(row4)

            # if gameover still equals zero, then all the spots are filled and no two tiles can ad together
            # there fore, the game is over
            if gameover == 0 or gamewon == True:

                if gameoverpage == False:

                    gameoverpage = True

                    # display a message saying they lost, show their score and their options
                    screen.fill((235,235,235))

                    printboard()

                    # this prints a rectangle to the board, its width will be 370 by 370, and the other stuff is to make the rectangle translucent
                    rect1 = pygame.Surface((370,370), pygame.SRCALPHA, 32)
                    # this fills the rectange - the first three are just RGB, and the final item makes the square opaque
                    if gamewon == True:
                        rect1.fill((205,205,95,200))
                    else:
                        rect1.fill((205,192,176,200))
                    # this prints the opaque square
                    screen.blit(rect1, (140,200))

                    # print that they lost
                    font = pygame.font.SysFont('Helvetica Bold', 80)
                    if gamewon == True:
                        screen.blit(font.render("You Win!", True, (139,119,101)), (215, 230))
                    else:
                        screen.blit(font.render("Game Over!", True, (139,119,101)), (160, 230))

                    # print the two menu options: quit or new game
                    font = pygame.font.SysFont('Marker Felt', 60)
                    screen.blit(font.render("New Game", True, (139,119,101)), (200, 345))
                    screen.blit(font.render("Quit", True, (139,119,101)), (265, 450))

                    # now draw small boxes around the two options
                    pygame.draw.rect(screen,(139,119,101),(190,335,275,80),5)
                    pygame.draw.rect(screen,(139,119,101),(190,440,275,80),5)

                    # finally, cover up the old box saying click here for a new game
                    pygame.draw.rect(screen,(235,235,235),(100,580,440,60),0)

                    # update the screen
                    pygame.display.update()

            else:
                if event.type == MOUSEBUTTONDOWN:
                    mousepos = pygame.mouse.get_pos()

                    if mousepos[0] >= 100 and mousepos[0] <= 550 and mousepos[1] >= 580 and mousepos[1] <= 640:
                        main_keepgoing = False

                # if they pressed a key, then check which key they pressed
                elif event.type == KEYDOWN:

                    if event.key == K_q:

                        # check to see if you should change the highscore
                        fileo = open("2048 highscore.txt")
                        old_highscore = int(fileo.readline())
                        fileo.close()
                        # if the new highscore is bigger, then change it
                        if highscore > old_highscore:
                            fileo = open("2048 highscore.txt","w")
                            fileo.write(str(highscore))
                            fileo.close()

                        sys.exit()

                    # if they pressed the right arrow key
                    elif event.key == K_RIGHT:
                        setcol()

                        original = [col1,col2,col3,col4]

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        right(col1)
                        col1 = newlist
                        # add the first batch of tiles
                        addtiles(col1,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col1[2] = newcolumn[1]
                            col1[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            right(col1)
                            col1 = newlist
                        else:
                            addtiles(col1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col1[1] = newcolumn[1]
                                col1[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col1[1] = newcolumn[1]
                                col1[2] = newcolumn[0]
                            else:
                                addtiles(col1,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col1[0] = newcolumn[1]
                                    col1[1] = newcolumn[0]
                        right(col1)
                        col1 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        right(col2)
                        col2 = newlist
                        # add the first batch of tiles
                        addtiles(col2,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col2[2] = newcolumn[1]
                            col2[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            right(col2)
                            col2 = newlist
                        else:
                            addtiles(col2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col2[1] = newcolumn[1]
                                col2[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col2[1] = newcolumn[1]
                                col2[2] = newcolumn[0]
                            else:
                                addtiles(col2,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col2[0] = newcolumn[1]
                                    col2[1] = newcolumn[0]
                        right(col2)
                        col2 = newlist


                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        right(col3)
                        col3 = newlist
                        # add the first batch of tiles
                        addtiles(col3,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col3[2] = newcolumn[1]
                            col3[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            right(col3)
                            col3 = newlist
                        else:
                            addtiles(col3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col3[1] = newcolumn[1]
                                col3[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col3[1] = newcolumn[1]
                                col3[2] = newcolumn[0]
                            else:
                                addtiles(col3,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col3[0] = newcolumn[1]
                                    col3[1] = newcolumn[0]
                        right(col3)
                        col3 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        right(col4)
                        col4 = newlist
                        # add the first batch of tiles
                        addtiles(col4,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col4[2] = newcolumn[1]
                            col4[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            right(col4)
                            col4 = newlist
                        else:
                            addtiles(col4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col4[1] = newcolumn[1]
                                col4[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col4[1] = newcolumn[1]
                                col4[2] = newcolumn[0]
                            else:
                                addtiles(col4,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col4[0] = newcolumn[1]
                                    col4[1] = newcolumn[0]
                        right(col4)
                        col4 = newlist

                        screen.fill((235,235,235))
                        printboard()
                        # update the screen
                        pygame.display.update()

                        if original != [col1,col2,col3,col4]:
                            canyouadd = 0
                            for i in range(4):
                                if col1[i] == "    ":
                                    canyouadd = 1
                                if col2[i] == "    ":
                                    canyouadd = 1
                                if col3[i] == "    ":
                                    canyouadd = 1
                                if col4[i] == "    ":
                                    canyouadd = 1

                            if canyouadd == 1:
                                addnew()

                        setrow()

                    # if they pressed the left arrow key
                    elif event.key == K_LEFT:
                        setcol()

                        original = [col1,col2,col3,col4]

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        left(col1)
                        col1 = newlist
                        # add the first batch of tiles
                        addtiles(col1,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col1[1] = newcolumn[1]
                            col1[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            left(col1)
                            col1 = newlist
                        else:
                            addtiles(col1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col1[2] = newcolumn[1]
                                col1[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col1[2] = newcolumn[1]
                                col1[1] = newcolumn[0]
                            else:
                                addtiles(col1,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col1[3] = newcolumn[1]
                                    col1[2] = newcolumn[0]
                        left(col1)
                        col1 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        left(col2)
                        col2 = newlist
                        # add the first batch of tiles
                        addtiles(col2,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col2[1] = newcolumn[1]
                            col2[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            left(col2)
                            col2 = newlist
                        else:
                            addtiles(col2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col2[2] = newcolumn[1]
                                col2[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col2[2] = newcolumn[1]
                                col2[1] = newcolumn[0]
                            else:
                                addtiles(col2,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col2[3] = newcolumn[1]
                                    col2[2] = newcolumn[0]
                        left(col2)
                        col2 = newlist


                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        left(col3)
                        col3 = newlist
                        # add the first batch of tiles
                        addtiles(col3,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col3[1] = newcolumn[1]
                            col3[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            left(col3)
                            col3 = newlist
                        else:
                            addtiles(col3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col3[2] = newcolumn[1]
                                col3[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col3[2] = newcolumn[1]
                                col3[1] = newcolumn[0]
                            else:
                                addtiles(col3,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col3[3] = newcolumn[1]
                                    col3[2] = newcolumn[0]
                        left(col3)
                        col3 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        left(col4)
                        col4 = newlist
                        # add the first batch of tiles
                        addtiles(col4,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            col4[1] = newcolumn[1]
                            col4[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            left(col4)
                            col4 = newlist
                        else:
                            addtiles(col4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col4[2] = newcolumn[1]
                                col4[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(col4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                col4[2] = newcolumn[1]
                                col4[1] = newcolumn[0]
                            else:
                                addtiles(col4,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    col4[3] = newcolumn[1]
                                    col4[2] = newcolumn[0]
                        left(col4)
                        col4 = newlist

                        screen.fill((235,235,235))
                        printboard()
                        # update the screen
                        pygame.display.update()

                        if original != [col1,col2,col3,col4]:
                            canyouadd = 0
                            for i in range(4):
                                if col1[i] == "    ":
                                    canyouadd = 1
                                if col2[i] == "    ":
                                    canyouadd = 1
                                if col3[i] == "    ":
                                    canyouadd = 1
                                if col4[i] == "    ":
                                    canyouadd = 1

                            if canyouadd == 1:
                                addnew()

                        setrow()

                    # if they pressed the up arrow key
                    elif event.key == K_UP:
                        setrow()

                        original = [col1,col2,col3,col4]

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        up(row1)
                        row1 = newlist
                        # add the first batch of tiles
                        addtiles(row1,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row1[1] = newcolumn[1]
                            row1[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            up(row1)
                            row1 = newlist
                        else:
                            addtiles(row1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row1[2] = newcolumn[1]
                                row1[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row1[2] = newcolumn[1]
                                row1[1] = newcolumn[0]
                            else:
                                addtiles(row1,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row1[3] = newcolumn[1]
                                    row1[2] = newcolumn[0]
                        up(row1)
                        row1 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        up(row2)
                        row2 = newlist
                        # add the first batch of tiles
                        addtiles(row2,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row2[1] = newcolumn[1]
                            row2[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            up(row2)
                            row2 = newlist
                        else:
                            addtiles(row2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row2[2] = newcolumn[1]
                                row2[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row2[2] = newcolumn[1]
                                row2[1] = newcolumn[0]
                            else:
                                addtiles(row2,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row2[3] = newcolumn[1]
                                    row2[2] = newcolumn[0]
                        up(row2)
                        row2 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        up(row3)
                        row3 = newlist
                        # add the first batch of tiles
                        addtiles(row3,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row3[1] = newcolumn[1]
                            row3[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            up(row3)
                            row3 = newlist
                        else:
                            addtiles(row3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row3[2] = newcolumn[1]
                                row3[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row3[2] = newcolumn[1]
                                row3[1] = newcolumn[0]
                            else:
                                addtiles(row3,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row3[3] = newcolumn[1]
                                    row3[2] = newcolumn[0]
                        up(row3)
                        row3 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        up(row4)
                        row4 = newlist
                        # add the first batch of tiles
                        addtiles(row4,0,1)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row4[1] = newcolumn[1]
                            row4[0] = newcolumn[0]
                            # now shift all the tiles to the right again
                            up(row4)
                            row4 = newlist
                        else:
                            addtiles(row4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row4[2] = newcolumn[1]
                                row4[1] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row4[2] = newcolumn[1]
                                row4[1] = newcolumn[0]
                            else:
                                addtiles(row4,2,3)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row4[3] = newcolumn[1]
                                    row4[2] = newcolumn[0]
                        up(row4)
                        row4 = newlist

                        setcol()

                        screen.fill((235,235,235))
                        printboard()
                        # update the screen
                        pygame.display.update()

                        if original != [col1,col2,col3,col4]:
                            canyouadd = 0
                            for i in range(4):
                                if col1[i] == "    ":
                                    canyouadd = 1
                                if col2[i] == "    ":
                                    canyouadd = 1
                                if col3[i] == "    ":
                                    canyouadd = 1
                                if col4[i] == "    ":
                                    canyouadd = 1

                            if canyouadd == 1:
                                addnew()

                        setrow()

                    # if they pressed the down arrow key
                    elif event.key == K_DOWN:
                        setrow()

                        original = [col1,col2,col3,col4]

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        down(row1)
                        row1 = newlist
                        # add the first batch of tiles
                        addtiles(row1,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row1[2] = newcolumn[1]
                            row1[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            down(row1)
                            row1 = newlist
                        else:
                            addtiles(row1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row1[1] = newcolumn[1]
                                row1[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row1,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row1[1] = newcolumn[1]
                                row1[2] = newcolumn[0]
                            else:
                                addtiles(row1,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row1[0] = newcolumn[1]
                                    row1[1] = newcolumn[0]
                        down(row1)
                        row1 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        down(row2)
                        row2 = newlist
                        # add the first batch of tiles
                        addtiles(row2,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row2[2] = newcolumn[1]
                            row2[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            down(row2)
                            row2 = newlist
                        else:
                            addtiles(row2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row2[1] = newcolumn[1]
                                row2[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row2,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row2[1] = newcolumn[1]
                                row2[2] = newcolumn[0]
                            else:
                                addtiles(row2,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row2[0] = newcolumn[1]
                                    row2[1] = newcolumn[0]
                        down(row2)
                        row2 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        down(row3)
                        row3 = newlist
                        # add the first batch of tiles
                        addtiles(row3,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row3[2] = newcolumn[1]
                            row3[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            down(row3)
                            row3 = newlist
                        else:
                            addtiles(row3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row3[1] = newcolumn[1]
                                row3[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row3,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row3[1] = newcolumn[1]
                                row3[2] = newcolumn[0]
                            else:
                                addtiles(row3,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row3[0] = newcolumn[1]
                                    row3[1] = newcolumn[0]
                        down(row3)
                        row3 = newlist

                        # set addmid to 0
                        addmid = 0
                        # shift all the tiles to the right
                        down(row4)
                        row4 = newlist
                        # add the first batch of tiles
                        addtiles(row4,2,3)
                        if newcolumn != [] and newcolumn != ["    "]:
                            row4[2] = newcolumn[1]
                            row4[3] = newcolumn[0]
                            # now shift all the tiles to the right again
                            down(row4)
                            row4 = newlist
                        else:
                            addtiles(row4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row4[1] = newcolumn[1]
                                row4[2] = newcolumn[0]
                                addmid = 1
                        if addmid == 0:
                            addtiles(row4,1,2)
                            if newcolumn != [] and newcolumn != ["    "]:
                                row4[1] = newcolumn[1]
                                row4[2] = newcolumn[0]
                            else:
                                addtiles(row4,0,1)
                                if newcolumn != [] and newcolumn != ["    "]:
                                    row4[0] = newcolumn[1]
                                    row4[1] = newcolumn[0]
                        down(row4)
                        row4 = newlist

                        setcol()

                        screen.fill((235,235,235))
                        printboard()
                        # update the screen
                        pygame.display.update()

                        if original != [col1,col2,col3,col4]:
                            canyouadd = 0
                            for i in range(4):
                                if col1[i] == "    ":
                                    canyouadd = 1
                                if col2[i] == "    ":
                                    canyouadd = 1
                                if col3[i] == "    ":
                                    canyouadd = 1
                                if col4[i] == "    ":
                                    canyouadd = 1

                            if canyouadd == 1:
                                addnew()

                        setrow()

                    if score > highscore:
                        highscore = score

                    screen.fill((235,235,235))
                    printboard()
                    # update the screen
                    pygame.display.update()

    # check to see if you should change the highscore
    fileo = open("2048 highscore.txt")
    old_highscore = int(fileo.readline())
    fileo.close()
    # if the new highscore is bigger, then change it
    if highscore > old_highscore:
        fileo = open("2048 highscore.txt","w")
        fileo.write(str(highscore))
        fileo.close()
