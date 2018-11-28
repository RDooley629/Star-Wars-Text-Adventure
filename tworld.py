import items
import enemies
import barriers
import npcs

from random import randint 	# Used to generate random integers.


class Maptile:
	description = "Do not create raw Maptiles! Create a subclass instead!"
	barriers = []
	enemies = []
	items = []
	npcs = []
	teleport = None
	
	def __init__(self, x=0, y=0, barriers=[], items=[], enemies=[], npcs=[]):
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
			if enemy.direction:
				if enemy.direction not in directions_blocked:
					directions_blocked.append(enemy.direction)
			text += " " + enemy.check_text()
		for barrier in self.barriers:
			if barrier.direction:
				if barrier.direction not in directions_blocked:
					if barrier.verbose:
						text += " " + barrier.description()
		for npc in self.npcs:
			text += " " + npc.check_text()
		for item in self.items:
			text += " " + item.room_text()

		return text
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if not noun2:
			if verb == 'check':
				for barrier in self.barriers:
					if barrier.name:
						if barrier.name.lower() == noun1:
							return [True, barrier.description(), inventory]
				for item in self.items:
					if item.name.lower() == noun1:
						return [True, item.check_text(), inventory]
				for enemy in self.enemies:
					if enemy.name.lower() == noun1:
						return [True, enemy.check_text(), inventory]
				for npc in self.npcs:
					if npc.name.lower() == noun1:
						return [True, npc.check_text(), inventory]
			elif verb == 'take':
				for index in range(len(self.items)):
					if self.items[index].name.lower() == noun1:
						if isinstance(self.items[index], items.Item):
							pickup_text = "You picked up the %s." % self.items[index].name
							inventory.append(self.items[index])
							self.items.pop(index)
							return [True, pickup_text, inventory]
						else:
							return [True, "The %s is too heavy to pick up." % self.items[index].name, inventory]
			elif verb == 'drop':
				for index in range(len(inventory)):
					if inventory[index].name.lower() == noun1:
						inventory[index].is_dropped = True
						drop_text = "You dropped the %s." % inventory[index].name
						self.add_item(inventory[index])
						inventory.pop(index)
						return [True, drop_text, inventory]

		for listing in [self.barriers, self.items, self.enemies, self.npcs]:
			for item in listing:
				[status, description, inventory] = item.handle_input(verb, noun1, noun2, inventory)
				if status:
					return [status, description, inventory]
					
		for listing in [self.barriers, self.items, self.enemies, self.npcs]:
			# Added to give the player feedback if they have part of the name of an object correct.
			for item in listing:
				if item.name:
					if noun1 in item.name:
						return [True, "Be more specific.", inventory]
			
		return [False, "", inventory]
		
	def add_barrier(self, barrier):
		if len(self.barriers) == 0:
			self.barriers = [barrier]			# Initialize the list if it is empty.
		else:
			self.barriers.append(barrier)		# Add to the list if it is not empty.
			
	def add_item(self, item):
		if len(self.items) == 0:
			self.items = [item]			# Initialize the list if it is empty.
		else:
			self.items.append(item)		# Add to the list if it is not empty.
			
	def add_enemy(self, enemy):
		if len(self.enemies) == 0:
			self.enemies = [enemy]			# Initialize the list if it is empty.
		else:
			self.enemies.append(enemy)		# Add to the list if it is not empty.
			
	def add_npc(self, npc):
		if len(self.npcs) == 0:
			self.npcs = [npc]			# Initialize the list if it is empty.
		else:
			self.npcs.append(npc)		# Add to the list if it is not empty.
			
	def random_spawn(self):
		pass						# Update this for your specific subclass if you want randomly spawning enemies.
			
	def update(self, player):
		dead_enemy_indices = []
		for index in range(len(self.enemies)):
			if not self.enemies[index].is_alive():
				dead_enemy_indices.append(index)
				for item in self.enemies[index].loot:
					self.add_item(item)
		for index in reversed(dead_enemy_indices):
			self.enemies.pop(index)
		if (self.x == player.x) and (self.y == player.y):
			if self.teleport:
				player.x = self.teleport[0]
				player.y = self.teleport[1]
			for enemy in self.enemies:
				if enemy.agro:
					agro_text = "The %s seems very aggitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)	
		return player


#

class FoodComa(Maptile):
	description = """ You gorge yourself on food, revelling in the taste of airport food. \
	Soon, you find your eyelids growing heavy. Despite yourself, you soon fall asleep. \
	You die in your sleep. Whether by zombie or by heart attack, the world may never know. \
	Victory is yours, I suppose.
	
		"""


class FoodCourt(Maptile):
	description = """

		"""


class MainAirport(Maptile):
	description = """

		"""


class Monorail(Maptile):
	description = """

		"""


class MarioCart(Maptile):
	description = """

		"""


class Gate(Maptile):
	description = """

		"""


class Escalator(Maptile):
	description = """

		"""


