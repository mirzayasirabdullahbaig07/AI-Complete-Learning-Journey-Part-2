# ---------------------------------------------
# 📊 Statistics: An Overview
# ---------------------------------------------
# Statistics is a branch of mathematics used for collecting, analyzing,
# interpreting, and presenting data. It plays a crucial role in various fields:

# - Business & Economics: Market analysis, financial forecasting, customer behavior.
# - Medicine: Clinical trials, health research, epidemiology.
# - Government & Politics: Public opinion surveys, election predictions, policy analysis.
# - Climate & Weather: Forecasting, trend analysis, environmental studies.
# - Everyday Life: Decision-making, risk assessment, quality control.

# ---------------------------------------------
# 🔢 Types of Statistics
# ---------------------------------------------

# 1. Descriptive Statistics:
#    - Summarizes and describes the main features of a dataset.
#    - Examples: Mean, median, mode, range, variance, standard deviation.

# 2. Inferential Statistics:
#    - Makes predictions or inferences about a population based on a sample.
#    - Concepts:
#      - Population: Entire group of interest.
#      - Sample: Subset of the population.
#    - Important considerations:
#      - Sample Size: Sufficient to represent the population.
#      - Randomness: Ensures each member has an equal chance of selection.
#      - Representativeness: Reflects the characteristics of the population.

# ---------------------------------------------
# 🧮 Types of Data
# ---------------------------------------------

# 1. Categorical (Qualitative) Data:
#    - Nominal: Categories without a specific order (e.g., gender, color).
#    - Ordinal: Categories with a specific order (e.g., satisfaction ratings).

# 2. Numerical (Quantitative) Data:
#    - Discrete: Countable values (e.g., number of students).
#    - Continuous: Measurable values (e.g., height, weight).

# ---------------------------------------------
# 📍 Measures of Central Tendency
# ---------------------------------------------

# - Mean: Average of all values.
#   - Formula: Mean = (Sum of all values) / (Number of values)
#   - Note: Sensitive to outliers.

# - Median: Middle value when data is arranged in order.
#   - For odd number of values: Middle value.
#   - For even number of values: Average of two middle values.

# - Mode: Most frequently occurring value.

# ---------------------------------------------
# 📈 Measures of Dispersion
# ---------------------------------------------

# - Range: Difference between the maximum and minimum values.
#   - Formula: Range = Max value - Min value
#   - Note: Sensitive to outliers.

# - Variance: Average of the squared differences from the mean.
#   - Formula: Variance = Σ(x_i - mean)² / N

# - Standard Deviation: Square root of the variance.
#   - Formula: SD = √Variance
#   - Note: Same units as the data.

# - Coefficient of Variation (CV): Ratio of the standard deviation to the mean, expressed as a percentage.
#   - Formula: CV = (SD / Mean) * 100%

# - Mean Absolute Deviation (MAD): Average of the absolute differences from the mean.
#   - Formula: MAD = Σ|x_i - mean| / N

# ---------------------------------------------
# 📊 Frequency Distribution Table
# ---------------------------------------------

# - A table that summarizes the number of occurrences of each value or range of values in a dataset.
#   - Helps in understanding the distribution and patterns within the data.

# Note: When working with data, it's essential to choose the appropriate
# measures and techniques based on the nature of the data and the objectives of the analysis.

# ---------------------------------------------
# 📦 Frequency, Relative and Cumulative Frequency (Categorical Data)
# ---------------------------------------------
# - Frequency: Count of occurrences in each category.
# - Relative Frequency: Frequency relative to the total (percentage).
# - Cumulative Frequency: Running total of frequencies.

# ---------------------------------------------
# 🗃️ Binning and Histograms
# ---------------------------------------------
# - You have to create categories and bins for numerical data.
# - This is typically visualized using histograms.

# Histogram Shapes:
# - Symmetric
# - Bimodal
# - Left-Skewed
# - Right-Skewed
# - Uniform
# - No clear pattern

# ---------------------------------------------
# 🔄 Graphs for Bivariate Analysis
# ---------------------------------------------
# 1. Categorical vs Categorical:
#    - Use contingency tables / cross tabs.
#    - Summarize the relationship between two categorical variables in a frequency table.

# 2. Numerical vs Numerical:
#    - Use scatter plots to visualize correlation or patterns.

# 3. Categorical vs Numerical:
#    - Use bar charts to compare numerical values across categories.



# what is quantiles and what is percentiles

# Quantiles are statistical measures used to divide a set of numerical data into equal-sized groups, with each group containing an equal number of observations.

# Quantiles are important measures of variability and can be used to: understand distribution of data, summarize and compare different datasets. They can also be used to identify outliers.

# There are several types of quantiles used in statistical analysis, including:

# a. Quartiles: Divide the data into four equal parts, Q1 (25th percentile), Q2 (50th percentile or median), and Q3 (75th percentile).

# b. Deciles: Divide the data into ten equal parts, D1 (10th percentile), D2 (20th percentile), ..., D9 (90th percentile).

# c. Percentiles: Divide the data into 100 equal parts, P1 (1st percentile), P2 (2nd percentile), ..., P99 (99th percentile).

# d. Quintiles: Divides the data into 5 equal parts.


# things to remember while calculating these measures:
 # 1- data should be sorted from low to high
 # 2- u basically findingt the location of an observation
 # 3- they are not actual values in the data
 # 4- all other tiles can be easily dervied from percentiles
# 

# How to calculate percentile?

# A percentile is a statistical measure that represents the percentage of observations 
# in a dataset that fall below a particular value.
# For example: the 75th percentile is the value below which 75% of the data lies.

# Formula to find the location (PL) of a percentile:
# PL = (P / 100) * (N + 1)

# Where:
# PL = Percentile Location (position in the sorted dataset)
# P  = Desired percentile (e.g., 75 for 75th percentile)
# N  = Total number of observations in the dataset

# Example: Find the 75th percentile from this data:
# Data = [78, 83, 82, 88, 91, 93, 94, 99, 98, 96]

# Step 1: Sort the data in ascending order
# Sorted = [78, 82, 84, 88, 91, 93, 94, 96, 98, 99]
# Index =   1   2   3   4   5   6   7   8   9   10

# Step 2: Use the formula
# PL = (75 / 100) * (10 + 1) = 8.25
# This means the 75th percentile lies 25% of the way between the 8th and 9th values

# Step 3: Interpolate
# 8th value = 96, 9th value = 98
# 96 + 0.25 * (98 - 96) = 96 + 0.5 = 96.5

# 75th percentile = 96.5

# -------------------------------------------------------

# How to find the percentile **rank** of a value?

# Formula:
# Percentile Rank = (x + 0.5 * y) / N * 100

# Where:
# x = Number of values below the given value
# y = Number of values equal to the given value
# N = Total number of values in the dataset

# Example: What is the percentile rank of the value 88?

# Data (sorted): [78, 82, 84, 88, 91, 93, 94, 96, 98, 99]
# Values below 88 = 3 (78, 82, 84) → x = 3
# Values equal to 88 = 1 → y = 1
# Total values = 10 → N = 10

# Percentile Rank = (3 + 0.5 * 1) / 10 * 100
#                 = 3.5 / 10 * 100
#                 = 35%

# Percentile rank of 88 is **35%**
