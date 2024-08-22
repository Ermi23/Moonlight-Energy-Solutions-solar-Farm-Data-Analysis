import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

class ZScoreAnalysis:
    def __init__(self, df):
        self.df = df

    def calculate_z_scores(self, columns):
        # Calculate Z-scores for the specified columns
        self.z_scores = pd.DataFrame(stats.zscore(self.df[columns]), columns=columns)
        
        # Identify outliers
        self.outliers = (np.abs(self.z_scores) > 3).astype(int)
        
        # Add Z-scores and outliers to the original dataframe
        self.df_z_scores = self.df.copy()
        self.df_z_scores[self.z_scores.columns] = self.z_scores
        self.df_z_scores[self.outliers.columns + '_outliers'] = self.outliers

    # Histogram of Z-scores
    def plot_histograms(z_score_analysis, columns):
        for column in columns:
            plt.figure(figsize=(10, 6))
            sns.histplot(z_score_analysis.df_z_scores[column], kde=True, bins=30, color='blue')
            plt.title(f'Z-score Distribution for {column}')
            plt.xlabel('Z-score')
            plt.ylabel('Frequency')
            plt.show()

    # Boxplot for each column
    def plot_boxplots(z_score_analysis, columns):
        for column in columns:
            plt.figure(figsize=(10, 6))
            sns.boxplot(x=z_score_analysis.df_z_scores[column], color='orange')
            plt.title(f'Boxplot for {column}')
            plt.xlabel('Z-score')
            plt.show()

    # Scatter plot with outliers highlighted
    def plot_scatter(z_score_analysis, columns):
        for i in range(len(columns) - 1):
            plt.figure(figsize=(10, 6))
            sns.scatterplot(data=z_score_analysis.df_z_scores, x=columns[i], y=columns[i+1],
                            hue=z_score_analysis.df_z_scores[f'{columns[i]}_outliers'], palette={0: 'blue', 1: 'red'})
            plt.title(f'Scatter Plot of {columns[i]} vs {columns[i+1]} with Outliers')
            plt.xlabel(columns[i])
            plt.ylabel(columns[i+1])
            plt.show()
