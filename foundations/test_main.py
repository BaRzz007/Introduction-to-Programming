import unittest
from unittest import TestCase
from unittest.mock import patch
import io
import sys
#from contextlib import redirect_stdout

class TestMain(TestCase):
    
    def test_output(self):
        captured_inputs = []
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        def mocked_input(prompt):
            captured_inputs.append(prompt)

            if prompt == "Enter your name\n":
                return "Ezekiel"
            if prompt == "Enter your age\n":
                return "37"
        with patch("builtins.input", side_effect=mocked_input):
        
            with open("source/main.py") as f:
            
                code = f.read()

                exec(code) #{'__name__': '__main__'})
                self.assertEqual(captured_inputs, ["Enter your name\n", "Enter your age\n"])

        sys.stdout = sys.__stdout__

        output = captured_output.getvalue()



        # self.assertIn("Enter your name", output)
        # self.assertIn("Enter your age",  output)
        self.assertEqual("Hello Ezekiel, you will be 38 years next year\n", output)



if __name__ == "__main__":
	unittest.main()
