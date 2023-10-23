# Component Related Imports
from Calculator import Calculator
from DisplayViewer import DisplayViewer

# Unittest Related Imports
import unittest
from unittest.mock import patch


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.display = DisplayViewer(0)

    def tearDown(self):
        pass

    def test_sum_function_goodCase(self):
        """Given: 2 inputs (10, 20)
            When: calling the sum function
            Then: must return 30
        """
        # Arrange Pre-Conditions
        a = 10
        b = 20
        expected_value = 30
        my_calculator = Calculator(self.display)

        # Act on SUT
        ret_val = my_calculator.sum(a, b)

        # Assert
        self.assertEqual(expected_value, ret_val)

    def test_subtract_function_goodCase(self):
        """Given: 2 inputs (20, 11)
            When: calling the subtract function
            Then: must return 9
        """
        # Arrange Pre-Conditions
        a = 20
        b = 11
        expected_value = 9
        my_calculator = Calculator(self.display)

        # Act on SUT
        retVal = my_calculator.subtract(a, b)

        # Assert
        self.assertEqual(expected_value, retVal)

    @patch('DisplayViewer.DisplayViewer.showValueOnScreen')
    def test_subtract_function_badCase(self, mocked_show_value_on_screen):
        """Given: 2 inputs (20, 11) and a mocked result from showValueOnScreen function
            When: calling the subtract function
            Then: must return the errorCode
        """
        # Arrange Pre-Conditions
        a = 20
        b = 11
        expectedValue = 404
        myCalculator = Calculator(self.display)
        mocked_show_value_on_screen.return_value = 404

        # Act on SUT
        retVal = myCalculator.subtract(a, b)

        # Assert
        self.assertEqual(expectedValue, retVal)


if __name__ == '__main__':
    unittest.main()
