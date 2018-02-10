from random import randint 	# Used to generate random integers.

from textwrap import fill	# Gives us a tool for formatting text in a much prettier fashion.

from terminalsize import get_terminal_size		# Allows us to determine terminal window size on any OS.
												# Adapted for Python 3.x from https://gist.github.com/jtriley/1108174

from player import Player
from world import World
import parse

debug_mode = True	# Use this to toggle verbose mode on the text parser.

game_name = "Escape from Cave Terror, v2"

help_text = "To interact with this game world, you will use a basic text-based interface. \
Try single-word commands like 'inventory' or 'west' (or their counterpart abbreviations, 'i' or 'w', respectively \
to get started. For more complex interactions, use commands of the format [VERB][NOUN] (e.g. 'open door', \
or in some cases, [VERB][NOUN][OBJECT] (e.g. 'attack thief with nasty knife').\
The game will ignore the articles 'a', 'an', and 'the' (e.g. 'open the door' is the same as 'open door.').\n\n\
To exit the game at any time, type 'exit' or 'quit'."

wrap_width = 0								# We will eventually use this so that we can wrap text.
	
def play():	
	clear_screen()
	print_wrap("Welcome to %s!" % game_name)
	player = Player()
	world = World()
	
	print_wrap(world.tile_at(player.x,player.y).intro_text())
	
	while True:
		print("")							# Print a blank line for spacing purposes.
		[raw_input, parsed_input] = parse.get_command()
		print("")							# Print a blank line for spacing purposes.
		
		if(parsed_input):
			if(len(parsed_input)==1):
				if(parsed_input[0] == "help"):
					print_wrap(help_text)
				elif(parsed_input[0] == "check"):
					print_wrap(world.tile_at(player.x,player.y).intro_text())
				elif(parsed_input[0] == "exit" or parsed_input[0] == quit):
					exit()
				else:
					print("I don't understand what you are trying to do. Please try again.")
			elif(len(parsed_input) == 2):
				if(parsed_input[0] == "go"):													### Command "go"
					move_status = False
					if(parsed_input[1] == "north"):
						[move_status, move_description] = world.check_north(player.x, player.y)
						print_wrap(move_description)
						if(move_status):
							player.move_north()
					elif(parsed_input[1] == "south"):
						[move_status, move_description] = world.check_south(player.x, player.y)
						print_wrap(move_description)
						if(move_status):
							player.move_south()
					elif(parsed_input[1] == "east"):
						[move_status, move_description] = world.check_east(player.x, player.y)
						print_wrap(move_description)
						if(move_status):
							player.move_east()
					elif(parsed_input[1] == "west"):
						[move_status, move_description] = world.check_west(player.x, player.y)
						print_wrap(move_description)
						if(move_status):
							player.move_west()		
					else:
						print("I don't understand where you're trying to go.")
					
					
					if(move_status):		# If we have successfully moved, give the player the new location's description.
						print_wrap(world.tile_at(player.x,player.y).intro_text())
						
						
						
				elif(parsed_input[0] == "check"):													### Command "check"
					if(parsed_input[1] == "inventory"):
						player.print_inventory()
					elif(parsed_input[1] == "around"):
						print_wrap(world.tile_at(player.x,player.y).intro_text())
					else:
						print("I don't know what you're trying to look at.")
						
				else:
					print("I don't understand what you are trying to do. Please try again.")
			else:
				print("I don't understand what you are trying to do. Please try again.")
				
				
			if(debug_mode):		
				for word in parsed_input:
					if(word):
						print(word + " ")
					else:
						print("None")
		else:
			print("Something seems to have gone wrong. Please try again.")
			
			
			
			
		
# These functions exist only to help make the text print nicer in the terminal.		
def get_width():
	dimensions = get_terminal_size()
	global wrap_width 
	if(dimensions[0] >= 20):
		wrap_width = dimensions[0] - 5				# Get the width of the user's window so we can wrap text.
	else:
		wrap_width = dimensions[0]						
	return dimensions
    
	
def clear_screen():
	terminal = get_width()
   
	for i in range(terminal[1]):
		print("")									# There are fancier ways to clear a screen, but this aligns our text where we want it at the bottom of the window.

		
def print_wrap(text):
	get_width()
	text = text.replace("\t", "")
	print(fill(text, wrap_width))
 

### Play the game.
play()