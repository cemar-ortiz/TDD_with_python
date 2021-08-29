# From User Story: 'A user is able to add residents to the citadel'

import unittest

from universe.places import Citadel
from universe.characters import Rick, Morty

class CitadelTests(unittest.TestCase):
		
	# Make a test for the add_residents functionality
	def test_add_residents(self):
		citadel = Citadel()
		rick = Rick(137)
		morty = Morty(137)
		citadel.add_residents([rick, morty])
		residents = citadel.get_all_residents()
		self.assertCountEqual(residents, [rick, morty])

	# I dropped the get_all_residents() test mentioned in the rubik's
	# code blogpost because the order of the tests was interferring
	# with the testing. In this case, this is no longer a 'unit'
	# test, but a scenario test. Besides, the test above already
	# tests the get_all_residents() functionality


if __name__ == '__main__':
	unittest.main()
	
	
