import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import streamlit as st

class ZScoreAnalysis:
  def __init__(self, df):
    self.df = df

  def calculate_z_scores(self, columns):
    """
    Calculates Z-scores for the specified columns and adds them to the dataframe along with identified outliers.

    Args:
        columns (list): List of column names for which to calculate Z-scores.
    """
    # Calculate Z-scores
    self.z_scores = pd.DataFrame(stats.zscore(self.df[columns]), columns=columns)

    # Identify outliers (data points with absolute Z-score greater than 3)
    self.outliers = (np.abs(self.z_scores) > 3).astype(int)

    # Add Z-scores and outliers as new columns to the original dataframe
    self.df_z_scores = self.df.copy()
    self.df_z_scores[self.z_scores.columns] = self.z_scores
    self.df_z_scores[self.outliers.columns + '_outliers'] = self.outliers

  def plot_histograms(self, columns):
    """
    Plots histograms for the Z-scores of the specified columns.

    Args:
        columns (list): List of column names for which to plot histograms.
    """
    for column in columns:
      plt.figure(figsize=(10, 6))
      sns.histplot(self.df_z_scores[column], kde=True, bins=30, color='blue')
      plt.title(f'Z-score Distribution for {column}')
      plt.xlabel('Z-score')
      plt.ylabel('Frequency')
      plt.show()

  def plot_boxplots(self, columns):
    """
    Plots boxplots for the Z-scores of the specified columns.

    Args:
        columns (list): List of column names for which to plot boxplots.
    """
    for column in columns:
      plt.figure(figsize=(10, 6))
      sns.boxplot(x=self.df_z_scores[column], color='orange')
      plt.title(f'Boxplot for {column}')
      plt.xlabel('Z-score')
      plt.show()

  def plot_scatter(self, columns):
    """
    Plots scatter plots for each pair of columns, highlighting outliers.

    Args:
        columns (list): List of column names for which to plot scatter plots.
    """
    for i in range(len(columns) - 1):
      plt.figure(figsize=(10, 6))
      sns.scatterplot(data=self.df_z_scores, x=columns[i], y=columns[i+1],
                     hue=self.df_z_scores[f'{columns[i]}_outliers'], palette={0: 'blue', 1: 'red'})
      plt.title(f'Scatter Plot of {columns[i]} vs {columns[i+1]} with Outliers')
      plt.xlabel(columns[i])
      plt.ylabel(columns[i+1])
      plt.show()
      
    def calculate_z_scores(self, columns):
        self.z_scores = self.df[columns].apply(lambda x: (x - x.mean()) / x.std(), axis=0)

    def plot_z_scores(self):
        self.z_scores.plot(figsize=(12, 6))
        plt.title("Z-score Analysis")
        plt.xlabel("Index")
        plt.ylabel("Z-score")
        plt.show()

    def plot_z_scores_streamlit(self):
        self.z_scores.plot(figsize=(12, 6))
        plt.title("Z-score Analysis")
        plt.xlabel("Index")
        plt.ylabel("Z-score")
        st.pyplot(plt)