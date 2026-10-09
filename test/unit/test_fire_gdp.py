import os
import sys
import unittest
from pathlib import Path

test_dir = Path(__file__).resolve().parent

# Navigate to tdd/src
src_dir = test_dir.parent.parent / "src"

sys.path.insert(0, str(src_dir))

import fire_gdp 


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        self.assertRaises(TypeError, fire_gdp.get_column_index)




if __name__ == '__main__':
    unittest.main()
