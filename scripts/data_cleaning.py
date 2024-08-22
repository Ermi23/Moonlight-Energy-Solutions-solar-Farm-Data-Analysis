# data_cleaning.py

import pandas as pd

class DataCleaning:
    def __init__(self, df):
        self.df = df

    def drop_na_comments(self):
        self.df = self.df.dropna(subset=['Comments'])
        return self.df

    def fill_missing_values(self, column, value):
        # Update to avoid using inplace=True
        self.df[column] = self.df[column].fillna(value)
        return self.df
