# Introduction to Matplotlib
# Mother of all data visualization libraries in Python

# Types of 2D Plots:
# - Line Plot
# - Scatter Plot
# - Bar Chart
# - Histogram
# - Pie Chart

# What is Data?
# Data refers to raw facts and figures. For example, students' information in a school.
# It can be anything that can be stored and analyzed.

# Types of Data:
# 1. Numerical Data:
#    - Data in numeric form.
#    - Examples: Age of people, temperature over days.
# 2. Categorical Data:
#    - Data in group form.
#    - Examples: Phone brands used by students, gender, universities.

# Understanding data is crucial for proper visualization.
# It helps in deciding the right type of graph.

# Types of Analysis:
# - Univariate Analysis: Plotting single column
# - Bivariate Analysis: Plotting two columns
# - Multivariate Analysis: Plotting more than two columns

# Important Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt  # Note: Corrected the spelling
import seaborn as sns

# 2D Line Plot
# - Used for bivariate analysis
# - Can be applied to numerical vs numerical or categorical vs numerical data
# - Commonly used in time series analysis (e.g., stock prices, COVID-19 cases)

# Example with manual data
iphone = [40000, 50000, 54000, 47000, 65000, 96000, 70000]
year = [2017, 2018, 2019, 2020, 2021, 2022, 2023]
plt.plot(year, iphone)

# Example with dataset
batsman = pd.read_csv("sharma-kohli.csv")

# Plotting data
plt.plot(batsman['index'], batsman['V Kohli'])
plt.plot(batsman['index'], batsman['RG Sharma'])

# Adding labels and title
plt.title('Rohit Sharma and Virat Runs Comparison')
plt.xlabel('Year')
plt.ylabel('Runs')

# Customizing colors
plt.plot(batsman['index'], batsman['V Kohli'], color='green')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red')

# Customizing line style
plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dashed')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red', linestyle='dashed')

# Customizing line width
plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dashed', linewidth=4)
plt.plot(batsman['index'], batsman['RG Sharma'], color='red', linestyle='dashed')

# Adding markers
plt.plot(batsman['index'], batsman['V Kohli'], color='green', linestyle='dashed', marker='d', markersize=10)
plt.plot(batsman['index'], batsman['RG Sharma'], color='red', linestyle='dashed')

# Adding legend
plt.plot(batsman['index'], batsman['V Kohli'], color='green', label='Virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red', label='Sharma')
plt.legend()

# Trimming outliers with axis limits
iphone = [40000, 50000, 54000, 47000, 65000, 96000, 70000, 10000000]
year = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
plt.plot(year, iphone)
plt.ylim(0, 75000)
plt.xlim(2019, 2023)

# Adding grid
plt.plot(batsman['index'], batsman['V Kohli'], color='green', label='Virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red', label='Sharma')
plt.title('Rohit Sharma and Virat Runs Comparison')
plt.xlabel('Year')
plt.ylabel('Runs')
plt.legend()
plt.grid()

# Final Plot with show()
plt.plot(batsman['index'], batsman['V Kohli'], color='green', label='Virat')
plt.plot(batsman['index'], batsman['RG Sharma'], color='red', label='Sharma')
plt.title('Rohit Sharma and Virat Runs Comparison')
plt.xlabel('Year')
plt.ylabel('Runs')
plt.legend()
plt.grid()
plt.show()
