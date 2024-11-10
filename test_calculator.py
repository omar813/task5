# test_calculator.py
import unittest
import yaml
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load the test cases from the YAML file
        with open("test_config.yml", "r") as f:
            cls.test_config = yaml.safe_load(f)

        cls.calculator = Calculator()

    def test_add(self):
        # Loop through each test case for the 'add' function
        for case in self.test_config["test_cases"]["add"]:
            with self.subTest(case=case):
                inputs = case["inputs"]
                expected = case["expected"]
                result = self.calculator.add(*inputs)
                self.assertEqual(result, expected, f"Failed on inputs {inputs}")

if __name__ == "__main__":
    unittest.main()
