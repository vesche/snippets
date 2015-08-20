# Concept game for python beginners

import os
import time

about_text = '''
This is a text adventure game that is played
inside the command prompt of Windows! You
have to stay alive, fight off some zombies,
and try to escape. Good luck...
'''

def main():
	started = True

	while started:
		# clear the screen
		os.system('cls')

		# print menu options and prompt
		print "CMD.EXE ADVENTURE!\n\t1. Play\n\t2. About\n\t3. Quit"
		menu_choice = raw_input('>')

		# act on menu choice
		if menu_choice == '1': game()
		if menu_choice == '2': raw_input(about_text)
		if menu_choice == '3': quit()

def game():
	# define intial variables
	playing		= True
	game_map	= ['_', '_', '_', '_', '_', '_', '_', '_', '_']
	character	= '@'
	pos			= 4

	# get user defined variables
	name = raw_input("\nWhat's your name? ")
	print "Get ready", name + '!'

	while playing:
		# clear the screen
		os.system('cls')

		# update character position
		game_map[pos] = character

		# print map and prompt
		print 'CMD.EXE ADVENTURE!\n' + name, '- Level 0\n'
		print '    ' + ' '.join(game_map[0:3])
		print '    ' + ' '.join(game_map[3:6])
		print '    ' + ' '.join(game_map[6:9])
		move = raw_input('\n> ')

		# reset position
		game_map[pos] = '_'

		# act on move
		if move.upper() == "NORTH":
			if pos <= 2:
				continue
			pos -= 3

		if move.upper() == "SOUTH":
			if pos >= 6:
				continue
			pos += 3

		if move.upper() == "EAST":
			if pos == 2 or pos == 5 or pos == 8:
				continue
			pos += 1

		if move.upper() == "WEST":
			if pos == 0 or pos == 3 or pos == 6:
				continue
			pos -= 1

		if move.upper() == "QUIT":
			playing = False

if __name__ == '__main__':
	main()