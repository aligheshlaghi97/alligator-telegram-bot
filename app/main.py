#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import datetime as dt
import plotly.graph_objects as go
from visualize import visualization
from telegram_bot import TelegramBot
from indicators import AddIndicators
from read_data import DataReadYfinance
from signal_strategy import SmaCrossStrategy
import plotly
import schedule
import time


def task(reading_data):  
    reading_data.get_data()
    reading_data.data_cleaning()
    df = reading_data.data
    ind_add = AddIndicators(df)
    ind_add.df
    df = ind_add.df
    df = df.iloc[50:]
    df = df.reset_index(drop=True)
    
    # m1 data
    reading_data.get_data(period='1m')
    reading_data.data_cleaning()
    df_1m = reading_data.data
    ind_add = AddIndicators(df_1m)
    ind_add.df
    df_1m = ind_add.df
    df_1m = df_1m.iloc[50:]
    df_1m = df_1m.reset_index(drop=True)

    strategy = SmaCrossStrategy()
    status = strategy.strategy_confirm(df)
    if status[0]:
        message_text = status[1]
        vis = visualization(df)
        # vis.show_fig()
        vis.save_fig('test')
        vis_1m = visualization(df_1m)
        vis_1m.save_fig('test_1m')
        telegram_bot = TelegramBot(message_text, 'test')
        telegram_bot.send_message()
        telegram_bot = TelegramBot('1m', 'test_1m')
        telegram_bot.send_message()

reading_data = DataReadYfinance()

print(f"started at {time.strftime('%X')}")
print(f"connection to Yfinance started at {time.strftime('%X')}")
def job():
    print(f"Started Reading Data at {time.strftime('%X')}")
    task(reading_data)
    print(f"Finished Reading Data at {time.strftime('%X')}")

schedule.every(1).minutes.at(':00').do(job)
while True:
    schedule.run_pending()
    time.sleep(0.1)

