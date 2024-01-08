import pandas as pd
from datetime import datetime


def utodatetime(unix_time):
    return datetime.utcfromtimestamp(unix_time).strftime('%Y-%m-%d %H:%M:%S')


data = pd.read_csv('data.csv')


data['time'] = data['time'].apply(utpdatetime)


data.to_csv('data_modified.csv', index=False)

