from main import multiply_3_numbers
import unittest


class TestMultiplication(unittest.TestCase):

    def test_1(self):
        """Test three positive integers."""
        num1, num2, num3 = 10, 11, 50
        result = multiply_3_numbers(num1, num2, num3)
        self.assertEqual(result, 5500)

    def test_2(self):
        """Test three negative integers"""
        num1, num2, num3 = -10, -11, -50
        result = multiply_3_numbers(num1, num2, num3)
        self.assertEqual(result, -5500)

    def test_3(self):
        """Test mixed positive and negative integers"""
        num1, num2, num3 = 10, 11, -50
        result = multiply_3_numbers(num1, num2, num3)
        self.assertEqual(result, -5500)

    def test_4(self):
        """Test positive float integers"""
        num1, num2, num3 = 10.5, 11.3, 50.1
        result = multiply_3_numbers(num1, num2, num3)
        self.assertAlmostEqual(result, 5944.365, 3)
