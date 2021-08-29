import unittest
from unittest import mock


class MockTests (unittest.TestCase):

	def test(self):
		
		# With the objects of Mock class you can mock any function
		# variable, or object
		m = mock.Mock()
		
		# All these tests will return true, for example
		assert isinstance(m.field, mock.Mock)
		assert isinstance(m.field2, mock.Mock)
		assert isinstance(m(), mock.Mock)
		assert m.field is not m.field2 is not m()
		
		
	def test_fields(self):
  		m = mock.Mock()
  		m.rubiks = 'code'
  		self.assertEqual(m.rubiks, 'code')

  		m.configure_mock(tdd='rulez')
  		self.assertEqual(m.tdd, 'rulez')
  		
  		
	def test_functions(self):
		m = mock.Mock()
		# We can mock value returns using the return_value option
		m.get_eleven.return_value = 11
		self.assertEqual(m.get_eleven(), 11)
		
		
	def test_exception(self):
		m = mock.Mock()
		# We can also mock errors using the side_effect option
		m.throw_exception.side_effect = RuntimeError('Oh no!')
		
		try:
			m.throw_exception()
		except RuntimeError:
			assert True
		else:
			assert False
			
			
	def test_multiple_return(self):
		m = mock.Mock()
		m.get_eleven.return_value = 11

		# side_effect also works as a way to return a different
		# value on each call of the function
		m.get_eleven.side_effect = [12, 13, 14]
		self.assertEqual(m.get_eleven(), 12)
		self.assertEqual(m.get_eleven(), 13)
		self.assertEqual(m.get_eleven(), 14)
		
		
	def test_verify_called(self):
		m = mock.Mock()
		m.called_function.return_value = 11
		m.called_function()
		# We can also verify if a function has been called
		# This is a pretty neat feature
		m.called_function.assert_called()


	# This functionality can also be used to check one 
	# or multiple calls
	def test_verify_called_once(self):
		m = mock.Mock()
		m.called_function.return_value = 11
		m.called_function()
		m.called_function.assert_called_once()


	def test_verify_called_multiple(self):
		m = mock.Mock()
		m.called_function.return_value = 11
		m.called_function()
		m.called_function()
		m.called_function()
		self.assertEqual(m.called_function.call_count, 3)


	# To reset interactions
	def test_reset_mock(self):
		m = mock.Mock()
		m.called_function.return_value = 11
		m.called_function()
		m.called_function()
		m.called_function()
		m.called_function.reset_mock();
		self.assertEqual(m.called_function.call_count, 0)
		
		
		
		
		
		
		
		
		
		
		
