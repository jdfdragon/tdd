import os
import sys
import unittest

module_path = os.path.abspath(".")

sys.path.append(module_path)

sys.path.append("orig/src")

import fire_gdp 


class TestGetColumnIndex(unittest.TestCase):

    def test_name_present(self):
        pass



if __name__ == '__main__':
    unittest.main()
