# Use unittest library to create a unit test method to test the calculate_avg_grade function created in the gradecalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest


from app.src.Student import Student
from app.src.gradecalc import calculate_avg_grade

class test_gradecalc(unittest):

    def test_grade(self): #check to make sure the normal input works
        input=[Student('s1',20,1824,90.5), Student('s2',21,1823,80.0), Student('s1',20,1824,70.0)]
        actual=calculate_avg_grade(input)
        expected={1824: 80.25, 1823: 80.0 }
        self.assertEqual(expected, actual)
        self.assertTrue(isinstance(actual, float))


    def test_gradecalc_bad_input(self):
        input=[Student('s1',"t","pat",90.5), Student('s2',"d","kk",80.0), Student('s1',"r","dk",70.0)]
        self.assertRaises(TypeError, calculate_avg_grade, input)

    def test_gradecalc_empty(self):
        input={}
        actual=calculate_avg_grade(input)
        expected={}
        self.assertEqual(expected, actual)
        self.assertTrue(actual=={})

