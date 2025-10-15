import unittest
from unittest import TestCase
from unittest.mock import patch
import io
import sys

class TestMain(TestCase):
    
    def test_output(self):
        captured_inputs = []
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        def mocked_input(prompt):
            captured_inputs.append(prompt)
            if prompt == "Enter your name: ":
                return "Ezekiel"
            if prompt == "Enter your age: ":
                return "37"
              
        with patch("builtins.input", side_effect=mocked_input):
            with open("source/main.py") as f:
                code = f.read()
                exec(code)
                self.assertEqual(captured_inputs, ["Enter your name: ", "Enter your age: "])
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        self.assertEqual("Hello Ezekiel, you will be 38 years next year\n", output)

if __name__ == "__main__":
	unittest.main()
