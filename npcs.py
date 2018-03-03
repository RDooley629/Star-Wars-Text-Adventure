import items

class NPC:
	name = "Do not create raw NPCs!"
	description = "There is no description here because you should not create raw NPC objects!"
	
	goods = []	# Stuff an NPC is carrying.
	quantities = []	# Quantities of that stuff.
	
	first_encounter = True			# Used to do something different on first encounter.
	
	def __str__(self):
		return self.name
		
	def check_text(self):
		if(self.first_encounter):
			text = self.first_time()
			return text
		else:
			return self.description

	def talk(self):		# Add to this method if you want to be able to talk to your NPC.
		return "The %s doesn't seem to have anything to say." % self.name		

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		return self.description
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class OldMan(NPC):
	name = "Old Man"
	goods = [items.Dagger(), items.Red_Potion(value = 50), items.Crusty_Bread(value = 5)]
	quantities = [1, -1, 2]		# Set quantity to -1 if you want it to be infinite.
	
	description = "An old man in a red robe is standing in the middle of the room."
	
	def talk(self):		# Add to this method if you want to be able to talk to your NPC.
		print("The old man says: I can sell you an item or two, if you are interested:")
		for item in self.goods:
			if item.value > 0:
				if(self.quantities[self.goods.index(item)] > 0):
					quantity = "quantity = %d" % self.quantities[self.goods.index(item)]
				else:
					quantity = "quantity = unlimited"
				print("* " + item.name.title() + " (" + str(item.value) + " gold, " + quantity + ")")
		return ""
		
	def give(self, item, inventory):
		for good in self.goods:
			if(good == item):
				inventory.append(good)
				if(self.quantities[self.goods.index(good)] > 0):
					self.quantities[self.goods.index(good)] -= 1
		for index in reversed(range(len(self.quantities))):	# Get rid of items with zero quantity.
			if(self.quantities[index] == 0):
				self.quantities.pop(index)
				self.goods.pop(index)
		return inventory

	def first_time(self):		# Used to have your NPC do something different the first time you see them.
		self.first_encounter = False
		text = self.description
		text += " As he holds out a dagger, he says: 'It is dangerous to go alone... take this.'"
		return text
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'old man' or noun1 == 'man'):
			if(verb == 'check'):
				return [True, self.check_text(), inventory]
			elif(verb == 'talk'):
				text = self.talk()
				return [True, text, inventory]
		elif(verb == 'take'):
			for good in self.goods:
				if(good.name.lower() == noun1):
					if(good.value == 0):
						inventory = self.give(good, inventory)
						return [True, "The old man gave you the %s." % good.name, inventory]
					else:
						return [True, "'Hey, what are you trying to pull? If you want that, the cost is %d gold.'" % good.value, inventory]
		return [False, "", inventory]