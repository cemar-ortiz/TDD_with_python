
from universe.characters import Rick

class Citadel():
	
	def __init__(self):
		# residents is a private field
		self._residents = []
		self._list_of_ricks = []
		
	def get_all_residents(self):
		resident_list = self._residents
		return resident_list

	def add_residents(self, add_list):
		self._residents.extend(add_list)
		ricks = [resident for resident in add_list if isinstance(resident, Rick)]
		self._list_of_ricks.extend(ricks)
		
	def pickle_turn(self):
			
		for rick in self._list_of_ricks:
			if rick.assigned_morty != None:
				rick.is_pickle = True
	
		
		
