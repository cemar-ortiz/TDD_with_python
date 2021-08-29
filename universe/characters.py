

class Rick():
	
	# Build a constructor to assign the universe_number
	def __init__(self, universe_number):
		self.universe_number = universe_number
		self.is_pickle = False
		self.assigned_morty = None
	
	def assign_morty(self, morty):
		self.assigned_morty = morty
		morty.assigned_rick = self
		

class Morty():

	# Likewise
	def __init__(self, universe_number):
		self.universe_number = universe_number

