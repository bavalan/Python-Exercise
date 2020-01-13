import unittest
from database import *
from squeal import *


class TestAssignment(unittest.TestCase):
    def Test_Product(self):
        d1 = {"Bava": ["1", "2"], "lan": ["3", "4"]}
        d2 = {"Thanga": ["5", "6"], "rajah": ["7", "8"]}
        t1 = Table()
        t2 = Table()
        t1.set_dict(d1)
        t2.set_dict(d2)
        result_table = squeal.cartesian_product(t1, t2)
        result_dict = result_table.get_dict()
        expected_dict = {"Bava": ["1", "1", "2", "2"],
                         "lan": ["3", "3", "4", "4"],
                         "Thanga": ["5", "6", "5", "6"],
                         "rajah": ["7", "8", "7", "8"]}
        self.assertEqual(result_dict, expected_dict)

if(__name__ == '__main__'):
    unittest.main()
