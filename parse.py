import string				# Used to strip user inputs of punctuation.

game_commands = {'help': ['help'], 'exit': ['exit', 'quit'], 'debug': ['debug']}

verbs = {'go': ['go', 'go to', 'walk', 'head', 'move'], \
	'take': ['take', 'pick up', 'grab', 'get'], \
	'give': ['give', 'hand'], \
	'drop': ['drop', 'put down', 'throw away'], \
	'open': ['open'], \
	'close': ['close', 'shut', 'slam'], \
	'push': ['push', 'shove'], \
	'pull': ['pull', 'tug'], \
	'equip': ['equip', 'put on', 'wear'], \
	'unequip': ['unequip', 'take off', 'remove'], \
	'use': ['use', 'apply'], \
	'consume': ['consume', 'eat', 'drink'], \
	'unlock': ['unlock'], \
	'lock': ['lock'], \
	'check': ['check', 'look at', 'look in', 'look', 'examine', 'inspect'], \
	'attack': ['attack', 'fight', 'kill']}
	
implied_verbs = {'go': {'north': ['north', 'n'], 'south': ['south', 's'], 'east': ['east', 'e'], 'west': ['west', 'w']}, 'check': {'inventory': ['inventory', 'i']}}
	
prepositions = ["with", "to", "on", "from", "at"]

articles = ["a", "an", "the"]


	
def identify_verbs(text):
	found_verb = False
			
	if(len(text) > 0):	
		for character in string.punctuation:
			text = text.replace(character, " ")		# Strip away all punctuation.	
		for verb in verbs.keys():							# This loop replaces any synonym that appears at the beginning of the user's input with their generic verb equivalent.
			for synonym in verbs[verb]:						# e.g. "look at door" becomes "check door".
				if text.startswith(synonym):
					text = text[len(synonym):]				# Strip the synonym from the beginning of the user's input.
					text = verb + text						# Put the generic verb equivalent at the beginning of the string.
					found_verb = True						# Let the code later on know that we found a matching verb.	
					
		if(not found_verb):
			for command in game_commands.keys():
				for synonym in game_commands[command]:
					if text.startswith(synonym):
						text = text[len(synonym):]			# Strip the synonym from the beginning of the user's input.
						text = command + text				# Put the command equivalent at the beginning of the string.
						found_verb = True					# Act as though we found a verb, even though commands may not be verbs.
					
	return [found_verb, text]
	
	
	
def strip_articles(text):
	
	if(len(text) > 0):
		text = text.split(" ")								# Split the text up into a list of words.
		
		for index in range(len(text)):
			for article in articles:
				if(text[index] == article):
					text[index] = ""						# Empty out any articles (e.g. "a" or "the").	
		text = list(filter(None, text))						# Get rid of any empty strings in the input text.	
	
	text = " ".join(text)											# This is essentially the oppostite of the split(" ") method - it puts the sentence back together.
	return text
	
	
	
def parse_command(text, found_verb):					
	if(len(text) > 0):
		text = text.split(" ")										# Split the text up into a list of words.
		
		if(len(text) == 1):										# If command is only one word long, we might have an implied verb or single word command.
				
			for verb in implied_verbs.keys():					# This set of loops replaces any listed single word command synonyms with their generic command equivalent and adds their implied verb.
				for command in implied_verbs[verb].keys():		# e.g. ["i"] becomes ["check", "inventory"]
					for synonym in implied_verbs[verb][command]:
						if text[0] == synonym:
							text.insert(0, verb)
							text[1] = command
							return text
			if(found_verb):
				return text
			else:
				return None											# Return empty-handed if no matching commands were found.
				
						
		elif(len(text) == 2):
			if not found_verb:
				text[0] = None									# Get rid of the verb if we do not recognize it.
			return text											# Return what's left of the user's input. If a verb was found, this will return input in the form [VERB, NOUN]. 
																# If no verb was found, this will return [None, NOUN]
		
		elif(len(text) > 2):
			if not found_verb:
				text[0] = None
				
			for preposition in prepositions:
				if (text[1] == preposition):
					return [text[0], None]				# Commands with a preposition following a verb are invalid.
					
			index = 2
			while(index < len(text)):
				found_preposition = False
				for preposition in prepositions:
					if (text[index] == preposition):
						found_preposition = True
				if(found_preposition):
					text.pop(index)
					index += 1
				else:
					text[index - 1] += " " + text[index]
					text.pop(index)
			return text
			
		else:													# Return empty handed if there is no user input.					
			return None

def pad_command(input):
	for i in range(3):
		try:
			input[i]
			
		except IndexError:		# If we have reached beyond the boundaries of our list.
			input.append(None)	# Add another None object to the end of the list.
			
		except:	# If the input is not a list (i.e. if the input is None).
			input = [None]		# Make input a list.
	return input
			
def get_command():
	text = input('>> ').lower()
	
	[found_verb, user_input] = identify_verbs(text)
	
	user_input = strip_articles(user_input)
	
	user_input = parse_command(user_input, found_verb)
	
	user_input = pad_command(user_input)
	
	return [text, user_input]