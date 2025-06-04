# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
batters = pd.read_csv('/content/batter.csv')

# Basic scatter plot using pyplot
plt.figure(figsize=(8, 5))
plt.scatter(batters['avg'], batters['strike_rate'])
plt.title("Average vs Strike Rate")
plt.xlabel("Average")
plt.ylabel("Strike Rate")
plt.show()

# Using fig and ax objects for better control
fig, ax = plt.subplots(figsize=(15, 6))
ax.scatter(batters['avg'], batters['strike_rate'])
ax.set_title("Batter Average vs Strike Rate")
ax.set_xlabel("Average")
ax.set_ylabel("Strike Rate")
plt.show()

# Subplots - multiple plots in a single figure (2 rows, 1 column)
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(10, 6), sharex=True)

# First subplot
ax[0].scatter(batters['avg'], batters['strike_rate'], color="red")
ax[0].set_title("Average vs Strike Rate")
ax[0].set_ylabel("Strike Rate")

# Second subplot
ax[1].scatter(batters['avg'], batters['runs'])
ax[1].set_title("Average vs Runs")
ax[1].set_ylabel("Runs")
ax[1].set_xlabel("Average")

plt.tight_layout()
plt.show()

# Subplots with 2 rows and 2 columns
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10, 6))

# Top-left plot
ax[0, 0].scatter(batters['avg'], batters['strike_rate'], color="red")
ax[0, 0].set_title("Avg vs Strike Rate")

# Top-right plot
ax[0, 1].scatter(batters['avg'], batters['runs'])
ax[0, 1].set_title("Avg vs Runs")

# Bottom-left histogram
ax[1, 0].hist(batters['avg'], bins=10, color='blue')
ax[1, 0].set_title("Distribution of Avg")

# Bottom-right histogram
ax[1, 1].hist(batters['runs'], bins=10, color='green')
ax[1, 1].set_title("Distribution of Runs")

plt.tight_layout()
plt.show()
