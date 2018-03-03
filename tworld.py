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
			if(teleport):
				player.x = teleport[0]
				player.y = teleport[1]
			for enemy in self.enemies:
				if(enemy.agro):
					agro_text = "The %s seems very aggitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)	
		return player


class relica(Maptile):
	descripion = 


class storage(Maptile):
	descripion = 


class storeroom(Maptile):
	descripion = 


class bedrooma(Maptile):
	description = """
	This bedroom likely belonged to an apprentice, judging by the robes in the closet. 
	A small bed lies on one wall, while a dresser faces it from the other side. The walls are bare of adornment.
		""""
	items = [items.Green_Keychip("A green keychip lies on the dresser.")]


class yourroom(Maptile):
	description = """
	
		"""


class northfield(Maptile):
	description = """
	
		"""


class studentroom(Maptile):
	description = """
	
		"""


class study(Maptile):
	description = """
	
		"""


class meditation(Maptile):
	description = """
	
		"""


class corridor(Maptile):
	description = """
	
		"""


class mealroom(Maptile):
	description = """
	
		"""


class beach(Maptile):
	description = """
	
		"""


class trainingfield(Maptile):
	description = """
	
		"""


class medbuilding(Maptile):
	description = """
	
		"""


class bedroomm(Maptile):
	description = """
	
		"""
	items = [items.Blue_Keychip("A blue keychip lies on the bed.")]


class sparroom(Maptile):
	description = """
	
		"""


class enter(Maptile):
	description = """
	
		"""


class kitchen(Maptile):
	description = """
	
		"""


class landingarea(Maptile):
	description = """
	
		"""


class southfield(Maptile):
	description = """
	
		"""


class lukehut(Maptile):
	description = """
	
		"""


class spacea(Maptile):
	description = """
	
		"""

	teleport = [1,3]


class spaceb(Maptile):
	description = """
	
		"""


class hyperspace(Maptile):
	description = """
	
		"""


class spacec(Maptile):
	description = """
	
		"""


class store(Maptile):
	description = """
	
		"""


class templeteleport(Maptile):
	description = """
	You leave the temple, heading out for a mission. You are to retrieve an ancient holocron, which was recently stolen. 
	Be careful, young Knight, and do not draw attention.
		""" 
	
	teleport = [5,4]


class housestudy(Maptile):
	description = """
	
		"""


class foyer(Maptile):
	description = """
	
		""" 


class housekitchen(Maptile):
	description = """
	
		"""


class staffroom(Maptile):
	description = """
	
		"""

class trophyteleport(Maptile):
	description =  """
		As you grasp the object, a strange fog comes over your vision. You fall to the floor, mind cloudy.
		You fade in and out of consciousness, understanding little of your surroundings. A pair of shoes. 
		Strange hands lifting you up. A voice (Male? Female? You can't tell), strident and loud, admonishing 
		someone for "rough handling". You see blue eyes, then your mind gives out. All is black. All is quiet.
		"""
	
	teleport = [0,5]


class introfoyer(Maptile):
	description = """
	
		"""


class temple(Maptile):
	description = """
	
		"""


class trophyroomup(Maptile):
	description = """
	
		"""


class frontparlor(Maptile):
	description = """
	
		"""


class diningroom(Maptile):
	description = """
	
		"""


class keys(Maptile):
	description = """
	
		"""


class trophyroomupintro(Maptile):
	description = """
	
		"""


class frontparlorintro(Maptile):
	description = """
	
		"""


class timeskip(Maptile):
	description = """
	
		"""


class trophyroommain(Maptile):
	description = """
	
		"""


class solar(Maptile):
	description = """
	
		"""


class courtyardup(Maptile):
	description = """
	
		"""


class gardenerhut(Maptile):
	description = """
	
		"""


class trophyroommainintro(Maptile):
	description = """
	
		"""


class solarintro(Maptile):
	description = """
	
		"""


class templespar(Maptile):
	description = """
	
		"""


class trophyroomlower(Maptile):
	description = """
	
		"""


class courtyardleft(Maptile):
	description = """
	
		"""


class statuering(Maptile):
	description = """
	
		"""


class courtyardright(Maptile):
	description = """
	
		"""


