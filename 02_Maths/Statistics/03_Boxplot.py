# What is a Boxplot?
# A boxplot, also known as a box-and-whisker plot, is a graphical representation of a dataset 
# that shows the distribution of the data. It displays a summary of the dataset, 
# including the minimum and maximum values, the first quartile (Q1), the median (Q2), and the third quartile (Q3).

# Benefits of Boxplot:
# - Provides an easy way to visualize the distribution of data
# - Indicates the skewness of the data
# - Helps identify outliers
# - Useful for comparing multiple categories of data side-by-side

# How to Create a Boxplot:
# Example data: 6, 213, 241, 260, 281, 290, 314, 321, 350, 1500

# Step 1: Sort the data 
# Sorted data: 6, 213, 241, 260, 281, 290, 314, 321, 350, 1500

# Step 2: Create the box using Q1, Q2 (median), and Q3

# Calculate Q2 (median):
# Q2 = 50/100 * (n + 1) = 0.5 * 11 = 5.5 → (281 + 290)/2 = 285.5

# Calculate Q1:
# Q1 = 25/100 * (n + 1) = 0.25 * 11 = 2.75 → Q1 = 213 + 0.75*(241 - 213) = 213 + 21 = 234

# Calculate Q3:
# Q3 = 75/100 * (n + 1) = 0.75 * 11 = 8.25 → Q3 = 321 + 0.25*(350 - 321) = 321 + 7.25 = 328.25

# Now build the whiskers (min and max range excluding outliers):

# Calculate IQR:
# IQR = Q3 - Q1 = 328.25 - 234 = 94.25

# Lower limit = Q1 - 1.5 * IQR = 234 - 1.5*94.25 = 93.625
# Upper limit = Q3 + 1.5 * IQR = 328.25 + 1.5*94.25 = 468.625

# Any values below 93.625 or above 468.625 are considered outliers

# Outliers in the dataset:
# - 6 (below lower limit)
# - 1500 (above upper limit)

# So, valid whisker range: 213 to 350 (excluding outliers)

# Side-by-Side Boxplot Creation:
# You can create side-by-side boxplots to compare different categories or groups within the same graph.
# This allows visual comparison of distributions across multiple datasets.
