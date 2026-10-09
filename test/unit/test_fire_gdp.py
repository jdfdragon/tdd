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

    def test_funcPresent(self):
        self.assertRaises(TypeError, fire_gdp.get_column_index)

    def test_namePresent(self):
        header_list = ['a', 'b', 'c', 'd']
        r = fire_gdp.get_column_index(header_list, 'b')
        self.assertEqual(r, 1)

    def test_nameAbsent(self):
        header_list = ['a', 'b', 'c', 'd']
        self.assertRaises(TypeError, fire_gdp.get_column_index, 
                          header_list, None)

    def test_headerAbsent(self):
        self.assertRaises(TypeError, fire_gdp.get_column_index,
                          None, 'a')



class TestGetData(unittest.TestCase):

    def test_funcPresent(self):
        self.assertRaises(TypeError, fire_gdp.get_data)

    def test_namePresent(self):
        file = "../test/data/testAgroFood.csv"
        data = fire_gdp.get_data(file)
        rows = len(data)
        columns = len(data[0])
        self.assertEqual([rows, columns], [6, 31])


class TestGetFireGDPYearData(unittest.TestCase):

    def test_funcPresent(self):
        self.assertRaises(TypeError, fire_gdp.get_fire_gdp_year_data)


if __name__ == '__main__':
    unittest.main()