class trophyroomlowerintro(Maptile):
	description = """
	
		"""


class startingroom(Maptile):
	description = """
	
		"""


class World:
	map = [
		[relica(barriers = [barriers.wall('s')]),									storage(barriers = [barriers.wall('s')]),																		storeroom(barriers = [barriers.wall('e'), barriers.relicdoor('w')]),							bedrooma(barriers = [barriers.wall('w'), barriers.wall('e')]),						yourroom(barriers = [barriers.wall('s'), barriers.wall('w')]),					northfield(),																		studentroom(barriers = [barrier.wall('s')])							]
		[study(barriers = [barriers.secretdoor('n'), barriers.wall('e')]),			meditation(barriers = [barriers.wall('n'), barriers.wall('w')]),												corridor(),																						mealroom(barriers = [barriers.wall('e')]),											beach(barriers = [barriers.wall('w'), barriers.wall('n'), barriers.wall('s')]),	trainingfield(),																	medbuilding(barriers = [barriers.wall('n'), barriers.wall('s')])	]
		[bedroomm(barriers = [barriers.wall('s')]),									sparroom(barriers = [barriers.wall('s'), barriers.wall('e'), barriers.bedroomdoor('w')]),						enter(barriers = [barriers.wall('w'), barriers.wall('e'), barriers.door('n')]),					kitchen(barriers = [barriers.wall('w'), barriers.wall('s'), barriers.door('e')]),	landingarea(barriers = [barriers.wall('n'), barriers.wall('w')]),				southfield(barriers = [barriers.wall('s')]),										lukehut(barriers = [barriers.wall('n'), barriers.wall('s')])		]
		[None,																		spacea(barriers = [barriers.wall('n')]),																		spaceb(barriers = [barriers.wall('w'), barriers.wall('s')]),									hyperspace(barriers = [barriers.wall('n'), barriers.wall('s')]),					spacec(barriers = [barriers.wall('s')]),										store(barriers = [barriers.wall('n'), barriers.wall('s'), barriers.wall('e')]),		templeteleport()													]
		[housestudy(barriers = [barriers.wall('n'), barriers.wall('s')]),			foyer(barriers = [barriers.wall('e'), barriers.foyerdoor('w')], enemies = [enemies.StormtrooperGroup()]),		housekitchen(barriers = [barriers.wall('w'), barriers.wall('n'), barriers.woodendoor('e')]),	staffroom(barriers = [barriers.wall('n'), barriers.wall('s')]),						trophyteleport(),																introfoyer(barriers = [barriers.wall('n'), barriers.wall('e')]),					temple(barriers = [barriers.wall('w'), barriers.wall('s')])			]
		[trophyroomup(barriers = [barriers.wall('e'), barriers.secretdoor('n')]),	frontparlor(barriers = [barriers.wall('w')], enemies = [enemies.ImperialOfficer('n')]),							diningroom(barriers = barriers.wall('s'), barriers.wall('e')]),									keys(barriers = barriers.wall('n'), barriers.wall('w'), barriers.wall('e')]),		trophyroomupintro(barriers = [barriers.wall('w'), barriers.wall('e')]),			frontparlorintro(barriers = barriers.wall('w'), barriers.wall('e')]),				timeskip(barriers = [barriers.wall('w'), barriers.wall('s')])		]
		[trophyroommain(),															solar(enemies = [enemies.Stormtrooper()]),																		courtyardup(barriers = [barriers.wall('n')]),													gardenerhut(barriers = [barriers.door('n'), barriers.wall('e')]),					trophyroommainintro(barriers = barriers.wall('w')]),							solarintro(barriers = barriers.wall('s'), barriers.wall('e')]),						templespar(barriers = barriers.wall('w'), barriers.wall('s')])		]
		[trophyroomlower(barriers = [barriers.wall('e')]),							courtyardleft(barriers = barriers.wall('w')]),																	statuering(),																					courtyardright(barriers = [barriers.wall('e')]),									trophyroomlowerintro(barriers = barriers.wall('w')]),							None,																				startingroom()														]
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
			return [True, "You move to the north."]
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
			return [True, "You go south."]
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
			return [True, "You head east."]
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
					player = room.update(player)	
		return player




