from player import Player
import world 

def play():
	print("Escape from the cave!"
	player = Player()
	while True:
		action_input = get_player_command()
		if action_input in ["n", "N"]:
			player.move_north()
		elif action_input in ['s', "S"]:
			player.move_south()
		elif action_input in ['e', "E"]:
			player.move_east()
		elif action_input in ['w', "W"]:
			player.move_inventory
		elif action_input in ['i', "I"]:
			player.print_inventory()
		else:
			print("Excuse me, but I couldn't quite catch that.")

def get_player_command():
	return input("Action: ")

play()
