import matplotlib.pyplot as plt

class BubbleCharts:
    def __init__(self, df):
        self.df = df

    def plot_bubble_chart(self, x_col, y_col, size_col):
        plt.figure(figsize=(10, 8))
        plt.scatter(self.df[x_col], self.df[y_col], s=self.df[size_col]*10, alpha=0.5)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'Bubble Chart: {x_col} vs {y_col} with {size_col} as Bubble Size')
        plt.show()
