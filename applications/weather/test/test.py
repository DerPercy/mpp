import unittest
import os

from weather.lib import Parser
from weather.lib import parseFile

import logging

#logging.basicConfig(level=logging.DEBUG, format='%(message)s')

my_path = os.path.abspath(os.path.dirname(__file__))
file_data = open(my_path+"/demo_api_result.json","r")
test = parseFile(file_data)

class TestStringMethods(unittest.TestCase):
	def test_parsed_timestamp(self): # get time of forecast file
		self.assertEqual(test.uiTime(), '07:42')
		
	def test_parsed_houry(self): # getting hourly forecast values
		self.assertEqual(test.hourly().get(0).uiTemp(), '21 °C')
		self.assertEqual(test.hourly().get(1).uiTemp(), '22 °C')
		
		
		
		
		
#	def test_upper(self):
#		self.assertEqual('foo'.upper(), 'FOO')
#
#	def test_isupper(self):
#		self.assertTrue('FOO'.isupper())
#		self.assertFalse('Foo'.isupper())
#
#	def test_split(self):
#		s = 'hello world'
#		self.assertEqual(s.split(), ['hello', 'world'])
#		# check that s.split fails when the separator is not a string
#		with self.assertRaises(TypeError):
#			s.split(2)

if __name__ == '__main__':
    unittest.main()
