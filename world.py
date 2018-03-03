import items
import enemies
import barriers
import npcs

from random import randint 	# Used to generate random integers.

class MapTile:
	description = "Do not create raw MapTiles! Create a subclass instead!"
	barriers = []
	enemies = []
	items = []
	npcs = []
	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = [], npcs = []):
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
		for npc in npcs:
			self.add_npc(npc)
	
	def intro_text(self):
		text = self.description
		directions_blocked = []
		
		for enemy in self.enemies:
			if (enemy.direction):
				if(enemy.direction not in directions_blocked):
					directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if (barrier.direction):
				if(barrier.direction not in directions_blocked):
					if(barrier.verbose):
						text += " " + barrier.description()
		for npc in self.npcs:
			text += " " + npc.check_text()
		for item in self.items:
			text += " " + item.room_text()

		return text
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(not noun2):
			if(verb == 'check'):
				for barrier in self.barriers:
					if(barrier.name):
						if(barrier.name.lower() == noun1):
							return [True, barrier.description(), inventory]
				for item in self.items:
					if(item.name.lower() == noun1):
						return [True, item.check_text(), inventory]
				for enemy in self.enemies:
					if(enemy.name.lower() == noun1):
						return [True, enemy.check_text(), inventory]
				for npc in self.npcs:
					if(npc.name.lower() == noun1):
						return [True, npc.check_text(), inventory]
			elif(verb == 'take'):
				for index in range(len(self.items)):
					if(self.items[index].name.lower() == noun1):
						if(isinstance(self.items[index], items.Item)):
							pickup_text = "You picked up the %s." % self.items[index].name
							inventory.append(self.items[index])
							self.items.pop(index)
							return [True, pickup_text, inventory]
						else:
							return [True, "The %s is too heavy to pick up." % self.items[index].name, inventory]
			elif(verb == 'drop'):
				for index in range(len(inventory)):
					if(inventory[index].name.lower() == noun1):
						inventory[index].is_dropped = True
						drop_text = "You dropped the %s." % inventory[index].name
						self.add_item(inventory[index])
						inventory.pop(index)
						return [True, drop_text, inventory]

		for list in [self.barriers, self.items, self.enemies, self.npcs]:
			for item in list:
				[status, description, inventory] = item.handle_input(verb, noun1, noun2, inventory)
				if(status):
					return [status, description, inventory]
					
		for list in [self.barriers, self.items, self.enemies, self.npcs]:			# Added to give the player feedback if they have part of the name of an object correct.
			for item in list:
				if(item.name):
					if(noun1 in item.name):
						return [True, "Be more specific.", inventory]
			
		return [False, "", inventory]
		
	def add_barrier(self, barrier):
		if(len(self.barriers) == 0):
			self.barriers = [barrier]		# Initialize the list if it is empty.
		else:
			self.barriers.append(barrier)	# Add to the list if it is not empty.
			
	def add_item(self, item):
		if(len(self.items) == 0):
			self.items = [item]		# Initialize the list if it is empty.
		else:
			self.items.append(item)	# Add to the list if it is not empty.
			
	def add_enemy(self, enemy):
		if(len(self.enemies) == 0):
			self.enemies = [enemy]		# Initialize the list if it is empty.
		else:
			self.enemies.append(enemy)	# Add to the list if it is not empty.
			
	def add_npc(self, npc):
		if(len(self.npcs) == 0):
			self.npcs = [npc]		# Initialize the list if it is empty.
		else:
			self.npcs.append(npc)	# Add to the list if it is not empty.
			
	def random_spawn(self):
		pass						# Update this for your specific subclass if you want randomly spawning enemies.
			
	def update(self, player):
		dead_enemy_indices = []
		for index in range(len(self.enemies)):
			if (not self.enemies[index].is_alive()):
				dead_enemy_indices.append(index)
				for item in self.enemies[index].loot:
					self.add_item(item)
		for index in reversed(dead_enemy_indices):
			self.enemies.pop(index)
		if(self.x == player.x and self.y == player.y):
			for enemy in self.enemies:
				if(enemy.agro):
					agro_text = "The %s seems very aggitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)


class StartTile(MapTile):
	items = [items.Rock()]
	description = """You find yourself in a cave with a flickering torch on the wall.
		You can make out a path to the east and to the west, each equally as dark and foreboding.
		"""

class Corridor(MapTile):
	description = """You find yourself in a poorly lit corridor."""
	flavor_text = ["This portion of the cave seems particularly musty.", \
				"You head nearly brushes the low ceiling.", \
				"The sound of bats in the distance gives you a chill."]
	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = [], npcs = []):	# Since this tile appears so much, I gave it its own __init__() function to add random flavor text to some of the tiles.
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
		for npc in npcs:
			self.add_npc(npc)
			
		num = randint(0,len(self.flavor_text)*3-1)	# Generate a random number. Based on our range, 1 in 3 corridors will have added flavor text.
		if(num < len(self.flavor_text)):
			self.description += " " + self.flavor_text[num]
	
	def intro_text(self):	# Since this tile appears so much, I gave it its own intro_text function to make its text more descriptive.
		text = self.description
			
		directions_clear = ['north', 'south', 'east', 'west']
		for barrier in self.barriers:
			try:
				directions_clear.pop(directions_clear.index(barrier.direction))		# Attempt to remove the barrier's direction from the list of clear directions.
			except:
				pass		# If the barrier direction is not in the list of clear directions already, then we ignore it.
		#for enemy in self.contents['enemies']:
		#	text += " " + enemy.description()
		
		if(len(directions_clear) == 1):
			text += " There is a clear pathway leading to the %s." % directions_clear[0]
		elif(len(directions_clear) == 2):
			text += " There are clear pathways leading to the %s and %s." % (directions_clear[0], directions_clear[1])
		elif(len(directions_clear) == 3):
			text += " There are clear pathways leading to the %s, %s, and %s." % (directions_clear[0], directions_clear[1], directions_clear[2])
		elif(len(directions_clear) == 4):
			text += " It appears that your path is clear in all directions." 
		
		directions_blocked = []
		
		for enemy in self.enemies:
			if (enemy.direction):
				if(enemy.direction not in directions_blocked):
					directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if (barrier.direction):
				if(barrier.direction not in directions_blocked):
					if(barrier.verbose):
						text += " " + barrier.description()
		for npc in self.npcs:
			text += " " + npc.check_text()
		for item in self.items:
			text += " " + item.room_text()
		return text
	
		
