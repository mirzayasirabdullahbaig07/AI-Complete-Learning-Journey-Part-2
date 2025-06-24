# ------------------------------------------
# What is a Normal Distribution?
# ------------------------------------------

# A normal distribution, also called a Gaussian distribution, 
# is a continuous probability distribution commonly used in statistics.
# It is symmetric around the mean and has a characteristic bell-shaped curve.

# ------------------------------------------
# Key Characteristics:
# ------------------------------------------

# - Symmetrical around the mean (μ)
# - Most of the data points lie near the mean
# - Fewer data points are found as we move away from the mean (in the tails)
# - Asymptotic: the tails approach the x-axis but never touch it
# - Defined by two parameters: mean (μ) and standard deviation (σ)

# ------------------------------------------
# Parameters:
# ------------------------------------------

# 1. Mean (μ):
#    - Represents the center of the distribution
#    - Also the point of symmetry

# 2. Standard Deviation (σ):
#    - Measures the spread of the distribution
#    - Larger σ means the curve is wider and flatter
#    - Smaller σ means the curve is narrower and taller

# ------------------------------------------
# Visual Intuition:
# ------------------------------------------

# - The y-axis represents probability density (PDF)
# - The peak (highest point) occurs at the mean (μ)
# - Left and right ends are called "tails"
#     * Left tail: very low values
#     * Right tail: very high values
# - Most values are within ±1σ, ±2σ, and ±3σ from the mean

# ------------------------------------------
# Notation:
# ------------------------------------------

# X ~ N(μ, σ²)
# Where:
# - μ = mean
# - σ² = variance
# - σ = standard deviation

# ------------------------------------------
# Summary:
# ------------------------------------------

# - The normal distribution is bell-shaped, symmetric, and centered at μ
# - Tails represent rare/extreme values
# - It is widely used in real-world data modeling and hypothesis testing


# ---------------------------------------------------
# Why is the Normal Distribution Important?
# ---------------------------------------------------

# 1. Common in Nature:
#    Many natural and real-world phenomena follow a normal distribution.
#    Examples include:
#      - Height of people
#      - Weight of objects
#      - IQ scores
#      - Measurement errors
#      - Blood pressure levels
#    Because of this, the normal distribution offers a practical and reliable
#    way to model, analyze, and make predictions about such data.

# 2. Foundation of Statistical Inference:
#    The normal distribution forms the basis for many statistical tests,
#    including hypothesis testing and confidence intervals.

# 3. Central Limit Theorem:
#    According to the CLT, the sampling distribution of the sample mean
#    approaches a normal distribution as the sample size increases,
#    regardless of the original distribution.

# ---------------------------------------------------
# PDF Equation of the Normal Distribution:
# ---------------------------------------------------

# The probability density function (PDF) of a normal distribution is given by:

# f(x) = (1 / (σ * sqrt(2π))) * e^(-0.5 * ((x - μ)/σ)^2)

# Where:
# - x  = data point
# - μ  = mean of the distribution
# - σ  = standard deviation
# - e  = Euler’s number (~2.718)
# - π  = Pi (~3.14159)

# ---------------------------------------------------
# What is a Standard Normal Variate?
# ---------------------------------------------------

# A standard normal variate (Z) is a normalized version of a normal distribution.
# It has:
# - Mean (μ) = 0
# - Standard Deviation (σ) = 1

# This process is called **standardization**, and it allows us to:
# - Compare different normal distributions
# - Use Z-tables (or software) to calculate probabilities
# - Convert any normal variable X to Z using:

# Z = (X - μ) / σ

# This transformation is essential in many statistical applications.


# Benefits of the Standard Normal Distribution

# Standardizing a normal distribution allows us to:
# - Compare different distributions with each other.
# - Calculate probabilities using standard Z-tables or statistical software.

import pandas as pd
import seaborn as sns

# Load the Titanic dataset
titanic = pd.read_csv("link/to/titanic.csv")

# View the first few rows
titanic.head()

# Visualize the distribution of 'Age'
sns.kdeplot(titanic['Age'])

# Note: The age distribution is not perfectly normal (slightly skewed)

# Calculate the mean and standard deviation of Age
mean_age = titanic['Age'].mean()
std_age = titanic['Age'].std()

# Standardize the 'Age' column (convert to Z-scores)
titanic['Age_z'] = (titanic['Age'] - mean_age) / std_age

# Example Problem:
# Suppose the heights of adult males in a certain population follow a normal distribution
# with a mean of 68 inches and a standard deviation of 3 inches.
# What is the probability that a randomly selected adult male from this population is taller than 72 inches?

# Step 1: Calculate the Z-score
# Z = (X - μ) / σ
# Z = (72 - 68) / 3 = 4 / 3 ≈ 1.33

# Step 2: Use the Z-table to find the probability to the left of Z = 1.33
# P(Z < 1.33) ≈ 0.9082

# Step 3: We want the probability of being taller than 72 inches, which is:
# P(Z > 1.33) = 1 - P(Z < 1.33) = 1 - 0.9082 = 0.0918

# Final Answer:
# There is approximately a 9.18% probability that a randomly selected adult male
# from this population is taller than 72 inches.

# Properties of Normal Distribution

# Symmetry:
# The normal distribution is symmetric about its mean,
# which means the probability of observing a value above the mean
# is the same as observing a value below the mean.
# The bell-shaped curve reflects this perfect symmetry.

# Measures of Central Tendency:
# In a normal distribution, the mean, median, and mode are all equal.
# This equality reinforces the symmetry and balance of the distribution.

# What is the Empirical Rule?
# The normal distribution follows a well-known rule called the Empirical Rule
# (also known as the 68-95-99.7 Rule):
# - Approximately 68% of the data lies within 1 standard deviation of the mean
# - About 95% lies within 2 standard deviations
# - About 99.7% lies within 3 standard deviations

# What is Skewness?
# A normal distribution is a bell-shaped, symmetrical distribution 
# defined by a specific mathematical formula that describes how data is spread out.
# Skewness tells us when data is not symmetrical—meaning it is not normally distributed.

# Skewness is a statistical measure of the asymmetry of a probability distribution.
# It quantifies the degree to which a dataset deviates from the normal distribution.

# In a symmetrical distribution:
# - Mean = Median = Mode
# In a skewed distribution:
# - Mean, Median, and Mode are not equal
# - The distribution has a longer tail on one side

# Types of Skewness:
# - Positive Skew: Tail is longer on the right side
# - Negative Skew: Tail is longer on the left side
# - Zero Skew (Symmetrical): Perfectly balanced distribution

# CDF of Normal Distribution:
# The Cumulative Distribution Function (CDF) of a normal distribution
# gives the probability that a random variable will take a value less than or equal to a specific value.

# Uses of Normal Distribution in Data Science:
# - Outlier Detection
# - Making assumptions about data for machine learning algorithms
# - Hypothesis Testing
# - Central Limit Theorem (CLT): Explains why many distributions tend to become normal as sample size increases

