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
			if(self.teleport):
				player.x = self.teleport[0]
				player.y = self.teleport[1]
			for enemy in self.enemies:
				if(enemy.agro):
					agro_text = "The %s seems very aggitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)	
		return player


class relica(Maptile):
	descripion = ""


class storage(Maptile):
	descripion = ""


class storeroom(Maptile):
	descripion = ""


class bedrooma(Maptile):
	description = """
	This bedroom likely belonged to an apprentice, judging by the robes in the closet. 
	A small bed lies on one wall, while a dresser faces it from the other side. The walls are bare of adornment.
		"""
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
	description = """The demo is now over. Thank you for playing! We might expand it in the future.
	
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
	You leave the temple, heading out to your mission. Will you succeed? You hope so. \
	The introduction is now over. Have fun, and good luck.
		""" 
	
	teleport = [5,4]


class housestudy(Maptile):
	description = """A desk lies before you, covered with papers. Looking at them, you realize just how long you were trapped. (........) 
		It's been forty years. Looking at the rest of the documents, your heart plummets. The Temple is gone. The Jedi are dead, as is some 
		"Emperor".
	
		"""


class foyer(Maptile):
	description = """You see the outside world to the north. There's a door to the west. You feel like you could open it now, if you wanted.
	
		""" 


class housekitchen(Maptile):
	description = """A great stench attacks your nostrils. It seems all the food stored here rotted away. You see two ways out: 
		one to the south and one to the east.
	
		"""


class staffroom(Maptile):
	description = """This seems to be the housing for the rest of the staff. The kitchen is to the west.
	
		"""

class trophyteleport(Maptile):
	description =  """
		As you grasp the object, a strange fog comes over your vision. You fall to the floor, mind cloudy. \
		You fade in and out of consciousness, understanding little of your surroundings. A pair of shoes. \
		Strange hands lifting you up. A voice (Male? Female? You can't tell), strident and loud, admonishing \
		someone for "rough handling". You see blue eyes, then your mind gives out. All is black. All is quiet.
		(......................................................................................................)
		Time passes, though you hardly notice. People come and people go.
		(......................................................................................................)
		Something disrupts the peace. You fall to the floor (were you standing?), and look up to a strange face. Shaggy
		blond hair is all you can really make out. Your vision is bad. The presence leaves. Time passes. You wake up again. 
		You stand up.
		"""
	
	teleport = [0,5]


class introfoyer(Maptile):
	description = """You stand just within the entrance to a large, ornate home. Looking at the furniture, you think it may be actual wood. \
		A locked door lies to the west. Ignore it for now; your mission lies elsewhere.
	
		"""


class temple(Maptile):
	description = """ You've passed your Trials and are now a Knight. Your first mission lies ahead of you: retrieve an ancient holocron. \
		Recently lost after events above your security clearance, it has been found at the home of a wealthy merchant. \
		He is known to collect strange trinkets, but it is highly unlikely he actually knows what it is. \
		Be careful, young Knight, and do try not to attract attention. (...........)

		Your old master pulls you aside before you leave, giving you a few last words of wisdom: \
		"Do not tarry. Get in and get out. Watch your surroundings and listen to your instincts."
	
		"""


class trophyroomup(Maptile):
	description = """A large case dominates one wall. Somehow, you know that's where you were. Preserved as some kind of trophy for... 
		you don't know how long it was. Too long. Different technologies cover the stands, now. It's not important. You need to get back to the Temple. 
		A bad feeling rises in your gut, but you push it aside. You need to get moving, and the only exit is to the south.
	
		"""


class frontparlor(Maptile):
	description = """The front parlor. Strange to think it was only this morning that you got here. Well, not quite. Close enough. The foyer is to the north,
		the solar to the south, and there seems to be a table in the room to the east.
	
		"""


class diningroom(Maptile):
	description = """This is a dining room. Food lies rotten on the table. Did the merchant leave in a hurry? Are they still alive?
	
		"""


class keys(Maptile):
	description = """There's a bed, halfway rotten. There's a shelf, too, filled with keys. No other furniture is in sight. 
		The rest of the hut is to the south of you.
	
		"""
	items = [items.Red_Keychip("A red keychip catches your eye. You should probably take it.")]


