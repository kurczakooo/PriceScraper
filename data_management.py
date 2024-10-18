import numpy as np
import pandas as pd
from datetime import datetime

class DataManager:
    def __init__(self, path):
        self.df = pd.DataFrame()
        self.path = path
        
    def load_data(self):
        self.df = pd.read_csv(self.path, header=0, index_col=0)
        self.df['time'] = pd.to_datetime(self.df['time'])
        
    def add_row(self, price):

        formatted_time = pd.to_datetime(datetime.now())

        print(f'\n price: {price}, time: {formatted_time}')

        self.df.loc[len(self.df)] = [price, formatted_time]
        
        print('\nAdded a row!')
        
    def save_df_to_path(self):
        self.df.to_csv(self.path)    
        print('\nSaved the price df to file!')