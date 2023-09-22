import json
import unittest
import solution


class TestFizzBuzz(unittest.TestCase):
    def test_one_to_hundred(self):
        with open("../expected.json") as file:
            expected = json.load(file)

        output = solution.fizzbuzz(1, 100)

        self.assertListEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
