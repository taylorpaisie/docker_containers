import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_rdp(self):
        command = "classifier --version 2>&1 | awk '{print $4}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, "v2.14\n")

    def test_python(self):
        command = "python --version 3>&1 | awk '{print $2}'"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, "3\n")


if __name__ == "__main__":
    unittest.main()