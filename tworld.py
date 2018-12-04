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
			text += "" + enemy.check_text()
		for barrier in self.barriers:
			if barrier.direction:
				if barrier.direction not in directions_blocked:
					if barrier.verbose:
						text += "" + barrier.description()
		for npc in self.npcs:
			text += "" + npc.check_text()
		for item in self.items:
			text += "" + item.room_text()

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
					agro_text = "The %s seems very agitated. It attacks! " % enemy.name
					agro_text += player.take_damage(enemy.damage)
					print()
					print(agro_text)	
		return player


#

class FoodComa(Maptile):
	description = \
		"""You gorge yourself on food, revelling in the taste of airport food. \n\
Soon, you find your eyelids growing heavy. Despite yourself, you soon fall asleep. \n\
You die in your sleep. Whether by zombie or by heart attack, the world may never know. \n\
Victory is yours, I suppose.
"""


class FoodCourt(Maptile):
	description = \
		"""The airport food court, where new travellers stress-eat their \n\
worries away and old travellers rest between layovers.
"""


class MainAirport(Maptile):
	description = \
		"""Terminals stretch before you, empty as can be. While you could wander for hours, there \n\
are only a few places that you think could be useful right now. To the east is the monorail, which could bring \n\
you to the outer terminals. To the west is the food court, if you're hungry at all. To the south are the escalators, \n\
bane of shoelaces everywhere.
"""


class Monorail(Maptile):
	description = \
		"""The rails are empty at first, but the monorail rumbles over after a few short minutes \n\
of waiting. There doesn't seem to be anybody else on board. Hesitantly, you step onto the old carpet, hard \n\
beneath your feet. After a few minutes, the monorail takes off again. The familiar female voice tells you \n\
once you've arrived to Terminal D, International Flights. You step off, only to see a German woman wave you over \n\
to a gate. It seems an arriving flight landed, realized there were zombies, and turned around to leave. \n\
You were just in time. Victory is yours.
"""


class MarioCart(Maptile):
	description = \
		"""Luggage carts both full and empty litter the area. The sky stretches between the horizon and \n\
the airport, blue as your daughter's eyes. Clouds of cotton dot the sky like water on the wall after a dog \n\
shakes itself dry. The main airport lies to the west, but you see the runway stretch south. There are some \n\
zombies there, but a luggage cart could probably maneuver its way through them safely. There's a red one that \n\
looks like it could do the job.
"""


class Gate(Maptile):
	description = \
		"""You're standing in Terminal B, specifically between gates B12 and B13. To the south - \n\
toward gate B15 - you hear the rumble of feet within a passenger boarding bridge. There might be a plane \n\
docked there, but it could just as easily be more zombies. To the west is a staircase that leads to ground level. \n\
There are probably some luggage carts down there, if you want to take a look. To the east, the escalator \n\
continues its continual climb upward.
"""


class Escalator(Maptile):
	description = \
		"""The escalators lies before you, forever churning their steps forward. \n\
To the south lies the security checkpoint. To the west, you see Terminal B. North lies the \n\
the heart of the airport. To the east is the contraband room. You never know what you'll \n\
find in there, really.
"""


class Contraband(Maptile):
	description = \
		"""Ah, the contraband room. All sorts of things have ended up here, from machetes to rifles. \n\
Good times. At any rate, it also doubles as a sort of break room during lunch. Sure, there's an \n\
official break room, but you and your buddy Joe used to hang out in here with burgers and guess \n\
how people decided to bring each thing into an airport. ANYWAY! Nostalgia aside, the exit lies \n\
to the west, along with the rest of the airport. Every other wall is covered in storage lockers, \n\
cat posters, or cat poster-covered storage lockers.
"""


