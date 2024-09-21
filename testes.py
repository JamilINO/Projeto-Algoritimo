import unittest
from unittest.mock import *

class TestStringMethods(unittest.TestCase):


    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @patch('builtins.input', lambda _: 'y') # <- value to be returned by input method
    def test_should_be_the_correct_value(self):

        # replace with your class or method to be tested:
        value = input('enter with a value')

        assert value == 'y'

if __name__ == '__main__':
    unittest.main()