import string
import pandas as pd

from utils.dates import is_valid_date, to_datetime
from utils.network import get_json


class Userbase():

    api_link = ''
    data = None

    def __init__(self, api_link):
        self.api_link = api_link
        self.data = self._get_data(self.api_link)

    def _get_data(self, api_link):
        data_json = get_json(api_link)
        dataframe = pd.DataFrame.from_dict(data_json, orient="index", columns=['users'])
        dataframe.reset_index(inplace=True)
        dataframe.rename({'index': 'date_string'} , axis=1, inplace=True)

        dataframe['date'] = pd.to_datetime(dataframe.date_string, format='%d-%m-%Y')
        dataframe.sort_values(by='date', inplace = True)

        return dataframe

    def filter_data(self, start_date: string, end_date: string):
        if (is_valid_date(start_date) and is_valid_date(end_date)):
            if (to_datetime(start_date) > to_datetime(end_date)):
                return None, 'start date can not be greater than end date'
            if (to_datetime(start_date) < self.get_first_date()):
                return None, 'start date less than available first date'
            if (to_datetime(end_date) > self.get_last_date()):
                return None, 'end date greater than available end date'
            return self.data[(self.data['date'] >= to_datetime(start_date)) & (self.data['date'] <= to_datetime(end_date))], None
        
        return None, 'invalid date provided'

    def get_all_data(self):
        return self.data

    def get_last_date(self):
        return self.data.iloc[-1]['date']

    def get_first_date(self):
        return self.data.iloc[0]['date']