import unittest
import subprocess


class TestVersion(unittest.TestCase):
    def test_rdp(self):
        command = "classifier --version"
        process = subprocess.Popen(
            command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = process.communicate()
        self.assertEqual(out, "RDP version 2.14")


if __name__ == "__main__":
    unittest.main()