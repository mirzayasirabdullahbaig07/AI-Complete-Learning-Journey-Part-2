# What is a Scatter Plot?
# A scatter plot is a graphical representation used to visualize the relationship between two numerical variables.

# 3 Important Things About Scatter Plot:
# 1. Scatter plot always applies on bivariate data — means 2 columns.
# 2. It can only be applied on numerical values — both variables must be numbers.
# 3. It is used to analyze correlation between two quantities.

# Note:
# - 2D plot and scatter plot are similar.
# - In 2D plot, we join the points.
# - For making a 2D plot, you first create a scatter plot.
# - 2D plot is a special case of scatter plot. Scatter plot is the main base.

# How to plot a scatter plot:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # Note: Corrected the spelling
import seaborn as sns

x = np.linspace(-10, 10, 50)
y = 10 * x + 3 + np.random.randint(0, 300, 50)

plt.scatter(x, y)

# Example using a CSV file:
df = pd.read_csv('batter.csv')
df.head(50)

plt.scatter(df['avg'], df['strike_rate'], color='red')
plt.title("Average of Top 50 Batsmen")
plt.xlabel("Average")
plt.ylabel("Strike Rate")

# Example using seaborn dataset:
tips = sns.load_dataset('tips')
tips

plt.scatter(tips['total_bill'], tips['tip'], s=tips['size'] * 20)

# Notes:
# - This is a smaller technique.
# - This is suitable for larger datasets.

# plt.plot() vs plt.scatter():
# - plt.plot(): You cannot add size and other customizations.
# - This is a faster technique.
# - Suitable for small datasets.

plt.plot(tips['total_bill'], tips['tip'], 'o')
