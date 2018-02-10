class Maptile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")

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

class spacetile(Maptile):
	def intro_text(self)
		return """
		
		"""

class hyperspace(Maptile):
	def intro_text(self):
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

def tile_at(x, y):
	if x<0 or y<0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None

class World:	# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[relica(),storage(),storeroom(),bedrooma(),yourroom(),northfield(),studentroom()]
		[study(),meditation(),corridor(),mealroom(),beach(),trainingfield(),medbuilding()]
		[bedroomm(),sparroom(),enter(),kitchen(),landingarea(),southfield(),lukehut()]
		[None,spacetile(),spacetile(),hyperspace(),spacetile(),store(),teleport()]
		[housestudy(),foyer(),housekitchen(),staffroom(),None,introfoyer(),temple()]
		[trophyroomup(),frontparlor(),diningroom(),keys(),trophyroomupintro(),frontparlorintro(),timeskip()]
		[trophyroommain(),solar(),courtyardup(),gardenerhut(),trophyroommainintro(),solarintro(),templespar()]
		[trophyroomdown(),courtyardl(),statuering(),courtyardr(),trophyroomdownintro(),None,startingroom()]
	]
	
	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		if y-1 < 0:
			room = None
		try:
			room = self.map[y-1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be anything to the north."]
			
	def check_south(self, x, y):
		if y+1 < 0:
			room = None
		try:
			room = self.map[y+1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be anything to the south."]

	def check_west(self, x, y):
		if x-1 < 0:
			room = None
		try:
			room = self.map[y][x-1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be anything to the west."]
			
	def check_east(self, x, y):
		if x+1 < 0:
			room = None
		try:
			room = self.map[y][x+1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be anything to the east."]
