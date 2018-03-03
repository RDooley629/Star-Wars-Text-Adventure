class Barrier:
	name = None
	passable = False
	state = None	# Used to store the state of doors or hidden passages.
	locked = None	# Used to store the state of locked doors, if applicable.
	
	verbose = False	# Used to determine whether or not include the barrier's description in the room description.

	def __init__(self, direction):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			raise NotImplementedError("Barrier direction is not recognized.")
	
	def description(self):
		raise NotImplementedError("Create a subclass instead!")
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]
		
class wall(Barrier):
	def description(self):
		return "There doesn't seem to be a path to the %s." % self.direction
		
class woodendoor(Barrier):
	name = 'Wooden Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			return "An old wooden door blocks your path to the %s." % self.direction
		else:
			return "An old wooden door lies open before you to the %s." % self.direction
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'wooden door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					self.state = 'open'
					self.passable = True
					return [True, "You tug on the handle, and the wooden door creaks open.", inventory]
				else:
					return [True, "The door is already open.", inventory]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You slam the old wooden door shut.", inventory]
				else:
					return [True, "The door is already closed.", inventory]
			
		return [False, "", inventory]
		
		
class foyerdoor(Barrier):
	name = 'Locked Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	locked = True		# Used to store the state of locked doors, if applicable.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			if(self.locked):
				return "There's a door to the %s. A small red light blinks on the handle. It's probably locked." % self.direction
			else:
				return "A door blocks a passageway to the %s. It's trying to be imposing, but fails. The red light on the handle is no longer lit." % self.direction
		else:
			return "The door to your %s is open. Nice. You see a study through there." % self.direction
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'locked door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					if(self.locked):
						return [True, "You try to open the door, but the handle just shakes. You need to unlock it first.", inventory]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "You open an unlocked door. Impressive. Truly a master of the Jedi way.", inventory]
				else:
					return [True, "The door is already open. I told you that. Can you read? How did you make it this far?", inventory]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You close the door, I guess.", inventory]
				else:
					return [True, "The door is already closed. For your next class, I would recommend Logic 101.", inventory]
			if(verb == 'unlock'):
				if(self.locked):
					if(noun2 == 'red keychip'):
						for index in range(len(inventory)):
							if(inventory[index].name.lower() == 'red keychip'):
								inventory.pop(index)	# Removes the item at this index from the inventory.
								self.locked = False
								return [True, "You insert the red keychip into the padlock and twist. The padlock falls free with a clang. How is there an iron padlock? I have no idea. What just happened? Where did it come from? Where did it go? Is this the home of Cotton-Eye Joe?", inventory]
						return [True, "Seriously? You don't even have the right key. Some people...", inventory]
					elif(noun2 == 'key'):
						return [True, "Be more specific. This door only takes a specific key.", inventory]
					else:
						return [True, "What ITEM do you plan to UNLOCK the DOOR with? DO I NEED TO CAPITALIZE EVERYTHING?", inventory]
				else:
					return [True, "The door is already unlocked. What are you, five?", inventory]
			
		return [False, "", inventory]

class relicdoor(Barrier):
	name = 'Locked Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	locked = True		# Used to store the state of locked doors, if applicable.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			if(self.locked):
				return "An imposing door with a large iron padlock blocks a passageway to the %s." % self.direction
			else:
				return "An imposing door blocks a passageway to the %s. A large iron padlock which once held it shut lies on the ground beside it." % self.direction
		else:
			return "An imposing door lies open before you to the %s." % self.direction
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'locked door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					if(self.locked):
						return [True, "You try to open the door, but the padlock holds it firmly shut. You need to unlock it first.", inventory]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "You heave the once-locked door open.", inventory]
				else:
					return [True, "The door is already open.", inventory]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You push the massive door closed.", inventory]
				else:
					return [True, "The door is already closed.", inventory]
			if(verb == 'unlock'):
				if(self.locked):
					if(noun2 == 'blue keychip'):
						for index in range(len(inventory)):
							if(inventory[index].name.lower() == 'blue keychip'):
								inventory.pop(index)	# Removes the item at this index from the inventory.
								self.locked = False
								return [True, "You swipe the blue keychip. There's a soft chime, and the door unlocks.", inventory]
						return [True, "You don't seem to have the right key for this door. Keep looking!", inventory]
					elif(noun2 == 'key'):
						return [True, "Be more specific. This door only takes a specific key. Unlike some doors, this door has standards.", inventory]
					else:
						return [True, "Okay, unlock the door... but with what? Your bare hands?", inventory]
				else:
					return [True, "The door is already unlocked.", inventory]
			
		return [False, "", inventory]

class bedroomdoor(Barrier):
	name = 'Locked Door'
	state = 'closed'	# Used to store the state of doors or hidden passages.
	locked = True		# Used to store the state of locked doors, if applicable.
	
	verbose = True	# Used to determine whether or not include the barrier's description in the room description.
	
	def description(self):
		if(self.state == 'closed'):
			if(self.locked):
				return "An old door with a small blue lock blocks the way to the %s." % self.direction
			else:
				return "An imposing door blocks a passageway to the %s. Some dust is on the floor. When did that get there?" % self.direction
		else:
			return "A door lies open before you to the %s. Nice." % self.direction
		
	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == 'door' or noun1 == 'locked door'):
			if(verb == 'check'):
				return [True, self.description(), inventory]
			if(verb == 'open'):
				if(self.state == 'closed'):
					if(self.locked):
						return [True, "You try to open the door, but the lock holds it shut. You need to unlock it first.", inventory]
					else:
						self.state = 'open'
						self.passable = True
						return [True, "You push the once-locked door open.", inventory]
				else:
					return [True, "The door is already open. You might need an optomestrist.", inventory]
			if(verb == 'close'):
				if(self.state == 'open'):
					self.state = 'closed'
					self.passable = False
					return [True, "You push the door closed.", inventory]
				else:
					return [True, "You try to close the door, but find that it's already closed! Oh dear! Whatever shall you do?", inventory]
			if(verb == 'unlock'):
				if(self.locked):
					if(noun2 == 'green keychip'):
						for index in range(len(inventory)):
							if(inventory[index].name.lower() == 'green keychip'):
								inventory.pop(index)	# Removes the item at this index from the inventory.
								self.locked = False
								return [True, "You insert the keychip into the lock. You hear a faint click.", inventory]
						return [True, "You don't seem to have the right keychip.", inventory]
					elif(noun2 == 'key'):
						return [True, "Be more specific. This game doesn't have skeleton keys. They're so bony and we don't support eating disorders. Shame on you.", inventory]
					else:
						return [True, "What do you want to unlock that door with?", inventory]
				else:
					return [True, "The door is already unlocked. Oh dear. The scandal.", inventory]
			
		return [False, "", inventory]






