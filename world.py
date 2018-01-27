class Maptile:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")

class Starttile(Maptile):
	def intro_text(self)
		return """
		You find yourself in a cave. Hanging from the ceiling is a
		flickering light. Four paths lay ahead of you, each equally
		frightening. Take your pick.
		"""

class Boringtile(Maptile):
	def intro_text(self):
		return """
		This part of the cave is fairly boring. The walls are simple
		rock, the floor is rough, and your footsteps echo down the
		hallways. Besides that, there's not much to see.
		"""

class Victorytile(Maptile):
	def intro_text(self):
		return """
		At first it seems a trick of your eyes, but a few blinks of
		your eyes get rid of that idea. There's a light ahead, though
		faint. As you draw closer, you realize something important.
		It's sunlight; you're free.

		Victory is yours, champion... but for how long?
		"""

world_map = [
	[None,Victorytile(1,0),None]
	[None,Boringtile(1,1),None]
	[Boringtile(0,2),Starttile(1,2),Boringtile(2,2)]
	[None,Boringtile(1,3),None]
]

def tile_at(x, y):
	if x<0 or y<0:
		return None
	try:
		return world_map[y][x]
	except IndexError:
		return None
