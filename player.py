import items

class Player:
	def __init__(self):
		self.inventory = [items.Rock(),
						items.Dagger(),
						items.Crusty_Bread()]
		self.gold = 5
		self.hp = 100
		self.x = 2
		self.y = 3

	def print_inventory(self):
		print("Inventory:")
		for item in self.inventory:
			print('* ' + str(item).title())
			best_weapon = self.most_powerful_weapon()
		print("* %i Gold" % self.gold)
		print("Your best weapon is your {}".format(best_weapon))
	
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
			