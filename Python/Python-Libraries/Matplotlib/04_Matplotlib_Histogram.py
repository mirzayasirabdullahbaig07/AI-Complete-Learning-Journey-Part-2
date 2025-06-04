# Histogram Graph Example
# -----------------------
# A histogram is used in **univariate analysis** to visualize the **distribution of a single variable**.
# Use case: **Frequency count** – how often each range of values occurs in the dataset.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Simple Example - Basic Histogram
data = [30, 45, 76, 10, 28, 31, 17, 72]
plt.figure(figsize=(6, 4))
plt.hist(data, bins=5, color='skyblue', edgecolor='black')
plt.title('Histogram of Simple Data')
plt.xlabel('Value Range')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 2. Histogram from CSV (Univariate analysis on "batsman_runs")
df = pd.read_csv('/content/vk.csv')
plt.figure(figsize=(8, 5))
plt.hist(df['batsman_runs'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
         color='lightgreen', edgecolor='black')
plt.title('Histogram of Batsman Runs')
plt.xlabel('Runs')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# 3. Histogram with Log Scale from NumPy array
arr = np.load('/content/big-array.npy')
plt.figure(figsize=(8, 5))
plt.hist(arr, bins=[10, 20, 30, 40, 50, 60, 70], log=True, color='salmon', edgecolor='black')
plt.title('Histogram of Big Array (Log Scale)')
plt.xlabel('Value Range')
plt.ylabel('Log Frequency')
plt.grid(True)
plt.show()
