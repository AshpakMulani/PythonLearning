
###########################################################################################
##############################    Pylint    ###############################################
# pip install pylint
# Pylint : It is a code linter which analyzes python code and provide feedback and quality scrore for our code
# It validate against PEP8 standards and help us witting better code. It validate examples like
    #Missing DOCSTRINGS for function and class
    #class name is invalid if not used camelcase for naming
    #constant name should be in capitals
    # unused veriables
    #tabs and spaces are not used properly

# use >>> pylint <path of python file to evaluate>

###########################################################################################


###########################################################################################
##############################    Unittest    #############################################
# This helps developers or QA testers to write test cases which can be run on functions
# from python script and validate if it is returning expected results
###########################################################################################

import unittest   # this library help us to create validaiton functions

def function_for_testing(text):
    return text.capitalize()

def function_for_testing1(text):
    return text.title()

# Consider here 'Function_for_testing()' is present in some other script which we want to test.
# we are witting it in same script to avoid multiple scripts.


class testing(unittest.TestCase):   # TestCase is a class in unittest library which help us to test particular
      def test_func(self):          # response to given input. There are lots of other classes for different
           test = 'ashpak mulani'          # functions in unittest library
           result = function_for_testing(test)
           self.assertEqual(result, 'Ashpak Mulani')  # Here we want this line to check if function return results
                                                      # are equal to 'Ashpak Mulani' when give input as 'ashpak mulani'
      def test_func1(self):
          test='ashpak mulani'
          result = function_for_testing1(test)
          self.assertEqual(result, 'Ashpak Mulani')


if __name__ == '__main__':
    unittest.main()   # this call is required to start unittest operation, which will execute our checks

# This will return results as failed for one test test_func because function_for_testing is using capitalize
#  method which only make first letter of give string capital and we need every first letter of every word in
# string as capital. This is what we are checking in assertEqual method.
# Second result will be success because .index returns exactly what we want. Which will return
# ran 2 tests are failed test is one with details of failed test.
# So if we use unittest.main() cal it will automatically run all methods from class which are inheriting
# from unittest class.<required method>
# this way we can define multiple test cases in any class and use them against code what we need to test
# using unit test. There are lots of different checks like assertEqual in unittest library.



















