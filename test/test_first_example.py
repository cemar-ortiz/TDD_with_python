# Comes already with any python installation
import unittest


# Create the class 'FirstTestClass'
# Inherits TestCase from the unittest module
# Contains test methods (or cases) which will be registered
# in the unittest module and we will be able to run later
class FirstTestClass(unittest.TestCase):
	
	# Verifies that the call of the .upper() function
	# returns the same string with all caps
	def test_upper(self):
		self.assertEqual('rubiks code'.upper(), 'RUBIKS CODE')


# Python entry point
if __name__ == '__main__':
	# This will run all registered tests
	unittest.main()
	

