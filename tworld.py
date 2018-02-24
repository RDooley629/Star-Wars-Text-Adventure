class Maptile:
	description = "Do not create raw MapTiles! Create a subclass instead!"
	barriers = []
	enemies = []
	items = []
	
	def __init__(self, x=0, y=0, barriers = [], items = [], enemies = []):
		self.x = x
		self.y = y
		for barrier in barriers:
			self.add_barrier(barrier)
		for item in items:
			self.add_item(item)
		for enemy in enemies:
			self.add_enemy(enemy)
	
	def intro_text(self):
		text = self.description
		for barrier in self.barriers:
			if(barrier.verbose):
				text += " " + barrier.description()
		#for enemy in self.contents['enemies']:
		#	text += " " + enemy.description()
		for item in self.items:
			text += " " + item.room_text()
		return text
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(not noun2):
			if(verb == 'check'):
				for item in self.items:
					if(item.name.lower() == noun1):
						return [True, item.check_text(), inventory]
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

		for list in [self.barriers, self.items, self.enemies]:
			for item in list:
				[status, description, inventory] = item.handle_input(verb, noun1, noun2, inventory)
				if(status):
					return [status, description, inventory]
					
		for list in [self.barriers, self.items, self.enemies]:			# Added to give the player feedback if they have part of the name of an object correct.
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

	


class relica(Maptile):
	def intro_text(self)
		return """
		
		"""

class storage(Maptile):
	def intro_text(self):
		return """
		
		"""

class storeroom(Maptile):
	def intro_text(self):
		return """
		
		"""

class bedrooma(Maptile):
	def intro_text(self)
		return """
		
		"""

class yourroom(Maptile):
	def intro_text(self):
		return """
		
		"""

class northfield(Maptile):
	def intro_text(self):
		return """
		
		"""

class studentroom(Maptile):
	def intro_text(self)
		return """
		
		"""

class study(Maptile):
	def intro_text(self):
		return """
		
		"""

class meditation(Maptile):
	def intro_text(self):
		return """
		
		"""

class corridor(Maptile):
	def intro_text(self)
		return """
		
		"""

class mealroom(Maptile):
	def intro_text(self):
		return """
		
		"""

class beach(Maptile):
	def intro_text(self):
		return """
		
		"""

class trainingfield(Maptile):
	def intro_text(self)
		return """
		
		"""

class medbuilding(Maptile):
	def intro_text(self):
		return """
		
		"""

class bedroomm(Maptile):
	def intro_text(self):
		return """
		
		"""

class sparroom(Maptile):
	def intro_text(self)
		return """
		
		"""

class enter(Maptile):
	def intro_text(self):
		return """
		
		"""

class kitchen(Maptile):
	def intro_text(self):
		return """
		
		"""

class landingarea(Maptile):
	def intro_text(self)
		return """
		
		"""

class southfield(Maptile):
	def intro_text(self):
		return """
		
		"""

class lukehut(Maptile):
	def intro_text(self):
		return """
		
		"""

class spacea(Maptile):
	def intro_text(self)
		return """
		
		"""

class spaceb(Maptile):
	def intro_text(self)
		return """
		
		"""

class hyperspace(Maptile):
	def intro_text(self):
		return """
		
		"""

class spacec(Maptile):
	def intro_text(self)
		return """
		
		"""

class store(Maptile):
	def intro_text(self):
		return """
		
		"""

class teleport(Maptile):
	def intro_text(self)
		return """
		
		"""

class housestudy(Maptile):
	def intro_text(self):
		return """
		
		"""

class foyer(Maptile):
	def intro_text(self):
		return """
		
		"""

class housekitchen(Maptile):
	def intro_text(self)
		return """
		
		"""

class staffroom(Maptile):
	def intro_text(self):
		return """
		
		"""

class introfoyer(Maptile):
	def intro_text(self):
		return """
		
		"""

class temple(Maptile):
	def intro_text(self)
		return """
		
		"""

class trophyroomup(Maptile):
	def intro_text(self):
		return """
		
		"""

class frontparlor(Maptile):
	def intro_text(self):
		return """
		
		"""

class diningroom(Maptile):
	def intro_text(self)
		return """
		
		"""

class keys(Maptile):
	def intro_text(self):
		return """
		
		"""

class trophyroomupintro(Maptile):
	def intro_text(self):
		return """
		
		"""

class frontparlorintro(Maptile):
	def intro_text(self)
		return """
		
		"""

class timeskip(Maptile):
	def intro_text(self):
		return """
		
		"""

class trophyroommain(Maptile):
	def intro_text(self):
		return """
		
		"""

class solar(Maptile):
	def intro_text(self)
		return """
		
		"""

class courtyardup(Maptile):
	def intro_text(self):
		return """
		
		"""

class gardenerhut(Maptile):
	def intro_text(self):
		return """
		
		"""

class trophyroommainintro(Maptile):
	def intro_text(self)
		return """
		
		"""

