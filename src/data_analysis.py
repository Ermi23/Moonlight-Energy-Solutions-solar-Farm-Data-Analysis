import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_1 = pd.read_excel('data/benin-malanville.csv')
df_2 = pd.read_excel('data/sierraleone-bumbuna.csv')
df_3 = pd.read_excel('data/togo-dapaong_qc.csv')

# Check data structure
print(df_1.info())
print(df_2.info())
print(df_3.info())

# Handle missing values
df_1.dropna(inplace=True)
df_2.dropna(inplace=True)
df_3.dropna(inplace=True)

# Calculate summary statistics
print(df_1.describe())
print(df_2.describe())
print(df_3.describe())

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(df_1['feature1'], df_1['feature2'])
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('Scatter Plot of Feature 1 vs Feature 2')
plt.savefig('notebooks/scatter_plot.png')

# Histogram
plt.figure(figsize=(8, 6))
df_1['feature1'].hist(bins=20)
plt.xlabel('Feature 1')
plt.ylabel('Frequency')
plt.title('Histogram of Feature 1')
plt.savefig('notebooks/histogram.png')