class LuggageVoid(Maptile):
	description = \
		"""You maneuver your way through the zombies with ease, reflexes honed by years of battling \n\
your siblings in Mario Cart. You pull off of the runway and onto a side path, headed away from \n\
the airport. You see the vast concrete fields of rental cars, highways, and parking structures \n\
stretching before you, but success is snatched away just as you begin to taste it. \n\
The first thing you recognize is that it's cold. The second is that you don't really feel gravity \n\
anymore. Looking around, your lose your breath. A great brown orb lies before you, dominating \n\
the sky and surrounded by a halo of stars. To your sides, floating pieces of luggage fill \n\
the air. You reach out to grab a handle, but the world lurches once more as you make contact. \n\
You wake up in your bed, drenched in sweat. Clutched in your hand is a suitcase you've never \n\
seen before. Inside lies nothing but a model of the solar system, engraved with "Victory is yours."
"""


class Plane(Maptile):
	description = \
		"""Walking over to gate B15, you see what seems to be a group of soldiers hurrying \n\
into the airport. In a flurry of events, you're spotted, escorted onto the plane by \n\
two men, and brought to a military base you don't remember hearing the name of. You \n\
don't remember much of the flight. You're asked a great many questions, but you're \n\
finally released and sent back home. Victory is yours."""


class Checkpoint(Maptile):
	description = \
		"""You find yourself at the security checkpoint. \n\
You've confiscated many a Zippo and dumped many a water bottle here. \n\
To the north are the escalators, which will take you to the body of the airport. \n\
To the south is the entrance lobby, which then leads to the rental cars. 
"""


class Bathroom(Maptile):
	description = \
		"""Surrounding you is an airport bathroom. There really isn't much to \n\
say here beyond that it's a bathroom, you're in it, and there's some 2012 \n\
pop song playing over the speakers.
"""


class Cars(Maptile):
	description = \
		"""While this parking lot is filled with rental cars, you park a little further out. \n\
It takes you a few minutes, but you finally make it to the employee parking garage. \n\
You walk down the line of cars, then come to a stop before a motorcycle. As you \n\
cruise off into the distance, you smile. There are a great many rides out there, \n\
but this Victory is yours."""


class TicketCounter(Maptile):
	description = \
		"""The ticket counters line the wall to the north, empty of their normal staff. It seems \n\
like nobody else got caught in zombieland. Still, it's certainly given you a great \n\
story for the kiddos. To the west are the rental cars (why the airport decided to \n\
put the rental cars here as well as by departures is a mystery} and to the east is \n\
the lobby. What do you want to do?
"""


class Lobby(Maptile):
	description = \
		"""You stand in the lobby of the airport. Above you is some trendy, modern-looking \n\
sculpture that probably cost way too much.
"""


class LobbyEast(Maptile):
	description = \
		"""The east section of the lobby. Calming music plays over the speakers. It really doesn't \n\
seem appropriate for Raindrops by Chopin to be playing during a zombie \n\
apocalypse, though. To the north are the bathrooms. To the west is the \n\
main lobby. That's about it, really.
"""

#


class World:
	map = [
		[FoodComa(), 									FoodCourt(barriers=[barriers.Wall('s')], items=[items.Smoothie()]),	MainAirport(enemies=[enemies.ZombieHorde('e')]), 				Monorail()	],
		[MarioCart(barriers=[barriers.Wall('n')]), 	Gate(barriers=[barriers.Wall('n')], enemies=[enemies.Zombie('w')]),	Escalator(barriers=[barriers.lockeddoor('e')]), 				Contraband(barriers=[barriers.Wall('n'), barriers.Wall('s'), barriers.Door('w')], items=[items.Shotgun(), items.Grenade(), items.Old_Donut()])	],
		[LuggageVoid(), 								Plane(), 																Checkpoint(barriers=[barriers.Wall('e'), barriers.Wall('w')]),	Bathroom(barriers=[barriers.Wall('n'), barriers.Wall('w')], enemies=[enemies.Zombie('s')])],
		[Cars(), 										TicketCounter(barriers=[barriers.Wall('n'), barriers.Sliding('w')]), 	Lobby(enemies=[enemies.Zombie('w')], items=[items.Keychip()]),	LobbyEast()	]


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

#
