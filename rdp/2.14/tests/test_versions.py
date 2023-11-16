import unittest
import subprocess
import sys
import re


class TestVersion(unittest.TestCase):
    def test_rdp(self):
        try:
            version = self.get_classifier_version()
        except subprocess.CalledProcessError as e:
            version = e.output.strip()

        if version is None:
            self.fail("Failed to retrieve the classifier version.")
        else:
            self.assertEqual(version, "v2.14")

    def get_classifier_version(self):
        try:
            result = subprocess.check_output(["classifier.jar", "version"], stderr=subprocess.STDOUT, text=True)
            version_match = re.search(r"v(\S+)", result)
            return version_match.group(1) if version_match else None
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e.cmd}")
            print(f"Output:\n{e.output.strip()}")
            return None

    def test_python(self):
        version = f"{sys.version_info.major}.{sys.version_info.minor}"
        self.assertEqual(version, "3.8")  # Update this with the expected Python version


if __name__ == "__main__":
    unittest.main()
