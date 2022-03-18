import os
import sys

from utils.dates import is_valid_date, to_datetime
sys.path.insert(0, os.getcwd()+'/src')

from datetime import datetime
import unittest

class TestUtils(unittest.TestCase):

    def test_to_datetime(self):
        self.assertEqual(datetime.strptime('01-05-2023', "%d-%m-%Y"), to_datetime('01-05-2023'))
        with self.assertRaises(ValueError):
            to_datetime('50-10-2023')

    def test_is_valid_date(self):
        self.assertTrue(is_valid_date('01-05-2023'))
        self.assertFalse(is_valid_date('01-15-2023'))