import fxcmpy
from dotenv import load_dotenv
import os


class DataReadFxcm:
    def __init__(self):
        load_dotenv()
        self.con = fxcmpy.fxcmpy(access_token = os.environ['FXCM_API_TOKEN'], log_level='error',log_file=None)
        self.data = None
#         self.get_data()
#         self.data_cleaning()
        
    def get_data(self, currency='EUR/USD', period='m5', length=150):
        self.data = self.con.get_candles(currency, period=period, number=length)
        self.data = self.data.reset_index(drop = False)
        
    def data_cleaning(self):
        new_dates = []
        new_format = "%m-%d-%Y, %H:%M:%S"
        x_dates = self.data['date']
        for l_date in x_dates:
            new_date_ = l_date.strftime(new_format)
            new_dates.append(new_date_)
        self.data['time_str'] = new_dates
        self.data = self.data.rename({'bidopen': 'Open', 'bidhigh': 'High', 'bidlow': 'Low', 'bidclose': 'Close'}, axis=1)
        self.data = self.data[['Open', 'High', 'Low', 'Close', 'time_str']]
        
