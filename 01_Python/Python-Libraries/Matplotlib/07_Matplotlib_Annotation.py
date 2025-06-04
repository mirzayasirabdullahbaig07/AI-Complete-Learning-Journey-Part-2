
# What is Annotation in Matplotlib?
# Annotation means adding text labels to parts of your plot to make it more informative. In scatter plots, it’s often used to label data points — for example, showing player names at each point.


import pandas as pd
import matplotlib.pyplot as plt

# Load data
batters = pd.read_csv('/content/batter.csv')

# Take top 25 batters
subset = batters.head(25)

# Plot
plt.figure(figsize=(15, 7))
plt.scatter(subset['avg'], subset['strike_rate'], s=subset['runs'], color='skyblue', edgecolor='black')

# Add reference lines
plt.axhline(130, color="red", linestyle='--', label='SR = 130')
plt.axhline(140, color="yellow", linestyle='--', label='SR = 140')
plt.axvline(30, color="green", linestyle='--', label='Avg = 30')

# Annotate each point
for i in range(len(subset)):
    plt.text(subset['avg'].values[i] + 0.2,   # slightly offset for better visibility
             subset['strike_rate'].values[i] + 0.2,
             subset['batter'].values[i],
             fontsize=9)

# Labels and title
plt.xlabel('Batting Average')
plt.ylabel('Strike Rate')
plt.title('Top 25 Batters: Average vs Strike Rate with Runs as Bubble Size')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
