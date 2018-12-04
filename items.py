from random import randint 	# Used to generate random integers.


class Item:
	name = "Do not create raw Item objects!"
	
	description = "You should define a description for items in their subclass."
	dropped_description = "You should define the description for this item after it is dropped in its subclass."
	
	is_dropped = False	# This is going to store the status of whether this item has been picked up and dropped before.
	
	value = 0		# Used to establish value if item is for sale.
		
	def __init__(self, description = "", value = 0):
		if description:
			self.intro_description = description
		else:
			self.intro_description = self.dropped_description
		
		if self.value == 0:
			self.value = value
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if not self.is_dropped:
			# We may want to have a different description for a weapon the first time
			# it is encountered vs. after it has been dropped.
			return self.intro_description
		else:
			return self.dropped_description

	def check_text(self):
		return self.description
		
	def drop(self):
		self.is_dropped = True
		
	def pick_up(self):
		self.is_dropped = False
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class Keychip(Item):
	name = "keychip"
	
	description = "A red keychip from the lobby. You're not sure how it got there."
	dropped_description = "A keychip lies on the ground. That probably breaks regulation."
		
		
class Consumable(Item):
	consume_description = "You should define flavor text for consuming this item in its subclass."

	healing_value = 0		# Define this appropriately in your subclass.
		
	def consume(self):
		return [self.consume_description, self.healing_value]
			

class Crusty_Bread(Consumable):
	name = "crusty bread"
	healing_value = 10
	
	description = "Just a stale old piece of bread."
	dropped_description = "A piece of crusty bread is lying on the ground."
	consume_description = "You eat the crusty piece of bread."


class Old_Donut(Consumable):
	name = "old donut"
	healing_value = 5

	description = "Seems it was made a while back. Still edible, though."
	dropped_description = "An old donut catches your eye."
	consume_description = "You eat the donut. It reminds you of Friday."


class Snack(Consumable):
	name = "snack"
	healing_value = 10

	description = "An overly generic snack. Why did it drop? Who knows."
	dropped_description = "A snack lies on the ground, wrapper intact."
	consume_description = "Popping it open, you take a few bites. It's bland."


class Smoothie(Consumable):
	name = "smoothie"
	healing_value = 45
	
	description = "A protein smoothie. The liquid inside looks suspiciously healthy."
	dropped_description = "A confiscated protein smoothie lies on the ground. Maybe it'd help you feel better."
	consume_description = "You drink the smoothie. You feel your arteries unclogging and your muscles fortifying."
	

class Weapon(Item):	
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0		# Define this appropriately in your subclass.
		
	def equip_text(self):
		return self.equip_description
			
	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)]]
		# def attack(self):
		# return [self.attack_descriptions[randint(0, len(self.attack_descriptions))], self.damage]
		# Return damage and a random attack description from your list.
		# Return a random attack description from your list.


class PepperSpray(Weapon):
	name = "pepper spray"

	description = "Your handy-dandy pepper spray. It tastes horrible... not from experience, though!"
	dropped_description = "Your beloved pepper spray lies on the ground."
	equip_description = "Your pepper spray finds its familiar home on your belt."
	attack_descriptions = ["An orange cone erupts from the nozzle.", "The pepper spray makes contact!", "Pepper spray fills the air."]
	damage = 6


class Shotgun(Weapon):
	name = "shotgun"

	description = "It's a very nice shotgun. Excellent for zombie disposal."
	dropped_description = "A high-quality shotgun lies on the ground."
	equip_description = "The ch-chunk of the shotgun sends a shiver down your spine. Zombies watch out!"
	attack_descriptions = ["Thunder erupts from the muzzle of the gun", "More than ever, you're glad your uncle took you out to the range.", "Your ears ring as the zombie takes the hit."]
	damage = 8


class Grenade(Weapon):
	name = "grenade"

	description = "Who thought it was a good idea to bring this into an airport???"
	dropped_description = "A grenade rolls around on the floor."
	equip_description = "You grab the grenade in your hand."
	attack_descriptions = ["You just lobbed a grenade.", "Calling upon memories of baseball, you hurl the grenade through the air.", "A green chunk of explosive death sails forward."]
	damage = 25

	
class Container:
	name = "Do not create raw Container objects!"
	
	closed_description = "You should define a closed description for containers in their subclass."
	open_description = "You should define an open description for containers in their subclass."
	
	closed = True
	
	contents = []
	
	def __init__(self, items=[]):
		for item in items:
			if len(self.contents) == 0:
				self.contents = [item]
			else:
				self.contents.append(item)
	
	def add_item(self, item):
		if len(self.contents) == 0:
			self.contents = [item]		# Initialize the list if it is empty.
		else:
			self.contents.append(item)		# Add to the list if it is not empty.
			
	def remove_item(self, item):
		removal_index = -1
		for index in range(len(self.contents)):
			if self.contents[index].name == item.name:
				removal_index = index
		if removal_index >= 0:
			self.contents.pop(removal_index)
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if self.closed:					# We may want to have a different description for a container if it is open or closed.
			return self.closed_description
		else:
			return self.open_description

	def check_text(self):
		if self.closed:
			return self.closed_description
		else:
			if len(self.contents) > 0:
				print("The %s contains:" % self.name)
				for item in self.contents:
					print('* ' + str(item).title())
			else:
				return "The %s is empty of anything useful." % self.name
		
	def handle_input(self, verb, noun1, noun2, inventory):			
		return [False, "", inventory]

		
class Storage_Locker(Container):
	name = "storage locker"
	closed_description = "A regulation TSA contraband locker sits on the wall. It's currently closed."
	open_description = "The door of the storage locker lies slightly ajar."

	contents = [Shotgun(), Grenade(), Old_Donut()]

	
	def handle_input(self, verb, noun1, noun2, inventory):
		if noun1 == self.name:
			if verb == 'check':
				return [True, self.check_text(), inventory]
			if verb == 'open':
				if self.closed:
					self.closed = False
					return [True, "Scanning your badge, you open up the locker.", inventory]
				else:
					return [True, "You try to open the locker, only to find that it was already open.", inventory]
			if verb == 'close':
				if not self.closed:
					self.closed = True
					return [True, "Though its heavy, you heave the door shut again.", inventory]
				else:
					return [True, "You try to close the locker, but fail. Turns out it was already closed.", inventory]
		elif noun1:
			if verb == 'take':
				if not self.closed:
					for index in range(len(self.contents)):
						if self.contents[index].name.lower() == noun1:
							if isinstance(self.contents[index], Item):
								pickup_text = "You took the %s from the locker. It's now in your inventory." % self.contents[index].name
								inventory.append(self.contents[index])
								self.contents.pop(index)
								return [True, pickup_text, inventory]
							else:
								return [True, "The %s is too heavy to pick up." % self.contents[index].name, inventory]
			if verb == 'check':
				if not self.closed:
					for index in range(len(self.contents)):
						if self.contents[index].name.lower() == noun1:
							if isinstance(self.contents[index], Item):
								return [True, self.contents[index].check_text(), inventory]
		return [False, None, inventory]