class solarintro(Maptile):
	def intro_text(self):
		return """
		
		"""

class templespar(Maptile):
	def intro_text(self):
		return """
		
		"""

class trophyroomlower(Maptile):
	def intro_text(self)
		return """
		
		"""

class courtyardleft(Maptile):
	def intro_text(self):
		return """
		
		"""

class statuering(Maptile):
	def intro_text(self):
		return """
		
		"""

class courtyardright(Maptile):
	def intro_text(self)
		return """
		
		"""

class trophyroomlowerintro(Maptile):
	def intro_text(self):
		return """
		
		"""

class startingroom(Maptile):
	def intro_text(self):
		return """
		
		"""

class World:
	map = [
		[relica(barriers = [barriers.wall('s')]),									storage(barriers = [barriers.wall('s'), barriers.lockeddoor('w')]),							storeroom(barriers = [barriers.wall('e')]),										bedrooma(barriers = [barriers.wall('w'), barriers.wall('e')]),						yourroom(barriers = [barriers.wall('s'), barriers.wall('w')]),					northfield(),																		studentroom(barriers = [barrier.wall('s')])							]
		[study(barriers = [barriers.secretdoor('n'), barriers.wall('e')]),			meditation(barriers = [barriers.wall('n'), barriers.wall('w')]),							corridor(),																		mealroom(barriers = [barriers.wall('e')]),											beach(barriers = [barriers.wall('w'), barriers.wall('n'), barriers.wall('s')]),	trainingfield(),																	medbuilding(barriers = [barriers.wall('n'), barriers.wall('s')])	]
		[bedroomm(barriers = [barriers.wall('s')]),									sparroom(barriers = [barriers.wall('s'), barriers.wall('e'), barriers.lockeddoor('w')]),	enter(barriers = [barriers.wall('w'), barriers.wall('e'), barriers.door('n')]),	kitchen(barriers = [barriers.wall('w'), barriers.wall('s'), barriers.door('e')]),	landingarea(barriers = [barriers.wall('n'), barriers.wall('w')]),				southfield(barriers = [barriers.wall('s')]),										lukehut(barriers = [barriers.wall('n'), barriers.wall('s')])		]
		[None,																		spacea(barriers = [barriers.wall('n')]),													spaceb(),																		hyperspace(barriers = [barriers.wall('n'), barriers.wall('s')]),					spacec(barriers = [barriers.wall('s')]),										store(barriers = [barriers.wall('n'), barriers.wall('s'), barriers.wall('e')]),		teleport(FIGURETHISOUTLATERTELEPORTSTUFF)							]
		[housestudy(barriers = [barriers.wall('n'), barriers.wall('s')]),			foyer(barriers = [barriers.wall('e'), barriers.lockeddoor('w')]),							housekitchen(barriers = [barriers.wall('w'), barriers.wall('n')]),				staffroom(barriers = [barriers.wall('n'), barriers.wall('s')]),						None,																			introfoyer(barriers = [barriers.wall('n'), barriers.wall('e')]),					temple(barriers = [barriers.wall('w'), barriers.wall('s')])			]
		[trophyroomup(barriers = [barriers.wall('e'), barriers.secretdoor('n')]),	frontparlor(barriers = [barriers.wall('w')]),												diningroom(barriers = barriers.wall('s'), barriers.wall('e')]),					keys(barriers = barriers.wall('n'), barriers.wall('w'), barriers.wall('e')]),		trophyroomupintro(barriers = [barriers.wall('w'), barriers.wall('e')]),			frontparlorintro(barriers = barriers.wall('w'), barriers.wall('e')]),				timeskip(barriers = [barriers.wall('w'), barriers.wall('s')])		]
		[trophyroommain(),															solar(barriers = barriers.lockeddoor('w')]),												courtyardup(barriers = [barriers.wall('n')]),									gardenerhut(barriers = [barriers.door('n'), barriers.wall('e')]),					trophyroommainintro(barriers = barriers.wall('w')]),							solarintro(barriers = barriers.wall('s'), barriers.wall('e')]),						templespar(barriers = barriers.wall('w'), barriers.wall('s')])		]
		[trophyroomlower(barriers = [barriers.wall('e')]),							courtyardleft(barriers = barriers.wall('w')]),												statuering(),																	courtyardright(barriers = [barriers.wall('e')]),									trophyroomlowerintro(barriers = barriers.wall('w')]),							None,																				startingroom()														]
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
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'north':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('n'))	
				
		[status, text] = self.check_south(x,y)
		barrier_present = False
		if(not status):
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'south':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('s'))	
			
		[status, text] = self.check_east(x,y)
		barrier_present = False
		if(not status):
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'east':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('e'))	
			
		[status, text] = self.check_west(x,y)
		barrier_present = False
		if(not status):
			for barrier in self.map[y][x].barriers:
				if barrier.direction == 'west':
					barrier_present = True
			if(not barrier_present):
				self.map[y][x].add_barrier(barriers.Wall('w'))	


