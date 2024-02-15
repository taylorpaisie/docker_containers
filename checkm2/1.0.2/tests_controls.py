import unittest
import subprocess
from subprocess import PIPE


class TestControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        command = "bash /tests/scripts/run_controls.sh"
        subprocess.run(command, shell=True, stdout=PIPE)


    def test_checkm2(self):
        with open("checkm2_checksum.txt") as f:
            checkm2_checksum = f.readlines()[0].split(" ")[0]
        self.assertEqual(
            checkm2_checksum,
            "a38342a9ba63946ffb4324c7858f5cc43b873673cb08080437f7500dda351f65",
        )


if __name__ == "__main__":
    unittest.main()