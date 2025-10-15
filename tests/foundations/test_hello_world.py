import unittest
from unittest import TestCase
from contextlib import redirect_stdout
import io

class TestHelloWorld(TestCase):

    def test_hello_world(self):
        captured_output = io.StringIO()

        with open("foundations/src/hello_world.py") as f:
            with redirect_stdout(captured_output):
                exec(f.read())

        self.assertEqual(captured_output.getvalue().strip(), "Hello World!")
