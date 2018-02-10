class Weapon:
	def __init__(self):
		raise NotImplementedError("Do not create raw Weapon objects.")

	def __str__(self):
		return self.name

class 3Saber(Weapon):
	def __init__(self):
		self.name = "Lightsaber"
		self.description = "Your lightsaber, ready to use."
		self.damage = 6

class 4Saber(Weapon):
	def __init__(self):
		self.name = "Lightsaber"
		self.description = "Your lightsaber, ready to use."
		self.damage = 8

class 5Saber(Weapon):
	def __init__(self):
		self.name = "Lightsaber"
		self.description = "Your lightsaber, ready to use."
		self.damage = 10

class Rock(Weapon):
	def __init__(self):
		self.name = "Rock"
		self.description = "A fist-sized rock, suitable for bludgeoning."
		self.damage = 5

class Dagger(Weapon):
	def __init__(self):
		self.name = "Dagger"
		self.description = "A small dagger, slightly rusty." \
				   "A bit more dangerous than a rock."
		self.damage = 10

class RustySword(Weapon):
	def __init__(self):
		self.name = "Rusty Sword"
		self.description = "This sword is showing its age, " \
				   "but still has some fight in it."
		self.damage = 20
