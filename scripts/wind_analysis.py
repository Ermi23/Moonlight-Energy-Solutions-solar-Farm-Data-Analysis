from windrose import WindroseAxes
import matplotlib.pyplot as plt

class WindAnalysis:
    def __init__(self, df):
        self.df = df

    def plot_wind_rose(self):
        ax = WindroseAxes.from_ax()
        ax.bar(self.df['WD'], self.df['WS'], normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.title('Wind Speed and Direction Distribution')
        plt.show()
