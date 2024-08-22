import seaborn as sns
import matplotlib.pyplot as plt

class TemperatureHumidityAnalysis:
    def __init__(self, df):
        self.df = df

    def plot_temperature_vs_humidity(self):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='RH', y='TModA', data=self.df, label='TModA')
        sns.scatterplot(x='RH', y='TModB', data=self.df, label='TModB', color='red')
        plt.title('Impact of Relative Humidity on Temperature')
        plt.show()
