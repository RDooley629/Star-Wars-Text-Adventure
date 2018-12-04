class Barrier:
	name = None
	passable = False
	state = None		# Used to store the state of doors or hidden passages.
	locked = None		# Used to store the state of locked doors, if applicable.
	
	verbose = False	# Used to determine whether or not include the barrier's description in the room description.

	def __init__(self, direction):
		if direction == 'n':
			self.direction = 'north'
		elif direction == 's':
			self.direction = 'south'
		elif direction == 'e':
			self.direction = 'east'
		elif direction == 'w':
			self.direction = 'west'
		else:
			raise NotImplementedError("Barrier direction is not recognized.")
	
	def description(self):
		raise NotImplementedError("Create a subclass instead!")
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class Wall(Barrier):
	def description(self):
		return "There doesn't seem to be a path to the %s." % self.direction


class Door(Barrier):
	name = 'door'
	state = 'open'		# Used to store the state of doors or hidden passages.
	locked = False
	passable = True

	verbose = True		# Used to determine whether or not include the barrier's description in the room description.

	def description(self):
		if self.state == 'closed':
			return "The heavy door blocks your way to the %s." % self.direction
		else:
			return "The door hangs open. Through it, you can see the %s exit." % self.direction

	def handle_input(self, verb, noun1, noun2, inventory):
		if (noun1 == 'door') or (noun1 == 'locked door'):
			if verb == 'check':
				return [True, self.description(), inventory]
			elif verb == 'open':
				if self.state == 'closed':
					if self.locked:
						return [True, "You try to open the door, but the handle just shakes. You need to unlock it first.", inventory]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "You open an unlocked door. Impressive. Truly, the TSA is fearsome.", inventory]
				else:
					return [True, "The door is already open. I told you that. Can you read? How did you make it this far?", inventory]
			elif verb == 'close':
				if self.state == 'open':
					self.state = 'closed'
					self.passable = False
					return [True, "You close the door, I guess.", inventory]
				else:
					return [True, "I mean, you can try. I don't think you can close it any further, though.", inventory]
			elif verb == 'unlock':
				if self.locked and (self.state == 'closed'):
					if noun2 == 'keychip':
						for index in range(len(inventory)):
							if inventory[index].name.lower() == 'keychip':
								self.locked = False
								return [True, "Nice try, but it's already unlocked.", inventory]
						return [True, "Wait, what happened to your keychip?", inventory]
					elif noun2 == 'key':
						return [True, "I mean, it's open.", inventory]
					else:
						return [True, "That really isn't necessary.", inventory]
				elif self.state == 'open':
					return [True, "You can't unlock an already open door. That's not how that works.", inventory]

				else:
					return [True, "You just walked through here. It's unlocked.", inventory]
			elif verb == 'lock':
				return [True, "According to TSA regulations, this room can't be locked with people inside. Nice try, though!", inventory]

		return [False, "", inventory]


class Sliding(Barrier):
	name = 'sliding door'
	state = 'closed'  # Used to store the state of doors or hidden passages.

	verbose = True  # Used to determine whether or not include the barrier's description in the room description.

	def description(self):
		if self.state == 'closed':
			return "A closed, unpowered sliding door lies to the %s, blocking the way to the parking lot." % self.direction
		else:
			return "The 'glass' door to the %s has been forced open." % self.direction

	def handle_input(self, verb, noun1, noun2, inventory):
		if (noun1 == 'door') or (noun1 == 'sliding door'):
			if verb == 'check':
				return [True, self.description(), inventory]
			if verb == 'open':
				if self.state == 'closed':
					self.state = 'open'
					self.passable = True
					return [True, "You give it a shove. Slowly, it gives way.", inventory]
				else:
					return [True, "The door is already open.", inventory]
			if verb == 'close':
				if self.state == 'open':
					self.state = 'closed'
					self.passable = False
					return [True, "You shove the sliding door shut.", inventory]
				else:
					return [True, "The door is already closed.", inventory]

		return [False, "", inventory]


class lockeddoor(Barrier):
	name = 'Locked Door'
	state = 'closed'		# Used to store the state of doors or hidden passages.
	locked = True			# Used to store the state of locked doors, if applicable.
	
	verbose = True		# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if self.state == 'closed':
			if self.locked:
				return "There's a door to the %s. A small red light blinks on the handle. It's probably locked." % self.direction
			else:
				return "A door lies to the %s. It tries to be imposing, but fails. The red light is no longer lit." % self.direction
		else:
			return "The door to your %s is open. Nice. You see the contraband room through there." % self.direction
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if (noun1 == 'door') or (noun1 == 'locked door'):
			if verb == 'check':
				return [True, self.description(), inventory]
			elif verb == 'open':
				if self.state == 'closed':
					if self.locked:
						return [True, "You try to open the door, but the handle just shakes. You need to unlock it first.", inventory]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "You open an unlocked door. Impressive. Truly, the TSA is fearsome.", inventory]
				else:
					return [True, "The door is already open. I told you that. Can you read? How did you make it this far?", inventory]
			elif verb == 'close':
				if self.state == 'open':
					self.state = 'closed'
					self.passable = False
					return [True, "You close the door, I guess.", inventory]
				else:
					return [True, "The door is already closed. For your next class, I would recommend Logic 101.", inventory]
			elif verb == 'unlock':
				if self.locked and (self.state == 'closed'):
					if noun2 == 'keychip':
						for index in range(len(inventory)):
							if inventory[index].name.lower() == 'keychip':
								self.locked = False
								return [True, "You slide the keychip through the reader. A soft chime sounds. You've unlocked a door.", inventory]
						return [True, "Seriously? You don't even have the keychip. Some people...", inventory]
					elif noun2 == 'key':
						return [True, "You pat your pockets for your house key, only to realize you need the keychip for this door.", inventory]
					else:
						return [True, "What ITEM do you plan to UNLOCK the DOOR WITH", inventory]
				elif self.state == 'open':
					return [True, "You can't unlock an open door. That's not how that works.", inventory]

				else:
					self.locked = True
					return [True, """You go to swipe open the door, only to realize that it was already unlocked. \
							It's now locked again. Great going.""", inventory]
			elif verb == 'lock':
				if self.locked and (self.state == 'closed'):
					if noun2 == 'keychip':
						for index in range(len(inventory)):
							if  inventory[index].name.lower() == 'keychip':
								self.locked = False
								return [True, "Sliding the keychip, you lock the door. A small red light begins to glow", inventory]
						return [True, "You don't have a key tho", inventory]
					elif noun2 == 'key':
						return [True, "Key or keychip? The bureaucracy cares.", inventory]
					else:
						return [True, "Okay, but what with?", inventory]
				elif self.state == 'open':
					return [True, "... The door is open. You'd need to close it first.", inventory]
				else:
					self.locked = False
					return [True, "You go to lock the door, only to realize that it was already locked. It's now unlocked.", inventory]
			
		return [False, "", inventory]






