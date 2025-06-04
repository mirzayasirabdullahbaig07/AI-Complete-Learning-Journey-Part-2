# ---------------------------------------------
# 📊 What is Pandas Plot?
# ---------------------------------------------
# Pandas provides built-in plotting capabilities for both Series and DataFrames.
# Internally, it uses Matplotlib for visualization.
# You can create line, bar, scatter, pie, histogram, and many other types of plots.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------------------
# 🔹 Plotting on Series
# ---------------------------------------------
s = pd.Series([1, 2, 3, 5, 7, 19, 9])

# Line Plot
s.plot(kind='line', title='Line Plot')
plt.show()

# Pie Chart
s.plot(kind='pie', title='Pie Chart')
plt.show()

# Histogram
s.plot(kind='hist', title='Histogram')
plt.show()

# ---------------------------------------------
# 🔹 Scatter Plot using DataFrame
# ---------------------------------------------
# Load the built-in 'tips' dataset from seaborn
tips = sns.load_dataset('tips')
tips.head()

# Scatter plot: Total Bill vs Tip
tips.plot(kind='scatter',
          x='total_bill',
          y='tip',
          title='Total Bill vs Tip by Gender',
          marker='+',
          c='sex',       # Color by 'sex' column
          cmap='viridis')  # Colormap for color differentiation
plt.show()

# ---------------------------------------------
# 🔹 Line Plot on Stock Data
# ---------------------------------------------
# Assume 'stocks' is a DataFrame with 'Date', 'MSFT', 'FB', 'APPLE'
# Example:
# stocks = pd.read_csv('stocks.csv', parse_dates=['Date'])

# Line plot for one stock
stocks['MSFT'].plot(kind='line', title='MSFT Stock Price')
plt.show()

# Line plot with Date on X-axis for multiple stocks
stocks.plot(kind='line', x='Date', title='Stock Prices Over Time')
plt.show()

# Selecting only relevant columns
stocks[['Date', 'MSFT', 'FB']]  # Just filtering columns (not plotting here)

# ---------------------------------------------
# 🔹 Bar Chart
# ---------------------------------------------
# Mean total bill by gender
tips.groupby('sex')['total_bill'].mean().plot(kind='bar', title='Avg Total Bill by Gender')
plt.show()

# Bar plot for season-wise performance
temp = pd.read_csv('/content/batsman_season_record.csv')

# Bar chart for 2015 season
temp['2015'].plot(kind='bar', title='Batsman Performance in 2015')
plt.show()

# Full stacked bar chart
temp.plot(kind='bar', title='Performance per Season')
plt.show()

# Stacked bar chart
temp.plot(kind='bar', stacked=True, title='Stacked Season-wise Performance')
plt.show()

# ---------------------------------------------
# 🔹 Histogram
# ---------------------------------------------
# Histogram for all stock data
stocks.plot(kind='hist', title='Stock Price Distribution')
plt.show()

# Histogram for selected columns (example: Facebook and Apple)
# Make sure the column name is correct (should be a list, not a string)
stocks[['FB', 'APPLE']].plot(kind='hist', title='FB and Apple Distribution')
plt.show()

# ---------------------------------------------
# 🔹 Multiple Pie Charts (One per Match)
# ---------------------------------------------
# Example: Assuming df contains scores from match1, match2, match3
# Each pie chart represents score distribution for each match

df[['match1', 'match2', 'match3']].plot(
    kind='pie', 
    subplots=True, 
    figsize=(15, 7),
    title='Score Distribution in Matches'
)
plt.show()

# ---------------------------------------------
# 🔹 Subplots for Multiple Line Charts
# ---------------------------------------------
stocks.plot(kind='line', subplots=True, title='Stocks as Subplots')
plt.show()

# ---------------------------------------------
# 🔹 Multi-Index Pivot Plotting
# ---------------------------------------------
# Create a pivot table with multiple index and columns
pivot_table = tips.pivot_table(
    index=['day', 'time'],  # Row index
    columns=['sex', 'smoker'],  # Column index
    values='total_bill',  # Data values
    aggfunc='mean'  # Aggregation
)

# Line plot
pivot_table.plot(kind='line', title='MultiIndex Line Plot')
plt.show()

# Bar plot
pivot_table.plot(kind='bar', title='MultiIndex Bar Plot')
plt.show()

# Pie plot with subplots
pivot_table.plot(kind='pie', subplots=True, figsize=(16, 7), title='MultiIndex Pie Plot')
plt.show()
