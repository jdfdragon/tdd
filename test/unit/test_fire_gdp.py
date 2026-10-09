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

    def test_func_present(self):
        self.assertRaises(TypeError, fire_gdp.get_column_index)

    def test_name_present(self):
        header_list = ['a', 'b', 'c', 'd']
        r = fire_gdp.get_column_index(header_list, 'b')
        self.assertEqual(r, 1)


class TestGetData(unittest.TestCase):

    def test_func_present(self):
        self.assertRaises(TypeError, fire_gdp.get_data)

class TestGetFireGDPYearData(unittest.TestCase):

    def test_func_present(self):
        self.assertRaises(TypeError, fire_gdp.get_fire_gdp_year_data)


if __name__ == '__main__':
    unittest.main()
