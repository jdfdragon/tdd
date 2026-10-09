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
        file = Path(__file__).resolve().parent.parent / "data" / "testAgroFood.csv"

        data = fire_gdp.get_data(file)

        rows = len(data)
        columns = len(data[0])
        self.assertEqual([rows, columns], [6, 31])

    def test_namePresent2(self):
        file = Path(__file__).resolve().parent.parent / "data" / "testIMF.csv"
        
        data = fire_gdp.get_data(file)

        rows = len(data)
        columns = len(data[0])
        self.assertEqual([rows, columns], [2, 74])

    def test_query(self):
        file = Path(__file__).resolve().parent.parent / "data" / "testAgroFood.csv"
        
        data = fire_gdp.get_data(file, 0, "Afghanistan")

        rows = len(data)
        columns = len(data[0])
        self.assertEqual([rows, columns], [3, 31])

    def test_noColumn(self):
        file = Path(__file__).resolve().parent.parent / "data" / "testAgroFood.csv"
        self.assertRaises(ValueError, fire_gdp.get_data, file, None, "Afghanistan")

    def test_noValue(self):
        file = Path(__file__).resolve().parent.parent / "data" / "testAgroFood.csv"
        self.assertRaises(ValueError, fire_gdp.get_data, file, 0)

    def test_header(self):
        file = Path(__file__).resolve().parent.parent / "data" / "testAgroFood.csv"

        data = fire_gdp.get_data(file, return_header=True)

        rows = len(data)
        columns = len(data[0])
        example = data[0][2]
        self.assertEqual([rows, columns, example], [7, 31, "Savanna fires"])



class TestGetFireGDPYearData(unittest.TestCase):

    def test_funcPresent(self):
        self.assertRaises(TypeError, fire_gdp.get_fire_gdp_year_data)

    def test_main(self):
        co2file = Path(__file__).resolve().parent.parent / "data" / "testAgroFood.csv"
        GDPfile = Path(__file__).resolve().parent.parent / "data" / "testIMF.csv"

        data = fire_gdp.get_fire_gdp_year_data(co2file, GDPfile, "Afghanistan")
        comparison = [[2002, 0.0557, 178756]]
        self.assertAlmostEqual(data, comparison)





if __name__ == '__main__':
    unittest.main()
