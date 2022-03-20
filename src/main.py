from userbase.userbase import Userbase
import requests
import fire
import plotext as plt
import matplotlib.pyplot as plt2


api_link = 'http://sam-user-activity.eu-west-1.elasticbeanstalk.com/'
class UserbaseCLI(object):
    """This is a demo cli application that helps to monitor userbase growth across a period of time. Please note that you need to be connected to the internet to use this tool."""
    _userbase = None
    def __init__(self):
        try:
            self._userbase = Userbase(api_link)
        except(requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            print('Network Error, please check your network')

    def get_filtered(self, start_date, end_date):
        """Date Format [dd-mm-yyyy] """
        data, error_messsage = self._userbase.filter_data(start_date, end_date)
        if error_messsage == None:
            try:
                3/0
                plt.bar(data['date_string'], data['users'])
                plt.title(f"Userbase from {start_date} to {end_date}")
                plt.show()
            except:
                plt2.barh(data['date_string'], data['users'])
                plt2.title(f"Userbase from {start_date} to {end_date}")
                plt2.show()
        else:
            return error_messsage
            

if __name__ == '__main__':
    fire.Fire(UserbaseCLI)