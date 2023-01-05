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
from read_data import DataReadFxcm
from signal_strategy import SmaCrossStrategy
import plotly
import fxcmpy
import schedule
import time


# In[2]:


def connection_check(data_reader):
    if data_reader is not None:
        if data_reader.con.connection_status != 'established':
            reading_data = DataReadFxcm()
            return reading_data
    
    return None


# In[3]:


def task(reading_data):  
#     if connection != 'established':
#         reading_data = DataReadFxcm()
#         connection = reading_data.con.connection_status
    reading_data.get_data()
    reading_data.data_cleaning()
    df = reading_data.data
    ind_add = AddIndicators(df)
    ind_add.df
    df = ind_add.df
    df = df.iloc[50:]
    df = df.reset_index(drop=True)
    
    # m1 data
    reading_data.get_data(period='m1')
    reading_data.data_cleaning()
    df_1m = reading_data.data
    ind_add = AddIndicators(df_1m)
    ind_add.df
    df_1m = ind_add.df
    df_1m = df_1m.iloc[50:]
    df_1m = df_1m.reset_index(drop=True)
    
#     display(df)
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
        telegram_bot = TelegramBot('m1', 'test_1m')
        telegram_bot.send_message()


# In[4]:


reading_data = DataReadFxcm()


# In[5]:


print(f"started at {time.strftime('%X')}")
print(f"connection to FXCM started at {time.strftime('%X')}")
def job():
    print("I'm working...")
    print(f"Started Reading Data at {time.strftime('%X')}")
    task(reading_data)
    print(f"Finished Reading Data at {time.strftime('%X')}")

schedule.every(5).minutes.at(':00').do(job)
while True:
    schedule.run_pending()
    time.sleep(0.1)


# In[ ]:





# In[ ]:




