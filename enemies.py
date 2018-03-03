import items

class Enemy:
	name = "Do not create raw enemies!"
	description = "There is no description here because you should not create raw Enemy objects!"
	attack_description = "There is no attack_description here because you should not create raw Enemy objects!"
	
	hp = 0
	damage = 0
	
	loot = []
	
	agro = False	# Used to cause enemies to attack spontaneously.
	
	def __init__(self, direction = None, loot = []):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			self.direction = None
		
		if(len(self.loot) > 0):
			for item in loot:
				self.loot.append(item)
		else:
			self.loot = loot

	def __str__(self):
		return self.name
		
	def check_text(self):
		text = ""
		if(self.direction):
			text = "A %s is blocking your progress to the %s." % (self.name, self.direction)
		text += " " + self.description			
		return text

	def take_damage(self, amount):
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			defeat_text = "The %s is defeated." % self.name
			if(len(self.loot) > 0):
				defeat_text += " It dropped the following items: "
				for item in self.loot:
					defeat_text += "* " + str(item)
			return defeat_text
		else:
			return "The %s took %d damage." % (self.name, amount)
			
	def is_alive(self):
		return self.hp > 0
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class GiantSpider(Enemy):
	name = "Giant Spider"
	description = "It twitches its mandibles at you menacingly."
	hp = 10
	damage = 2


class Ogre(Enemy):
	name = "Ogre"
	description = "It looks angry."
	hp = 30
	damage = 10


class BatColony(Enemy):
	name = "Colony of bats"
	description = "A colony of bats swarms through the air."
	hp = 100
	damage = 4
	
	agro = True


class RockMonster(Enemy):
	name = "Rock Monster"
	description = "A Rock Monster appears from the shadows. An old iron key dangles precariously from a stalagmite on the monster's shoulder."
	hp = 80
	damage = 15
	loot = [items.Iron_Key("An old iron key lies on the ground near the remains of the Rock Monster.")]