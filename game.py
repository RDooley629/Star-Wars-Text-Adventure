from formattext import *				# Import some important functions for formatting text.


from player import Player
from world import World
import parse

debug_mode = True	# Use this to toggle verbose mode on the text parser.

game_name = "Escape from Cave Terror, v3"

help_text = "To interact with this game world, you will use a basic text-based interface. \
Try single-word commands like 'inventory' or 'west' (or their counterpart abbreviations, 'i' or 'w', respectively \
to get started. For more complex interactions, use commands of the format [VERB][NOUN] (e.g. 'open door', \
or in some cases, [VERB][NOUN][OBJECT] (e.g. 'attack thief with nasty knife').\
The game will ignore the articles 'a', 'an', and 'the' (e.g. 'open the door' is the same as 'open door.').\n\n\
To toggle output from the game parser, type 'debug'. To exit the game at any time, type 'exit' or 'quit'."

victory_text = ["Thank you for playing!", \
				"I hope you enjoyed this game engine demo.", \
				"I look forward to seeing the games you create using this as an example!"]

player = Player()
world = World()
	
def play():	
	print_welcome_text()
	
	print_wrap(world.tile_at(player.x,player.y).intro_text())
	
	while True:
		print()							# Print a blank line for spacing purposes.
		[raw_input, parsed_input] = parse.get_command()
		print()							# Print a blank line for spacing purposes.
		
		
		if(debug_mode):	
			print("--------------------------------------------------------")
			print("RAW USER COMANDS: " + raw_input)
			print("PARSED USER COMMANDS: " + str(parsed_input))
			print("--------------------------------------------------------")
			print()
			

		if(len(parsed_input) == 3):
			[verb, noun1, noun2] = parsed_input
			result_text = handle_input(verb, noun1, noun2)
			if(result_text):
				if(isinstance(result_text, list)):	# Find out if there is more than one sentence returned.
					for text in result_text:
						print_wrap(text)
						if("Victory is yours!" in text):
							print_victory_text()
				else:
					print_wrap(result_text)
					if("Victory is yours!" in result_text):
						print_victory_text()
		else:
			print("Something seems to have gone wrong. Please try again.")
			
		player.update_inventory()
			
		
def handle_input(verb, noun1, noun2):
	global debug_mode
	if(verb == 'help'):
		if(not noun1):
			return help_text
		else:
			return "I'm not sure what you need help with. Try using 'help' on its own."

			
	elif(verb == 'exit'):
		if(not noun1):
			exit()
		else:
			return "Are you trying to quit the game? If so, just type 'exit' on its own."
			
	elif(verb == 'debug'):
		if(not noun1):
			if(debug_mode):
				debug_mode = False
				return "Debug mode turned off."
			else:
				debug_mode = True
				return "Debug mode turned on."
		else:
			return "I don't know what you are trying to debug. If you want to toggle the parser's output text, just type 'debug' on its own."
	
	
	elif(verb == 'go'):
		if(not noun2):
			if(noun1 == 'north'):
				[move_status, move_description] = world.check_north(player.x, player.y)
				if(move_status):
					player.move_north()
					return [move_description, world.tile_at(player.x, player.y).intro_text()]
				else:
					return move_description
					
			elif(noun1 == 'south'):
				[move_status, move_description] = world.check_south(player.x, player.y)
				if(move_status):
					player.move_south()
					return [move_description, world.tile_at(player.x, player.y).intro_text()]
				else:
					return move_description
					
			elif(noun1 == 'east'):
				[move_status, move_description] = world.check_east(player.x, player.y)
				if(move_status):
					player.move_east()
					return [move_description, world.tile_at(player.x, player.y).intro_text()]
				else:
					return move_description
					
			elif(noun1 == 'west'):
				[move_status, move_description] = world.check_west(player.x, player.y)
				if(move_status):
					player.move_west()
					return [move_description, world.tile_at(player.x, player.y).intro_text()]
				else:
					return move_description	
					
			else:
				return "I'm not sure where you're trying to go."
				
		else:
			return "Whatever you are trying to do is too complicated for me to understand. Please try again."
			
			
	elif(verb == 'check'):
		if(not noun2):
			if(noun1 == None or noun1 == 'around' or noun1 == 'room' or noun1 == 'surroundings'):
				return world.tile_at(player.x, player.y).intro_text()
			elif(noun1 == 'inventory' or noun1 == 'pockets'):
				player.print_inventory();
				return ''	# No need to return any text because the player.print_inventory() function already did.
			else:
				[status, description] = player.handle_input(verb, noun1, noun2)
				if(status):
					return description
				else:
					[status, description, inventory] = world.tile_at(player.x, player.y).handle_input(verb, noun1, noun2, player.inventory)
					if(status):
						return description
					else:
						return "I'm not sure what you are trying to look at."
		else:
			return "I think you are trying to look at something, but your phrasing is too complicated. Please try again."


			
	elif(verb):
		[status, description] = player.handle_input(verb, noun1, noun2)
		if(status):
			return description
		else:
			[status, description, inventory] = world.tile_at(player.x, player.y).handle_input(verb, noun1, noun2, player.inventory)
			if(status):
				player.inventory = inventory
				return description
			else:
				return "I'm not sure what you are trying to %s." % verb
	else:
		return "I have no idea what you are trying to do. Please try again."
 
def print_welcome_text():
	clear_screen()
	print_center("========================================================")
	print()
	print_center("WELCOME TO %s!" % game_name.upper())
	print()
	print_center("========================================================")
	print()
	
def print_victory_text():
	print()
	print_center("========================================================")
	print()
	for line in victory_text:
		print_center(line)
	print()
	print_center("========================================================")
	exit()

### Play the game.
play()