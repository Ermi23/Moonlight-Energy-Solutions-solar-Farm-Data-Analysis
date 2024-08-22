import matplotlib.pyplot as plt

class Histograms:
    def __init__(self, df):
        self.df = df

    def plot_histograms(self, columns):
        self.df[columns].hist(figsize=(10, 8), bins=20)
        plt.suptitle('Histograms of Key Variables')
        plt.show()
