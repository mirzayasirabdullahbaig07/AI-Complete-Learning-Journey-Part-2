# Bar Chart Visualization in Python

# What is a Bar Chart?
# - A bar chart represents categorical data with rectangular bars.
# - X-axis: categorical variables (e.g., names, colors, products).
# - Y-axis: numerical values (aggregates like count, sum, etc.).
# - Use case: Bivariate analysis → comparing a numeric value across categories.
# - Great for showing comparisons across different groups.

# Importing Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------------
# 1. Simple Vertical Bar Chart
# -----------------------------------
children = [10, 20, 40, 30, 15]
colors = ['red', 'blue', 'green', 'yellow', 'pink']
plt.figure(figsize=(6,4))
plt.bar(colors, children)
plt.title("Number of Children by Color Category")
plt.xlabel("Color")
plt.ylabel("Number of Children")
plt.show()

# -----------------------------------
# 2. Horizontal Bar Chart
# -----------------------------------
# Useful when category labels are long or there are many categories.
plt.figure(figsize=(6,4))
plt.barh(colors, children)
plt.title("Number of Children by Color Category (Horizontal)")
plt.xlabel("Number of Children")
plt.ylabel("Color")
plt.show()

# -----------------------------------
# 3. Multiple Quantities on Same Bar Chart (Grouped Bar Chart)
# -----------------------------------

# Load dataset
df = pd.read_csv('/content/batsman_season_record.csv')  # Make sure this path is valid
print(df)

# Method 1: Simple overlay (not ideal, can cause overlap)
plt.figure(figsize=(10,6))
plt.bar(df['batsman'], df['2015'], label='2015')
plt.bar(df['batsman'], df['2016'], label='2016')
plt.bar(df['batsman'], df['2017'], label='2017')
plt.title("Batsman Runs per Year (Overlapping)")
plt.xlabel("Batsman")
plt.ylabel("Runs")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Method 2: Better approach – setting bar width and positions (Grouped Bars)
x = np.arange(df.shape[0])  # number of batsmen
width = 0.25

plt.figure(figsize=(10,6))
plt.bar(x - width, df['2015'], width=width, label='2015')
plt.bar(x, df['2016'], width=width, label='2016')
plt.bar(x + width, df['2017'], width=width, label='2017')
plt.xticks(x, df['batsman'], rotation=45)
plt.title("Batsman Runs per Year (Grouped)")
plt.xlabel("Batsman")
plt.ylabel("Runs")
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------------
# 4. Stacked Bar Chart
# -----------------------------------
# Useful for showing total and part-to-whole relationships.

plt.figure(figsize=(10,6))
plt.bar(df['batsman'], df['2015'], label='2015')
plt.bar(df['batsman'], df['2016'], bottom=df['2015'], label='2016')
plt.bar(df['batsman'], df['2017'], bottom=df['2015'] + df['2016'], label='2017')
plt.title("Batsman Runs per Year (Stacked)")
plt.xlabel("Batsman")
plt.ylabel("Total Runs")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# -----------------------------------
# 5. Common Mistake Demonstration (Incorrect tick handling)
# -----------------------------------

# Problem: Long labels causing layout issues
children = [10, 20, 40, 30, 15]
long_labels = [
    'red red red red red red red red red red',
    'blue blue blue blue blue blue',
    'green green green green green green green green',
    'yellow yellow yellow yellow yellow',
    'pink pink pink pink pink'
]

plt.figure(figsize=(8,5))
plt.barh(long_labels, children)
plt.title("Incorrect Tick Example")
plt.xlabel("Value")
plt.tight_layout()

# Fixing typo: incorrect method `xtrick` should be `xticks` or `yticks` depending on chart
plt.yticks(rotation='vertical')  # rotate y-axis labels in horizontal bar chart
plt.show()
