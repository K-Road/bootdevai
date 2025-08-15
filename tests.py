import unittest
from functions.run_python import run_python_file
import os

class TestRunPythonFile(unittest.TestCase):
    def setUp(self):
        self.working_directory = os.path.abspath("calculator")

    def test_run_main(self):
        result = run_python_file(self.working_directory, "main.py")
        print("Result output:\n", result)
        self.assertIn("STDOUT", result)

    def test_run_main_with_args(self):
        result = run_python_file(self.working_directory, "main.py", ["3 + 5"])
        print("Result output:\n", result)
        self.assertIn("STDOUT", result)

    def test_run_tests_py(self):
        result = run_python_file(self.working_directory, "tests.py")
        print("Result output:\n", result)
        self.assertTrue("STDOUT" in result or "STDERR" in result)

    def test_run_outside_directory(self):
        result = run_python_file(self.working_directory, "../main.py")
        print("Result output:\n", result)
        self.assertTrue(result.startswith("Error: Cannot execute"))

    def test_run_nonexistent_file(self):
        result = run_python_file(self.working_directory, "nonexistent.py")
        print("Result output:\n", result)
        self.assertTrue(result.startswith("Error: File"))

if __name__ == "__main__":
    unittest.main()
