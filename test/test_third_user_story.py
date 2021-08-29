# From User Story: 'A user is able to turn all Ricks with assigned Mortys to pickles'

# This is a custom implementation I did before checking the blogpost's solution, its very different from what the author of the post did
# But still, it works to test the functionality and it was good practice! I encourage you to build your own tests and solutions too.

import unittest

from universe.characters import Rick, Morty
from universe.places import Citadel

class PickleTests(unittest.TestCase):

	def test_turn_into_pickles(self):
		rick_a = Rick(137)
		morty_a = Morty(137)
		
		rick_b = Rick(121)
		# no morty for you!
		
		citadel = Citadel()
		citadel.add_residents([rick_a, rick_b, morty_a])
		
		rick_a.assign_morty(morty_a)
		
		citadel.pickle_turn()
		
		self.assertTrue(rick_a.is_pickle)
		self.assertFalse(rick_b.is_pickle)
		
