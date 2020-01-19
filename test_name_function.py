import unittest

from name_function import *
class NamesTEstCase(unittest.TestCase):
    """test for name_function.py"""
    def test_first_last_name(self):
        formatted_name = get_formated_name('Janis', 'Joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()