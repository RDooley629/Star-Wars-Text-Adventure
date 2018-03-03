from random import randint 	# Used to generate random integers.

class Item:
	name = "Do not create raw Item objects!"
	
	description = "You should define a description for items in their subclass."
	dropped_description = "You should define the description for this item after it is dropped in its subclass."
	
	is_dropped = False	# This is going to store the status of whether this item has been picked up and dropped before.
	
	value = 0		# Used to establish value if item is for sale.
	
		
	def __init__(self, description = "", value = 0):
		if(description):
			self.intro_description = description
		else:
			self.intro_description = self.dropped_description
		
		if(self.value == 0):
			self.value = value
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if(not self.is_dropped):					# We may want to have a different description for a weapon the first time it is encountered vs. after it has been dropped.
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
		
		
class Blue_Keychip(Item):
	name = "blue keychip"
	
	description = "A blue keychip. It probably opens a door."
	dropped_description = "A small blue keychip lies on the floor."	

class Green_Keychip(Item):
	name = "green keychip"
	
	description = "A green keychip. It's old, but still in working condition."
	dropped_description = "A green keychip lies on the ground. It's small enough you almost miss it."	

class Red_Keychip(Item):
	name = "red keychip"
	
	description = "A red keychip from the gardener's hut. Probably opens something."
	dropped_description = "An old iron key is lying on the ground."	
		
		
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
			
class Red_Potion(Consumable):
	name = "red potion"
	healing_value = 75
	
	description = "A bottle of mysterious, glowing red potion. For some reason it looks healthy."
	dropped_description = "A bottle of red potion is glowing on the ground."
	consume_description = "You drink the glowing red potion."
	
	
	

class Weapon(Item):	
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]

	damage = 0		# Define this appropriately in your subclass.
		
	def equip_text(self):
		return self.equip_description
			
	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)]]		# Return a random attack description from your list.
		

class GreenLightsaber(Item):
	name = "green lightsaber"

	description = "You hold the lightsaber in your hand. It's comforting."
	droppped_description = "The hilt lies on the ground, quiet. You might want to pick it up."
	equip_description = "A humming green blade emerges from the hilt, bathing the area in light." 
	attack_descriptions = ["You swing the lightsaber.", "Going for a horizontal blow, you nearly cut your foe in half.", "SHWING batabatabata SHWING!"]

class BlueLightsaber(Item):
	name = "blue lightsaber"

	description = "This blade has been with you from childhood. It's seen a lot, but still holds up."
	dropped_description = "You know it's yours. Why isn't it with you?"
	equip_description = "A blue blade hums away from your body. You feel prepared."
	attack_descriptions = ["You slash at your enemy.", "Like an extension of your body, your lightsaber swings through the air.", "You strike at your foe, watching for a response."]

class YellowLightsaber(Item):
	name = "yellow lightsaber"

	description = "It's not the most common blade color, but it's yours. Having it close is comforting."
	dropped_description = "The lightsaber is on the floor. Your belt feels strange without it."
	equip_description = "You equip your lightsaber, and a yellow blade hums happily."
	attack_descriptions = ["You lunge forward, trying to catch your foe off guard.", "You release a mighty sweep of your blade!", "You slice at your enemy, nearly cutting him in half."]


	
	
class Container:
	name = "Do not create raw Container objects!"
	
	closed_description = "You should define a closed description for containers in their subclass."
	open_description = "You should define an open description for containers in their subclass."
	
	closed = True
	
	contents = []
	
	def __init__(self, items = []):
		for item in items:
			if(len(self.contents) == 0):
				self.contents = [item]
			else:
				self.contents.append(item)
	
	def add_item(self, item):
		if(len(self.contents) == 0):
			self.contents = [item]		# Initialize the list if it is empty.
		else:
			self.contents.append(item)	# Add to the list if it is not empty.
			
	def remove_item(self, item):
		removal_index = -1
		for index in range(len(self.contents)):
			if(self.contents[index].name == item.name):
				removal_index = index
		if(removal_index >= 0):
			self.contents.pop(removal_index)
	
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if(self.closed):					# We may want to have a different description for a container if it is open or closed.
			return self.closed_description
		else:
			return self.open_description

	def check_text(self):
		if(self.closed):
			return self.closed_description
		else:
			if(len(self.contents) > 0):
				print("The %s contains:" % self.name)
				for item in self.contents:
					print('* ' + str(item).title())
			else:
				return "The %s is empty." % self.name
		
	def handle_input(self, verb, noun1, noun2, inventory):			
		return [False, "", inventory]

		
class Old_Chest(Container):
	name = "old chest"
	closed_description = "A battered old chest sits against the far wall, its lid shut tightly."
	open_description = "A battered old chest sits against the far wall, its lid open wide."
	
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == self.name):
			if(verb == 'check'):
				return [True, self.check_text(), inventory]
			if(verb == 'open'):
				if(self.closed == True):
					self.closed = False
					return [True, "You pry the lid of the battered old chest open.", inventory]
				else:
					return [True, "The old chest is already wide open.", inventory]
			if(verb == 'close'):
				if(self.closed == False):
					self.closed = True
					return [True, "You push down the lid of the old chest and it closes with a bang.", inventory]
				else:
					return [True, "The old chest is already closed.", inventory]
		elif(noun1):
			if(verb == 'take'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								pickup_text = "You took the %s from the old chest and added it to your inventory." % self.contents[index].name
								inventory.append(self.contents[index])
								self.contents.pop(index)
								return [True, pickup_text, inventory]
							else:
								return [True, "The %s is too heavy to pick up." % self.contents[index].name, inventory]
			if(verb == 'check'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								return [True, self.contents[index].check_text(), inventory]
		return [False, None, inventory]
