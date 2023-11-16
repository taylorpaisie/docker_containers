import unittest
import subprocess
import sys


class TestVersion(unittest.TestCase):
    def test_rdp(self):
        try:
            result = subprocess.check_output(["classifier", "--version"], stderr=subprocess.STDOUT, text=True)
            version = result.strip()
        except subprocess.CalledProcessError as e:
            version = e.output.strip()

        self.assertEqual(version, "v2.14")

    def test_python(self):
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.assertEqual(version, "3.8")  # Update this with the expected Python version


if __name__ == "__main__":
    unittest.main()