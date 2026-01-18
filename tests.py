import unittest
import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self) :
        self.assertEqual(calculator.add(345678, 12343556), 12689234)

    def test_sub(self) :
        self.assertEqual(calculator.sub(150, 100), 50)

    def test_mul(self) :
        self.assertEqual(calculator.mul(1,2), 2)

    def test_div(self) :
        self.assertEqual(calculator.div(1,2), 0.5)

    def test_power(self) :
        self.assertEqual(calculator.power(2,2), 4)

    def test_root(self) :
        self.assertEqual(calculator.square_root(4), 2)


if __name__ == '__main__':
    unittest.main()