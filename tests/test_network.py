import os
import sys
sys.path.insert(0, os.getcwd()+'/src')

from datetime import datetime
import unittest
import requests
import requests_mock
from userbase.userbase import Userbase

class NetworkTests(unittest.TestCase):

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

    def test_call_api_connection_error(self):
        """Test Raise Connection Error"""
        with self.assertRaises(requests.exceptions.ConnectionError):
            with requests_mock.Mocker() as m:
                m.get(self.api_mock_url, exc=requests.exceptions.ConnectionError)

                requests.get(self.api_mock_url)

    def test_call_api_timeout_error(self):
        """Test Raise Timeout Error"""
        with self.assertRaises(requests.exceptions.Timeout):
            with requests_mock.Mocker() as m:
                m.get(self.api_mock_url, exc=requests.exceptions.Timeout)

                requests.get(self.api_mock_url)

    def test_call_api(self):
        """Test get data"""
        with requests_mock.Mocker() as m:
            m.get(self.api_mock_url, json=self.mock_json)

            self.assertEqual(self.mock_json, requests.get(self.api_mock_url).json())

    def test_first_date(self):
        """Test first date"""
        with requests_mock.Mocker() as m:
            m.get(self.api_mock_url, json=self.mock_json)

            userbase = Userbase(self.api_mock_url)
            first_date = datetime.strptime(list(self.mock_json.keys())[0], "%d-%m-%Y")

            self.assertEqual(first_date, userbase.get_first_date())

    def test_last_date(self):
        """Test last date"""
        with requests_mock.Mocker() as m:
            m.get(self.api_mock_url, json=self.mock_json)

            userbase = Userbase(self.api_mock_url)
            first_date = datetime.strptime(list(self.mock_json.keys())[-1], "%d-%m-%Y")

            self.assertEqual(first_date, userbase.get_last_date())


if __name__ == '__main__':
    unittest.main()