class Contraband(Maptile):
	description = """

		"""


class LuggageVoid(Maptile):
	description = """

		"""


class Plane(Maptile):
	description = """

		"""


class Checkpoint(Maptile):
	description = """

		"""


class Bathroom(Maptile):
	description = """

		"""


class Cars(Maptile):
	description = """

		"""


class TicketCounter(Maptile):
	description = """

		"""


class Lobby(Maptile):
	description = """

		"""


class LobbyEast(Maptile):
	description = """

		"""

#


class World:
	map = [
		[FoodComa(), 									FoodCourt(barriers=[barriers.Wall('s')], items=[items.Smoothie()]),	MainAirport(enemies=[enemies.ZombieHorde('e')]), 				Monorail()	],
		[MarioCart(barriers=[barriers.Wall('n')]), 	Gate(barriers=[barriers.Wall('n')], enemies=[enemies.Zombie('w')]),	Escalator(barriers=[barriers.lockeddoor('e')]), 				Contraband(barriers=[barriers.Wall('n'), barriers.Wall('s'), barriers.Door('w')], items=[items.Storage_Locker])	],
		[LuggageVoid(), 								Plane(), 																Checkpoint(barriers=[barriers.Wall('e'), barriers.Wall('w')]),	Bathroom(barriers=[barriers.Wall('n'), barriers.Wall('w')], enemies=[enemies.Zombie('s')])],
		[Cars(), 										TicketCounter(barriers=[barriers.Wall('n'), barriers.Sliding('w')]), 	Lobby(enemies=[enemies.Zombie('w')]), 							LobbyEast()	]


	]

	def __init__(self):
		for i in range(len(self.map)):				# We want to set the coordinates for each tile so that it "knows" its location.
			for j in range(len(self.map[i])):		# handle automatically so there is no chance that the map index does not match
				if self.map[i][j]:					# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
					self.add_implied_barriers(j, i)		# If there are implied barriers (e.g. edge of map, adjacent None room), add a Wall
						
#
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		for enemy in self.map[y][x].enemies:
			if enemy.direction == 'north':
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if barrier.direction == 'north' and not barrier.passable:
				return [False, barrier.description()]				
				
		if y-1 < 0:
			room = None
		else:
			try:
				room = self.map[y-1][x]
			except IndexError:
				room = None
		
		if room:
			return [True, "You move to the north."]
		else:
			return [False, "There doesn't seem to be a path to the north."]
			
	def check_south(self, x, y):
		for enemy in self.map[y][x].enemies:
			if enemy.direction == 'south':
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if barrier.direction == 'south' and not barrier.passable:
				return [False, barrier.description()]	
				
		if y+1 < 0:
			room = None
		else:
			try:
				room = self.map[y+1][x]
			except IndexError:
				room = None
		
		if room:
			return [True, "You go south."]
		else:
			return [False, "There doesn't seem to be a path to the south."]

	def check_west(self, x, y):
		for enemy in self.map[y][x].enemies:
			if enemy.direction == 'west':
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if barrier.direction == 'west' and not barrier.passable:
				return [False, barrier.description()]	
	
		if x-1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x-1]
			except IndexError:
				room = None
		
		if room:
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be a path to the west."]
			
	def check_east(self, x, y):
		for enemy in self.map[y][x].enemies:
			if enemy.direction == 'east':
				return [False, enemy.check_text()]		
		for barrier in self.map[y][x].barriers:
			if barrier.direction == 'east' and not barrier.passable:
				return [False, barrier.description()]	
				
		if x+1 < 0:
			room = None
		else:
			try:
				room = self.map[y][x+1]
			except IndexError:
				room = None
		
		if room:
			return [True, "You head east."]
		else:
			return [False, "There doesn't seem to be a path to the east."]
			
	def add_implied_barriers(self, x, y):

		[status, text] = self.check_north(x, y)
		barrier_present = False
		if not status:
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'north':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'north':
					barrier_present = True
			if not barrier_present:
				self.map[y][x].add_barrier(barriers.Wall('n'))
				
		[status, text] = self.check_south(x, y)
		barrier_present = False
		if not status:
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'south':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'south':
					barrier_present = True
			if not barrier_present:
				self.map[y][x].add_barrier(barriers.Wall('s'))
			
		[status, text] = self.check_east(x, y)
		barrier_present = False
		if not status:
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'east':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'east':
					barrier_present = True
			if not barrier_present:
				self.map[y][x].add_barrier(barriers.Wall('e'))
			
		[status, text] = self.check_west(x, y)
		barrier_present = False
		if not status:
			for enemy in self.map[y][x].enemies:
				if enemy.direction == 'west':
					barrier_present = True
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'west':
					barrier_present = True
			if not barrier_present:
				self.map[y][x].add_barrier(barriers.Wall('w'))
		
	def update_rooms(self, player):
		for row in self.map:
			for room in row:
				if room:
					player = room.update(player)	
		return player




