
class Citadel():
	
	def __init__(self, residents=[]):
		# residents is a private field
		self._residents = residents
		
	def get_all_residents(self):
		resident_list = self._residents
		return resident_list
