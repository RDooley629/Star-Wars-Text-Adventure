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


world_map = [
	[relica(0,0),storage(1,0),storeroom(2,0),bedrooma(3,0),yourroom(4,0),northfield(5,0),studentroom(6,0)]
	[study(0,1),meditation(1,1),corridor(2,1),mealroom(3,1),beach(4,1),trainingfield(5,1),medbuilding(6,1)]
	[bedroomm(0,2),sparroom(1,2),enter(2,2),kitchen(3,2),landingarea(4,2),southfield(5,2),lukehut(6,2)]
	[None,spacetile(1,3),spacetile(2,3),hyperspace(3,3),spacetile(4,3),store(5,3),teleport(6,3)]
	[housestudy(0,4),foyer(1,4),housekitchen(2,4),staffroom(3,4),None,introfoyer(5,4),temple(6,4)]
	[trophyroomup(0,5),frontparlor(1,5),diningroom(2,5),keys(3,5),trophyroomupintro(4,5),frontparlorintro(5,5),timeskip(6,5)]
	[trophyroommain(0,6),solar(1,6),courtyardup(2,6),gardenerhut(3,6),trophyroommainintro(4,6),solarintro(5,6),templespar(6,6)]
	[trophyroomlower(0,7),courtyardleft(1,7),statuering(2,7),courtyardright(3,7),trophyroomlowerintro(4,7),None,startingroom(6,7)]
]

def tile_at(x, y):
	if x<0 or y<0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None