class StoreRoom(MapTile):
	items = [items.Rusty_Sword("A rusty sword is propped against a shelf in the corner of the room."), \
			items.Red_Potion("A glowing bottle of mysterious red potion sits on one of the shelves."), \
			items.Old_Chest([items.Mountain_of_Gold()]), \
			items.Gold_Coins("A shiny handful of gold coins is on the ground near the chest.")]
	
	description = """You seem to have entered an underground storeroom!"""
		
class ExpanseSW(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the northeast."""
	
	def random_spawn(self):
		if(randint(0,3) == 0):		# 1 in 4 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
			
	
class ExpanseSE(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the northwest. There is a small corridor leading to the east from here."""
	
	def random_spawn(self):
		if(randint(0,2) == 0):		# 1 in 3 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
			
class ExpanseNW(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the southeast. There is a small corridor leading to the north from here."""

	def random_spawn(self):
		if(randint(0,3) == 0):		# 1 in 4 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
				
class ExpanseNE(MapTile):
	description = """You find yourself in an expansive cavern, with walls stretching out nearly as far as the eye can see. The room opens before you to the southwest. A small nook lies to your east."""

	def random_spawn(self):
		if(randint(0,1) == 0):		# 1 in 2 odds.
			self.enemies = [enemies.BatColony()]
		else:
			self.enemies = []
			
class Nook(MapTile):
	enemies = [enemies.RockMonster()]
	description = """You have entered a shadowy nook of the cave. The only way out is back the way you came."""
	
class Cave(MapTile):
	npcs = [npcs.OldMan()]
	description = """You have entered a very dark portion of the cave. Two small fires, one on each side of the room, are glowing softly."""
		
		
class NearVictory(MapTile):
	description = """You can see a light to the east at the end of this corridor. Could that be your way out?"""


class VictoryTile(MapTile):
	description = """You see a bright light in the distance...
		It grows as you get closer! It's sunlight!	
		Victory is yours!
		"""
		
class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[Corridor(barriers = [barriers.LockedDoor('e')]),			NearVictory(barriers = [barriers.Wall('s')]),																VictoryTile(),																																										Corridor(barriers = [barriers.Wall('w')]), 																			Corridor()],
		[ExpanseNW(),												ExpanseNE(barriers = [barriers.Wall('n')]),	 																Nook(barriers = [barriers.Wall('n'), barriers.Wall('s'), barriers.Wall('e')]), 																										Corridor(barriers = [barriers.Wall('e'), barriers.Wall('w')], enemies = [enemies.Ogre('s')]),						Corridor(barriers = [barriers.Wall('w')])],
		[ExpanseSW(),												ExpanseSE(barriers = [barriers.Wall('s')]), 																Corridor(barriers = [barriers.Wall('n'), barriers.Wall('s')]), 																														Corridor(barriers = [barriers.Wall('e'), barriers.Wall('s')]),		 												Corridor(barriers = [barriers.Wall('w')])],
		[Corridor(barriers = [barriers.Wall('n')]),					Corridor(barriers = [barriers.Wall('n')]),																	StartTile(barriers = [barriers.Wall('s'), barriers.Wall('n')]), 																													Corridor(barriers = [barriers.Wall('n')]), 																			Corridor()],
		[Cave(barriers = [barriers.Wall('e')]),						Corridor(barriers = [barriers.WoodenDoor('e'), barriers.Wall('w')], enemies = [enemies.GiantSpider('e')]),	StoreRoom(barriers = [barriers.Wall('n')]),																																			None,																												None]
	]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
					self.add_implied_barriers(j,i)	# If there are implied barriers (e.g. edge of map, adjacent None room, etc.) add a Wall.
						
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'north'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'north' and not barrier.passable):
				return [False, barrier.description()]				
				
		if y-1 < 0:
			room = None
		else:
			try:
				room = self.map[y-1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be a path to the north."]
			
	def check_south(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'south'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'south' and not barrier.passable):
				return [False, barrier.description()]	
				
		if y+1 < 0:
			room = None
		else:
			try:
				room = self.map[y+1][x]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be a path to the south."]

	def check_west(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'west'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'west' and not barrier.passable):
				return [False, barrier.description()]	
	
		if x-1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x-1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be a path to the west."]
			
	def check_east(self, x, y):
		for enemy in self.map[y][x].enemies:
			if(enemy.direction == 'east'):
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if(barrier.direction == 'east' and not barrier.passable):
				return [False, barrier.description()]	
				
		if x+1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x+1]
			except IndexError:
				room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be a path to the east."]
			
	def add_implied_barriers(self, x, y):

		[status, text] = self.check_north(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'north':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'north':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('n'))	
				
		[status, text] = self.check_south(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'south':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'south':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('s'))	
			
		[status, text] = self.check_east(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'east':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'east':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('e'))	
			
		[status, text] = self.check_west(x,y)
		barrier_present = False
		if(not status):
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'west':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'west':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('w'))	
		
	def update_rooms(self, player):
		for row in self.map:
			for room in row:
				if(room):
					room.update(player)
	