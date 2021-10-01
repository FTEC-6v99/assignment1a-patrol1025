# Create a unit test method to test the calculate_avg function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest

from app.src.utils import calculate_avg

class TestUtils(unittest.TestCase):
    def calc_avg_test(self):
        input=[1,4,5,2]
        expected=4
        actual=calculate_avg(input)
        self.assertEquals(expected, actual)
        self.assertTrue(isinstance(actual, float))

    def test_calc_avg_bad_input(self):
        input=['pat', 'rick', 'ro', 'land']
        self.assertRaises(TypeError, calculate_avg, input)

    def test_calc_avg_empty(self):
        self.assertRaises(Exception, calculate_avg, [])