class trophyroomupintro(Maptile):
	description = """The room you stand in now is devoted to relics of technology. Ancient droid models line one wall, primitive display screens another. \
		Your eyes drift to the holocron, which lies - seemingly unguarded and without alarms - on a pedestal. (........)

		You reach toward it, but then withdraw. A feeling in your gut tells you that, once you take it, things will change. Drastically. (......)

		To pick up the holocron, proceed north. To roam the house, do literally anything else.
	
		"""


class frontparlorintro(Maptile):
	description = """You step into a beautiful front parlor. Another locked door is to the east. The foyer lies to the north, while \
		sunlight streams in from the south. You would stop to appreciate the skill of the interior decorator, but you really don't have the time.
	
		"""


class timeskip(Maptile):
	description = """Over the years, you hone your powers. Training is not easy, but it is rewarding. Your connection to the Force increases, as does your skillset. \
		You now have Force Throw as an ability. By consuming two Force Points, you can use your environment as a weapon. Not sand, though. Very hard to get a good \
		grip on sand.

		"""	


class trophyroommain(Maptile):
	description = """You're back in the main trophy hall. Some subtle differences catch your eye. The color of the paint. A new painting. \
		There are two ways to go: south and east.
	
		"""


class solar(Maptile):
	description = """The solar. The windows still let in light, but it's dimmer. It seems to be evening.
		The doors open to the south and the east. You see the front parlor to the north.
	
		"""


class courtyardup(Maptile):
	description = """The cobblestone path is filled with weeds. The gardens are so overgrown you can't even tell what it 
		originally looked like. The whole place is a monument to decay. The house lies to the west, some statues to the south, 
		and some kind of hut to the east.
	
		"""


class gardenerhut(Maptile):
	description = """The gardener's hut. It's old and decrepit, but still seems to be structurally sound. Various fertilizers 
		and tools line the walls. Another room lies to the north, and there is courtyard to the west and south.
	
		"""


class trophyroommainintro(Maptile):
	description = """You stand in an enormous room, lit dimly. Various displays around the room showcase many objects, from \
		paintings on actual canvas to historical flimsy. The room is seemingly themed around ancient societies. Were this \
		another day, you might examine the exhibits for hours.  (..........)
		You give the room another long look, but the words of your old master linger in your mind. This is not the time to tarry.
	
		"""


class solarintro(Maptile):
	description = """A well-lit solar. More locked doors, one to the south and one to the east. \
		Large windows let in light, and through their misty panes you see a beautiful courtyard. \
		To the north lies the front parlor. You feel a strong pull to the west.
	
		"""


class templespar(Maptile):
	description = """ I'll tell you what skills are in the game. (.......)          
		Attack: exactly what it looks like. Cost: a bit of effort.  (........)
		Force Throw: pick up a random rock and hurl it with the Force. Cost: Not Yet Available.  (.......)
		Force Push: shove your enemy to the ground. Cost: One Force Point. (........)
		Meditate: Regain all spent Force Points. (.......)
		
		The effectiveness of each ability is determined by the class you chose. Have fun!
		"""


class trophyroomlower(Maptile):
	description = """The nature exhibits are different, you can tell immediately. You're certain that there wasn't a full \
		display devoted to the flora and fauna of Alderaan. Why that's there, though, you have no idea. The hall opens to the north.
	
		"""


class courtyardleft(Maptile):
	description = """Once beautiful, the courtyard is now full of weeds. You see statues to the east and the house to the north.
	
		"""


class statuering(Maptile):
	description = """Statues form a ring here. They loom over you, seeming to scowl. There's courtyard in every direction but the south.
	
		"""


class courtyardright(Maptile):
	description = """Vines creep over relics of the past. It's beautiful, but haunting. How long has it been? You see a hut to the north and statues to the west.
	
		"""


class trophyroomlowerintro(Maptile):
	description = """This room is full of nature exhibits. One corner is devoted to preserved sample of extinct flora. Another is full of \
		old fossils. Actual fossils, mind you, not Yoda, though one stone looks a little like his head if you squint.
	
		"""


class startingroom(Maptile):
	description = """ This is the Jedi Temple. Nice. You live here, which isn't too bad. Yesterday, you chose your class. Today, you embark on your journey.
		Note: While in the introduction, you will only be able to proceed north. After you leave the Temple, however, you will be able to move in a variety of directions.
		"""


