# -*- coding: utf-8 -*-
#Maze Generator By Zack Nathan
#Generates a text based maze
#Very long file took a long time to make, please don't steal me

from random import random, choice, randint, randrange
from time import sleep
import os
import sys

restart = False

def generate():
	global a, ypos, xpos, restart, steps, x, y

	array = []

	#Create array
	for i in range(a+1):
		array.append([1]*(a+1))

	#Create walls
	for row in range(a+1):

		if 0 < row < a+1:
			if row%2 == 1:
				for cell in range(a+1):
					if cell%2 == 0:
						if 0 < cell < a+1:
							array[row][cell] = 2
			else:
				for cell in range(a+1):
					if cell%2 == 1:
						if 0 < cell < a+1:
							array[row][cell] = 2

	#Outside Wall
	for row in array:
		row[0] = 3
		row[a] = 3
	for i in range(a+1):
		array[0][i] = 3
		array[a][i] = 3

	#Verticies
	for row in range(a+1):
		if 0 < row < a+1:
			if row%2 == 0:
				for cell in range(a+1):
					if cell%2 == 0:
						array[row][cell] = 3

	#Start and Finish
	array[0][1] = ' '
	array[a][a-1] = ' '

	#0: part of the maze, not retraced
	#1: not part of the maze, will become part of the maze
	#2: wall that may become part of the maze
	#3: wall that will be a wall
	#4: randomly generated middle wall, one of which will become part of the maze
	#' ': part of the maze, retraced

	#Choose direction to move and which wall to break, or retrace if it can't move
	def choosedirection(x, y, startingpoint):
		global ypos, xpos, a
		directions = []

		#Check if finished
		if startingpoint == ' ':
			return

		#Scan for possible directions
		if y > 2:
			if array[y-1][x] == 2 and array[y-2][x] == 1:
				directions.append('up')
		if y < 2*a-2:
			if array[y+1][x] == 2 and array[y+2][x] == 1:
				directions.append('down')
		if x > 2:
			if array[y][x-1] == 2 and array[y][x-2] == 1:
				directions.append('left')
		if x < 2*a-2:
			if array[y][x+1] == 2 and array[y][x+2] == 1:
				directions.append('right')

		#Return direction
		if len(directions) > 0:
			return choice(directions)

		#Retrace Mode
		else:

			directions = []

			#Scan for retraceable direction
			if y > 2:
				if array[y-1][x] == 0 and array[y-2][x] == 0:
					directions.append('up')
			if y < 2*a-2:
				if array[y+1][x] == 0 and array[y+2][x] == 0:
					directions.append('down')
			if x > 2:
				if array[y][x-1] == 0 and array[y][x-2] == 0:
					directions.append('left')
			if x < 2*a-2:
				if array[y][x+1] == 0 and array[y][x+2] == 0:
					directions.append('right')

			#Retrace and check for directions again
			if len(directions) == 1:
				direction = directions[0]
				if direction == 'up':
					array[y][x] = ' '
					array[y-1][x] = ' '
					ypos -= 2
				elif direction == 'down':
					array[y][x] = ' '
					array[y+1][x] = ' '
					ypos += 2
				elif direction == 'left':
					array[y][x] = ' '
					array[y][x-1] = ' '
					xpos -= 2
				elif direction == 'right':
					array[y][x] = ' '
					array[y][x+1] = ' '
					xpos += 2
				choosedirection(xpos, ypos, startingpoint)

			#Finished
			else:
				array[y][x] = ' '
				startingpoint = ' '
				return

	#Move in the direction chosen by the function and break down a wall
	def move(direction, x, y):
		global ypos, xpos
		if direction == 'up':
			array[y][x] = 0
			array[y-1][x] = 0
			ypos -= 2
		elif direction == 'down':
			array[y][x] = 0
			array[y+1][x] = 0
			ypos += 2
		elif direction == 'left':
			array[y][x] = 0
			array[y][x-1] = 0
			xpos -= 2
		elif direction == 'right':
			array[y][x] = 0
			array[y][x+1] = 0
			xpos += 2

	#Create middle wall
	if a >= 10:
		pick = randrange(4, a-4, 2)
		for i in range(1, a, 2):
			array[i][pick] = 4
			pick = randrange(pick-4, pick+4, 2)
			if pick > a:
				pick -= 4
			if pick < 0:
				pick += 4
		for i in range(2, a-1, 2):
			start = array[i-1].index(4)
			end = array[i+1].index(4)
			if end > start:
				for j in range(start, end):
					if array[i][j] == 2:
						array[i][j] = 4
			else:
				for j in range(end, start):
					if array[i][j] == 2:
						array[i][j] = 4

	#Start from bottom right corner
	array[-2][1] = 0
	xpos = 1
	ypos = a-1
	while array[-2][1] != ' ':
		direction = choosedirection(xpos, ypos, array[-2][1])
		if array[-2][1] == ' ':
			break
		move(direction, xpos, ypos)


	#Start from top left corner
	if a >= 10:
		array[1][-2] = 0
		xpos = a-1
		ypos = 1
		while array[1][-2] != ' ':
			direction = choosedirection(xpos, ypos, array[1][-2])
			if array[1][-2] == ' ':
				break
			move(direction, xpos, ypos)

	#Make hole in wall
	while True:
		hole = [randint(1, a-1), randint(4, a-4)]
		if array[hole[0]][hole[1]] == 4:
			array[hole[0]][hole[1]] = ' '
			break

	#Convert to hashtags
	for row in array:
		for i in range(a+1):
			if row[i] != ' ':
				row[i] = '#'

	#Convert to ascii
	for row in range(a+1):
		if 0 < row < a+1:
			if row%2 == 1:
				for cell in range(a+1):
					if cell%2 == 0:
						if 0 < cell < a+1:
							if array[row][cell] == '#':
								array[row][cell] = '┃'
			else:
				for cell in range(a+1):
					if cell%2 == 1:
						if 0 < cell < a+1:
							if array[row][cell] == '#':
								array[row][cell] = '━'

	#Edges
	for row in array:
		row[0] = '┃'
		row[a] = '┃'
	for i in range(a+1):
		array[0][i] = '━'
		array[a][i] = '━'

	#Verticies
	for row in range(a+1):
		if 0 < row < a+1:
			if row%2 == 0:
				for cell in range(a+1):
					if array[row][cell] == '#':

						if array[row-1][cell] == ' ':

							if array[row][cell+1] == ' ':

								if array[row+1][cell] == ' ':

									if array[row][cell-1] == ' ':
										array[row][cell] = '▪'
									else:
										array[row][cell] = '╸'

								else:
									if array[row][cell-1] == ' ':
										array[row][cell] = '╻'
									else:
										array[row][cell] = '┓'

							else:
								if array[row+1][cell] == ' ':

									if array[row][cell-1] == ' ':
										array[row][cell] = '╺'
									else:
										array[row][cell] = '━'

								else:
									if array[row][cell-1] == ' ':
										array[row][cell] = '┏'
									else:
										array[row][cell] = '┳'

						else:
							if array[row][cell+1] == ' ':

								if array[row+1][cell] == ' ':

									if array[row][cell-1] == ' ':
										array[row][cell] = '╹'
									else:
										array[row][cell] = '┛'

								else:
									if array[row][cell-1] == ' ':
										array[row][cell] = '┃'
									else:
										array[row][cell] = '┫'

							else:
								if array[row+1][cell] == ' ':

									if array[row][cell-1] == ' ':
										array[row][cell] = '┗'
									else:
										array[row][cell] = '┻'

								else:
									if array[row][cell-1] == ' ':
										array[row][cell] = '┣'
									else:
										array[row][cell] = '╋'

	#Edges
	for i in range(2, a+1, 2):
		if array[i][1] != ' ':
			array[i][0] = '┣'
		if array[i][-2] != ' ':
			array[i][-1] = '┫'
		if array[1][i] != ' ':
			array[0][i] = '┳'
		if array[-2][i] != ' ':
			array[-1][i] = '┻'

	#Corners, start, and end
	array[0][0] = '┏'
	array[0][1] = ' '
	array[a][a-1] = ' '
	array[a][a] = '┛'
	array[0][a] = '┓'
	array[a][0] = '┗'

	#Check if finished
	for row in array:
		for cell in row:
			if cell == '#':
				restart = True
				return

	#0: Part of solution path
	#1: Retraced
	#' ': Not part of path
	#Solve
	def solve():
		global a, steps, x, y
		directions = []

		array[y][x] = 0

		#Scan for possible directions
		if array[y-1][x] == ' ':
			directions.append('up')
		if array[y+1][x] == ' ':
			directions.append('down')
		if array[y][x-1] == ' ':
			directions.append('left')
		if array[y][x+1] == ' ':
			directions.append('right')

		#Move
		if len(directions) > 0:
			direction = choice(directions)
			if direction == 'up':
				y -= 1
			elif direction == 'down':
				y += 1
			elif direction == 'left':
				x -= 1
			elif direction == 'right':
				x += 1
			steps += 1
			return

		#Retrace Mode
		else:
			direction = 0
			#Scan for retraceable direction
			if array[y-1][x] == 0:
				direction = 'up'
			if array[y+1][x] == 0:
				direction = 'down'
			if array[y][x-1] == 0:
				direction = 'left'
			if array[y][x+1] == 0:
				direction = 'right'

			#Retrace and check for directions again
			if direction != 0:
				if direction == 'up':
					array[y][x] = 1
					y -= 1
				elif direction == 'down':
					array[y][x] = 1
					y += 1
				elif direction == 'left':
					array[y][x] = 1
					x -= 1
				elif direction == 'right':
					array[y][x] = 1
					x += 1
				steps -= 1
				return

			#Finished
			else:
				if x == a-1 and y == a-1:
					return
				else:
					print 'error'

	steps = 0
	x = 1
	y = 1
	solve()

	#Check if finished
	while True:
		if x == a-1 and y == a-1:
			break
		else:
			solve()

	#Convert back to spaces
	for i in range(a):
		for j in range(a):
			if array[i][j] in [0, 1]:
				array[i][j] = ' '

	print steps

	#Check if complex enough
	if a > 40:
		if a > 80:
			if steps < ((a/2)*(a/2))-(((a/2)/8)*(a/2))-(15*((a/2)-40))-(15*((a/2)-20))-a:
				restart = True
				return
		else:
			if steps < ((a/2)*(a/2))-(((a/2)/8)*(a/2))-(15*((a/2)-20))-a:
				restart = True
				return
	else:
		if steps < ((a/2)*(a/2))-a:
			restart = True
			return

	#Print maze
	for row in array:
		for i in range(a+1):
			print '\b'+str(row[i]),
			if i != a:
				if row[i+1] != ' ' and row[i] != ' ':
					print '\b━',
				else:
					print '\b ',
		print ''

while True:
	if restart == False:
		while True:
			a = input('Size: ')
			if a < 5:
				print 'Too small, please choose a number bigger than 5'
			else:
				break
		a *= 2
	if restart == True:
		restart = False
	generate()
