import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class DataQualityCheck:
    def __init__(self, df):
        self.df = df

    def check_missing_values(self):
        return self.df.isnull().sum()

    def check_negative_values(self, columns):
        return (self.df[columns] < 0).sum()

    def plot_outliers(self, columns):
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=self.df[columns])
        plt.title('Boxplot for Outlier Detection')
        plt.show()
