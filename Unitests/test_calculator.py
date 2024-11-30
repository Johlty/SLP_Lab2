import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Functions.operations import add, subtract, multiply, divide, power, square_root, modulo

class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        print("\nПочаток тесту...")

    def tearDown(self):
        if self._outcome.success:
            print("Тест пройдено успішно")
        else:
            print("Тест не пройдено")

    def test_addition(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-10, -5), -15)
        self.assertEqual(add(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(5, 10), -5)
        self.assertEqual(subtract(10, 10), 0)

    def test_multiplication(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(5, 0), 0)

    def test_division(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-10, 5), -2)
        self.assertEqual(divide(10, 1), 10)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_square_root_of_negative(self):
        with self.assertRaises(ValueError):
            square_root(-4)

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        with self.assertRaises(ZeroDivisionError):
            modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
