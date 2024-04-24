"""
Sample Test
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """ Test the calc module. """

    def test_add_numbers(self):
        """ Test adding them """
        res = calc.add(5, 6)

        self.assertEqual(res, 11)

    
    def test_subtract_numbers(self):
         """ Test subtracting them """
         res = calc.subtract(6, 5)

         self.assertEqual(res, 1)