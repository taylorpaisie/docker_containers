import unittest
import subprocess
import sys
import re
import platform


class TestVersion(unittest.TestCase):
    def test_rdp(self):
        try:
            version = self.get_classifier_version()
        except subprocess.CalledProcessError as e:
            version = e.output.strip()

        self.assertEqual(version, "v2.14")

    def get_classifier_version(self):
        if platform.system() == "Windows":
            command = "wmic datafile where name='C:\\\\Path\\\\To\\\\classifier.exe' get Version /value"
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True)
            # Extract version information from the result using regex or string manipulation
            version_match = re.search(r"Version=(\S+)", result)
            return version_match.group(1) if version_match else None
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            command = "file /path/to/classifier | awk '{print $5}'"
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
            # Extract version information from the result using regex or string manipulation
            version_match = re.search(r"v(\S+)", result)
            return version_match.group(1) if version_match else None
        else:
            raise NotImplementedError(f"Unsupported platform: {platform.system()}")

    def test_python(self):
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.assertEqual(version, "3.8")  # Update this with the expected Python version


if __name__ == "__main__":
    unittest.main()
