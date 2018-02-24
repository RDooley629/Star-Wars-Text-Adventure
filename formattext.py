from terminalsize import get_terminal_size					# Allows us to determine terminal window size on any OS.
															# Adapted for Python 3.x from https://gist.github.com/jtriley/1108174

import textwrap	# Gives us tools for formatting text in a much prettier fashion.


wrap_width = 0								# We will use this so that we can wrap text.


# These functions exist only to help make the text print nicer in the terminal.		
def get_width():
	dimensions = get_terminal_size()
	global wrap_width 
	wrap_width = dimensions[0] - 3				# Get the width of the user's window so we can wrap text.
	return dimensions
    
	
def clear_screen():
	terminal = get_width()
   
	for i in range(terminal[1]):
		print("")									# There are fancier ways to clear a screen, but this aligns our text where we want it at the bottom of the window.

		
def print_wrap(text):
	get_width()
	text = " ".join(text.split())				# Removes leading tabs from multiline strings.
	print(textwrap.fill(text, wrap_width, replace_whitespace=True))
	
def print_center(text):
	get_width()
	text = " ".join(text.split())				# Removes leading tabs from multiline strings.
	if(len(text) < wrap_width):
		for i in range(0,wrap_width-len(text),2):
			text = " " + text
		print(text)
	else:
		print(textwrap.fill(text, wrap_width, replace_whitespace=True))	
 
if __name__ == "__main__":
	sizex, sizey = get_terminal_size()
	print('width =' + str(sizex) + ' height =' +  str(sizey))