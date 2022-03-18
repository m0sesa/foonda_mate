import os
import sys
sys.path.insert(0, os.getcwd()+'/src')

from datetime import datetime
import unittest
import requests_mock
from userbase.userbase import Userbase

class TestLogic(unittest.TestCase):

    api_mock_url = 'mock://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
    mock_json = {
        '01-01-2022': 300,
        '02-01-2022': 500,
        '03-01-2022': 700,
        '04-01-2022': 1300,
        '05-01-2022': 2000,
        '06-01-2022': 3000,
        '07-01-2022': 3500,
        '08-01-2022': 4000,
        '09-01-2022': 4500,
    }

    def setUp(self):
        with requests_mock.Mocker() as m:
            m.get(self.api_mock_url, json=self.mock_json)

            self.userbase = Userbase(self.api_mock_url)

    def test_fetch_data(self):
        self.assertEqual(len(self.mock_json), len(self.userbase.get_all_data()))

    def test_available_start_end_date(self):
        self.assertTrue(datetime.strptime('1-1-2022', "%d-%m-%Y") == self.userbase.get_first_date())
        self.assertTrue(datetime.strptime('9-1-2022', "%d-%m-%Y") == self.userbase.get_last_date())
        self.assertFalse(datetime.strptime('1-1-2021', "%d-%m-%Y") == self.userbase.get_last_date())
        self.assertFalse(datetime.strptime('9-1-2021', "%d-%m-%Y") == self.userbase.get_last_date())

    def test_filter(self):
        self.assertEqual(self.userbase.filter_data('1-1-1990', '1-1-2000'), (None, 'start date less than available first date'))
        self.assertEqual(self.userbase.filter_data('1-1-2000', '1-1-1990'), (None, 'start date can not be greater than end date'))
        self.assertEqual(self.userbase.filter_data('1-1-2022', '19-1-2022'), (None, 'end date greater than available end date'))

        self.assertTrue(len(self.userbase.filter_data('01-01-2022', '05-01-2022')), 5)
        self.assertTrue(len(self.userbase.filter_data('01-01-2022', '01-01-2022')), 1)