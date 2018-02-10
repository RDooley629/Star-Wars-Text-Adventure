class enemy:
	def __init__(self,x,y,aim,attack,hp,defense):
		self.x = x
		self.y = y
		self.aim = aim
		self.attack = attack
		self.hp = hp
		self.defense = defense

class stormtrooper(enemy):
	def __init__(self,x,y):
		super().__init__(x,y,45,8,7,1)

class officer(enemy):
	def __init__(self,x,y):
		super().__init__(x,y,85,10,15,2)
