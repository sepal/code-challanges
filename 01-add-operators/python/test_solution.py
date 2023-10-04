from solution import addOperators
import unittest


class TestAddOperators(unittest.TestCase):
    def test_positive(self):
        result = addOperators(123, 6)
        exp = ["1*2*3", "1+2+3"]
        self.assertListEqual(result, exp)

    def test_negative(self):
        result = addOperators(3456237490, 9191)
        self.assertListEqual(result, [])


if __name__ == '__main__':
    unittest.main()
