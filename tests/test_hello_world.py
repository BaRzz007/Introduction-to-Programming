import unittest
import io
from contextlib import redirect_stdout


class TestHelloWorld(unittest.TestCase):

  def test_hello_world(self):
    captured_output = io.StringIO()
    with open("foundations/hello_world.py") as f:
      with redirect_stdout(captured_output):
        exec(f.read())
    self.assertEqual(captured_output.getvalue().strip(), "Hello World!")

if __name__ == "__main__":
  unittest.main()
