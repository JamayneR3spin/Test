import unittest
from Calculator_app import Calculator, Operation
class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_calculate_add(self):
        self.assertEqual(self.calculator.calculate(5, 3, Operation.ADD), 8)
        self.assertEqual(self.calculator.calculate(-1, 1, Operation.ADD), 0)
        self.assertEqual(self.calculator.calculate(0, 0, Operation.ADD), 0)
        self.assertEqual(self.calculator.calculate(10.5, 2.5, Operation.ADD), 13.0)
