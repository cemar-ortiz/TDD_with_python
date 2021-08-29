import unittest

from helloworld.get_greetings import get_greetings

class HelloWorldTests(unittest.TestCase):
	
	def test_get_helloworld(self):
		self.assertEqual(get_greetings(), 'Hello World!')
		

if __name__ == '__main__':
	unittest.main()
