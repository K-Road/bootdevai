import unittest
import os
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_get_files_info(self):
        working_directory = os.path.abspath("calculator")
        result = get_files_info(working_directory, ".")
        expected_lines = [
            "- main.py: file_size=575 bytes, is_dir=False",
            "- tests.py: file_size=1342 bytes, is_dir=False",
            "- pkg: file_size=0 bytes, is_dir=True"
        ]
        for line in expected_lines:
            self.assertIn(line, result)
        print("Result output:\n", result)
    
    def test_get_files_info_pkg(self):
        working_directory = os.path.abspath("calculator")
        result = get_files_info(working_directory, "pkg")
        expected_lines = [
            "- calculator.py: file_size=1737 bytes, is_dir=False",
            "- render.py: file_size=766 bytes, is_dir=False"
        ]
        for line in expected_lines:
            self.assertIn(line, result)
        print("Result output:\n", result)

    def test_get_files_info_bin(self):
        working_directory = os.path.abspath("calculator")
        result = get_files_info(working_directory, "/bin")
        expected_lines = [
           'Error: Cannot list "/bin" as it is outside the permitted working directory'
        ]
        for line in expected_lines:
            self.assertIn(line, result)
        print("Result output:\n", result)

    def test_get_files_info_(self):
        working_directory = os.path.abspath("calculator")
        result = get_files_info(working_directory, "../")
        expected_lines = [
            'Error: Cannot list "../" as it is outside the permitted working directory'
        ]
        for line in expected_lines:
            self.assertIn(line, result)
        print("Result output:\n", result)




if __name__ == "__main__":
    unittest.main()