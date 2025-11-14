import pandas as pd

class DataAnalysis:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def summary(self):
        return self.df.describe(include='all').transpose()
    
    def head(self, n=5):
        return self.df.head(n)
    
    def columns(self):
        return self.df.columns.tolist()