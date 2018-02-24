import items

class Player:
	defense = 0
	defense = 0
	force = 0
	inventory = []

	def __init__(self, player_class):

		if(player_class == "guardian"):
			self.damage = 8
			self.defense = 10
			self.force = 4
			self.inventory = [items.Dagger(),\
						items.Crusty_Bread()]

		elif(player_class == "consular"):
			self.damage = 6
			self.defense = 6
			self.force = 10
			self.inventory = [items.Rock(),\
						items.Crusty_Bread()]

		elif(player_class == "sentinel"):
			self.damage = 10
			self.defense = 6
			self.force = 6
			self.inventory = [items.Rock(),\
						items.Dagger()]

		self.gold = 5
		self.hp = 100 + 4*self.defense
		self.x = 2
		self.y = 3

	def print_inventory(self):
		print("Inventory:")
		for item in self.inventory:
			print('* ' + str(item).title())
		print("* %i Gold" % self.gold)
	
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
		
	def consolidate_inventory(self):
		self.move(dx=-1, dy=0)
		
	def handle_input(self, verb, noun1, noun2):
		if(verb == 'check'):
			for item in self.inventory:
				if item.name.lower() == noun1:
					return [True, item.check_text()]
		return [False, ""]
		
	def update_inventory(self):
		gold_indices = []
		gold_total = 0
		for index in range(len(self.inventory)):
			if(isinstance(self.inventory[index], items.Gold)):
				gold_total += self.inventory[index].value
				gold_indices.append(index)
		if(gold_total > 0):
			for index in gold_indices:	
				self.inventory.pop(index)
			self.gold += gold_total
			print("Your wealth increased by %d Gold." % gold_total)
			
