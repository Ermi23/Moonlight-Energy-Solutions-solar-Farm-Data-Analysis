import matplotlib.pyplot as plt
import streamlit as st

class BubbleCharts:
    def __init__(self, df):
        self.df = df

    def plot_bubble_chart(self, x_col, y_col, size_col):
        # Handle missing values by filling them with the mean of the respective column
        self.df[x_col].fillna(self.df[x_col].mean(), inplace=True)
        self.df[y_col].fillna(self.df[y_col].mean(), inplace=True)
        self.df[size_col].fillna(self.df[size_col].mean(), inplace=True)
        
        # Create the bubble chart
        plt.figure(figsize=(10, 8))
        plt.scatter(self.df[x_col], self.df[y_col], s=self.df[size_col]*10, alpha=0.5)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'Bubble Chart: {x_col} vs {y_col} with {size_col} as Bubble Size')
        plt.show()  # Display the plot
        plt.clf()  # Clear the figure after showing

   
    def plot_bubble_chart_streamlit(self, x_col, y_col, size_col):
        plt.figure(figsize=(10, 8))
        plt.scatter(self.df[x_col], self.df[y_col], s=self.df[size_col]*10, alpha=0.5)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.title(f'Bubble Chart: {x_col} vs {y_col} with {size_col} as Bubble Size')
        st.pyplot(plt)
