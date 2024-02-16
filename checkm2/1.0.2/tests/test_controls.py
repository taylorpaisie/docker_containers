import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)


    def test_checkm2_wgs(self):
        with open("burk_wgs_checksum.txt") as f:
            checkm2_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            checkm2_checksum,
            "2811f35e88827c3f53562d231a0dd99e7c6542d942acad9ea2ab1f8203dc3d23",
        )

    def test_checkm2_16S(self):
        with open("burk_16S_checksum.txt") as f:
            checkm2_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            checkm2_checksum,
            "6620483f1d713575c914058f9ec1483ea5fe38414811fc46293ccc3659884d15",
        )


if __name__ == "__main__":
    unittest.main()