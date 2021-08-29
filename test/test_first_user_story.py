# From User Story: 'A user is able to assign Ricks and Mortys a universe number'


import unittest
# from characters module in the universe package, import Rick class
from universe.characters import Rick, Morty


class RickTests(unittest.TestCase):	

	def test_universe_assign(self):
		rick = Rick(137)
		self.assertEqual(rick.universe_number, 137)


class MortyTests(unittest.TestCase):
	
	def test_universe_assign(self):
		morty = Morty(137)
		self.assertEqual(morty.universe_number, 137)

	
if __name__ == '__main__':
	unittest.main()