class World:
	map = [
		[relica(barriers = [barriers.wall('s')]),									storage(barriers = [barriers.wall('s')]),																		storeroom(barriers = [barriers.wall('e'), barriers.relicdoor('w')]),							bedrooma(barriers = [barriers.wall('w'), barriers.wall('e')]),						yourroom(barriers = [barriers.wall('s'), barriers.wall('w')]),					northfield(),																			studentroom(barriers = [barriers.wall('s')])						],
		[study(barriers = [barriers.wall('n'), barriers.wall('e')]),				meditation(barriers = [barriers.wall('n'), barriers.wall('w')]),												corridor(),																						mealroom(barriers = [barriers.wall('e')]),											beach(barriers = [barriers.wall('w'), barriers.wall('n'), barriers.wall('s')]),	trainingfield(),																		medbuilding(barriers = [barriers.wall('n'), barriers.wall('s')])	],
		[bedroomm(barriers = [barriers.wall('s')]),									sparroom(barriers = [barriers.wall('s'), barriers.wall('e'), barriers.bedroomdoor('w')]),						enter(barriers = [barriers.wall('w'), barriers.wall('e'), barriers.door('n')]),					kitchen(barriers = [barriers.wall('w'), barriers.wall('s'), barriers.door('e')]),	landingarea(barriers = [barriers.wall('n'), barriers.wall('w')]),				southfield(barriers = [barriers.wall('s')]),											lukehut(barriers = [barriers.wall('n'), barriers.wall('s')])		],
		[None,																		spacea(barriers = [barriers.wall('n')]),																		spaceb(barriers = [barriers.wall('w'), barriers.wall('s')]),									hyperspace(barriers = [barriers.wall('n'), barriers.wall('s')]),					spacec(barriers = [barriers.wall('s')]),										store(barriers = [barriers.wall('n'), barriers.wall('s'), barriers.wall('e')]),			templeteleport()													],
		[housestudy(barriers = [barriers.wall('n'), barriers.wall('s')]),			foyer(barriers = [barriers.wall('e'), barriers.foyerdoor('w')], enemies = [enemies.StormtrooperGroup()]),		housekitchen(barriers = [barriers.wall('w'), barriers.wall('n'), barriers.woodendoor('e')]),	staffroom(barriers = [barriers.wall('n'), barriers.wall('s')]),						trophyteleport(),																introfoyer(barriers = [barriers.wall('n'), barriers.wall('e')]),						temple(barriers = [barriers.wall('w'), barriers.wall('s')])			],
		[trophyroomup(barriers = [barriers.wall('e'), barriers.wall('n')]),			frontparlor(barriers = [barriers.wall('w')], enemies = [enemies.Stormtrooper('n')]),							diningroom(barriers = [barriers.wall('s'), barriers.wall('e')]),								keys(barriers = [barriers.wall('n'), barriers.wall('w'), barriers.wall('e')]),		trophyroomupintro(barriers = [barriers.wall('w'), barriers.wall('e')]),			frontparlorintro(barriers = [barriers.wall('w'), barriers.wall('e')]),					timeskip(barriers = [barriers.wall('w'), barriers.wall('s')])		],
		[trophyroommain(),															solar(enemies = [enemies.Stormtrooper()]),																		courtyardup(barriers = [barriers.wall('n')]),													gardenerhut(barriers = [barriers.door('n'), barriers.wall('e')]),					trophyroommainintro(barriers = [barriers.wall('w')]),							solarintro(barriers = [barriers.wall('s'), barriers.wall('e'), barriers.door('w')]),	templespar(barriers = [barriers.wall('w'), barriers.wall('s')])		],
		[trophyroomlower(barriers = [barriers.wall('e')]),							courtyardleft(barriers = [barriers.wall('w')]),																	statuering(),																					courtyardright(barriers = [barriers.wall('e')]),									trophyroomlowerintro(barriers = [barriers.wall('w')]),							None,																					startingroom()														]
	]

	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
					self.add_implied_barriers(j,i)	# If there are implied barriers (e.g. edge of map, adjacent None room, etc.) add a wall.
						

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
				self.map[y][x].add_barrier(barriers.wall('n'))	
				
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
				self.map[y][x].add_barrier(barriers.wall('s'))	
			
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
				self.map[y][x].add_barrier(barriers.wall('e'))	
			
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
				self.map[y][x].add_barrier(barriers.wall('w'))	
		
	def update_rooms(self, player):
		for row in self.map:
			for room in row:
				if(room):
					player = room.update(player)	
		return player



