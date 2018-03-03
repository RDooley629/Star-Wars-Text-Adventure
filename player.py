import items

class Player:
	damage = 0
	defense = 0
	force = 0
	inventory = []

	def __init__(self, player_class):

		if(player_class == "guardian"):
			self.damage = 8
			self.defense = 10
			self.force = 4
			self.forcepoints = 4
			self.maxforcepoints = 4
			self.inventory = [items.BlueLightsaber()]
			self.health = self.defense*5
			self.maxhealth = self.defense*5
			self.weapon = items.BlueLightsaber()
			self.x = 6
			self.y = 7

		elif(player_class == "consular"):
			self.damage = 6
			self.defense = 6
			self.force = 10
			self.forcepoints = 10
			self.maxforcepoints = 10
			self.inventory = [items.GreenLightsaber()]
			self.health = self.defense*5
			self.maxhealth = self.defense*5
			self.weapon = items.GreenLightsaber()
			self.x = 6
			self.x = 6
			self.y = 7


		elif(player_class == "sentinel"):
			self.damage = 10
			self.defense = 6
			self.force = 6
			self.forcepoints = 6
			self.maxforcepoints = 6
			self.inventory = [items.YellowLightsaber()]
			self.health = self.defense*5
			self.maxhealth = self.defense*5
			self.weapon = items.YellowLightsaber()
			self.x = 6
			self.y = 7

	def print_inventory(self):
		print("Inventory:")
		best_weapon = None
		equipped_weapon = False
		for item in self.inventory:
			inventory_text = '* ' + str(item).title()
			if(item == self.weapon and not equipped_weapon):
				inventory_text += ' (equipped)'
				equipped_weapon = True
			print(inventory_text)
			best_weapon = self.most_powerful_weapon()
		if(best_weapon):
			print("Your best weapon is your {}.".format(best_weapon))
		else:
			print("You are not carrying any weapons.")
	
	def most_powerful_weapon(self):
		max_damage = 0
		best_weapon = None
		for item in self.inventory:
			try:
				if item.damage > max_damage:
					best_weapon = item
					max_damage = item.damage
			except AttributeError:
				pass
		return best_weapon
		
	def move(self, dx, dy):
		self.x += dx
		self.y += dy

	def move_north(self):
		self.move(dx=0, dy=-1)

	def move_south(self):
		self.move(dx=0, dy=1)

	def move_east(self):
		self.move(dx=1, dy=0)

	def move_west(self):
		self.move(dx=-1, dy=0)
		
	def update_inventory(self):
		has_weapon = False
		for item in self.inventory:
			if(item == self.weapon):
				has_weapon = True
		if not has_weapon:
			self.weapon = None	# Drop the equipped item if it is no longer in inventory.
			
	def heal(self, amount):
		self.health += amount
		if(self.health > self.max_hp):
			self.health = self.max_hp
			return "Your health is fully restored."
		else:
			return "Your health was restored by %d HP." % amount
			
	def take_damage(self, amount):
		self.health -= amount
		if(self.health <= 0):
			self.health = 0
			return "Your health is critical... everything is getting dark."
		else:
			return "You took %d damage." % amount
			
	def is_alive(self):
		if(self.health <= 0):
			return False
		else:
			return True
			
	
	def handle_input(self, verb, noun1, noun2):
		if(verb == 'check'):
			if(noun1 == 'self' or noun1 == 'health' or noun1 == 'hp'):
				return [True, "Your health is currently %d / %d." % (self.health, self.max_hp)]
			for item in self.inventory:
				if item.name.lower() == noun1:
					return [True, item.check_text()]
		elif(verb == 'consume'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, items.Consumable)):
						heal_text = item.consume_description
						heal_text += " " + self.heal(item.healing_value)
						self.inventory.pop(self.inventory.index(item))
						return [True, heal_text]
		elif(verb == 'equip'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, items.Weapon)):
						if(self.weapon != item):
							self.weapon = item
							return [True, item.equip_description]
						else:
							return [True, "You already have your %s equipped." % item.name]
		elif(verb == 'unequip'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					if(isinstance(item, items.Weapon)):
						if(self.weapon == item):
							self.weapon = None
							return [True, "You have unequipped your %s." % item.name]
			return [True, "That does not appear to be equipped right now."]
		return [False, ""]
		

			
