# ======================================
# Statistical Moments & Kurtosis
# ======================================

# In statistics, there are four key moments:
# 1. Mean                → Central tendency
# 2. Standard Deviation  → Dispersion
# 3. Skewness            → Asymmetry of the distribution
# 4. Kurtosis            → Tailedness (fat tails or outliers)

# --------------------------------------
# What is Kurtosis?
# --------------------------------------

# Kurtosis is the 4th statistical moment. In probability theory and statistics,
# kurtosis (meaning "curved" or "arching") measures the tailedness of the 
# probability distribution of a real-valued random variable.
# Like skewness, kurtosis helps describe the shape of the distribution.
# It tells how heavy or light the tails of the distribution are — i.e., 
# how likely extreme values (outliers) are.

# Higher kurtosis ⇒ more extreme outliers (fat tails)
# Lower kurtosis ⇒ fewer extreme outliers (thin tails)

# --------------------------------------
# Practical Use-case in Finance
# --------------------------------------

# In finance, kurtosis risk refers to the risk associated with extreme outcomes 
# or “fat tails” in the distribution of returns of a particular asset or portfolio.

# ▶ A high kurtosis means a higher likelihood of large gains or losses.
# ▶ Investors may adjust their strategies to account for kurtosis risk.

# --------------------------------------
# Excess Kurtosis & Types
# --------------------------------------

# Excess Kurtosis:
# It measures how much more peaked or flat a distribution is compared to a 
# normal distribution (which has a kurtosis of 3).
# Excess kurtosis = Sample kurtosis − 3

# ➤ Types of Kurtosis:

# 1. Leptokurtic (Positive Excess Kurtosis)
# - Fat tails, more extreme values.
# - Riskier and more volatile.
# - Example: Financial assets with sudden price jumps.

# 2. Platykurtic (Negative Excess Kurtosis)
# - Thin tails, fewer extreme values.
# - Less risky and more stable.
# - Example: Assets with gradual price movements.

# 3. Mesokurtic (Zero Excess Kurtosis)
# - Similar to normal distribution.
# - Balanced risk and return.
# - Example: Ideal asset return distribution in theory.

# ======================================
# How to Check if Data is Normally Distributed?
# ======================================

# 1. Visual Inspection (Histogram/KDE)
# 2. QQ Plot (Quantile-Quantile Plot)
# 3. Statistical Tests (e.g., Shapiro-Wilk, Anderson-Darling)

# --------------------------------------
# 1. Visual Inspection
# --------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('iris')
sns.kdeplot(df['sepal_length'])
plt.title("KDE Plot - Sepal Length")
plt.show()

# --------------------------------------
# 2. QQ Plot (Quantile-Quantile Plot)
# --------------------------------------

import numpy as np
from scipy import stats

# Generate quantiles from sample data
data = sorted(df['sepal_length'].tolist())
y_quantiles = [np.percentile(data, i) for i in range(1, 101)]

# Generate quantiles from normal distribution
normal_sample = np.random.normal(loc=0, scale=1, size=1000)
x_quantiles = [np.percentile(normal_sample, i) for i in range(1, 101)]

# Plot QQ plot
sns.scatterplot(x=x_quantiles, y=y_quantiles)
plt.xlabel("Theoretical Quantiles (Normal Dist)")
plt.ylabel("Sample Quantiles (Data)")
plt.title("QQ Plot: Sample vs Normal Distribution")
plt.grid(True)
plt.show()

# QQ Plot Interpretation:
# ➤ If the points fall along a straight line → the distribution is approximately normal.
# ➤ Deviations from the line → distribution is not normal.

# --------------------------------------
# Does QQ Plot Only Test Normality?
# --------------------------------------

# No. QQ plots can compare data to **any distribution**, not just normal.

import statsmodels.api as sm

# Fit a uniform distribution
x = df['sepal_length']
params = stats.uniform.fit(x)  # Get parameters for uniform fit
dist = stats.uniform(loc=params[0], scale=params[1])

# QQ Plot with uniform distribution
fig = sm.qqplot(x, dist=dist, line='45')
plt.title("QQ Plot: Uniform Distribution Fit")
plt.xlabel("Theoretical Quantiles (Uniform)")
plt.ylabel("Sample Quantiles")
plt.grid(True)
plt.show()

# ======================================
# Summary
# ======================================

# ✔ Kurtosis measures the extremity of outliers in the data.
# ✔ Leptokurtic → More extreme values (fat tails)
# ✔ Platykurtic → Fewer extreme values (thin tails)
# ✔ Mesokurtic  → Normal tail thickness
# ✔ QQ plots help compare any dataset against any theoretical distribution.
# ✔ Use visual plots + statistical tests to confirm normality assumptions.


# What is Uniform Distribution and Its Types
# In probability theory and statistics, a uniform distribution is a probability distribution 
# where all outcomes are equally likely within a given range. This means that if you select a random 
# value from this range, any value would be as likely as any other.

# Types:
# - Discrete Uniform Distribution
# - Continuous Uniform Distribution

# Notation:
# X ~ U(a, b)

# Examples:
# a. The height of a randomly selected person from a group with heights ranging from 5'6" to 6'0" 
#    follows a continuous uniform distribution.
# b. The time a machine takes to produce a product, ranging from 5 to 10 minutes.
# c. The distance a car travels on a full tank, ranging from 300 to 400 miles.
# d. The weight of an apple from a basket, weighing between 100 and 200 grams.

# Applications in Machine Learning and Data Science:
# a. Random Initialization:
#    Used in algorithms like neural networks and k-means to ensure all initial values have equal chance.
# b. Sampling:
#    Useful for selecting representative subsets from balanced datasets.
# c. Data Augmentation:
#    Generate synthetic data points within a defined range using uniform distribution.
# d. Hyperparameter Tuning:
#    Uniform priors allow random search over hyperparameter space.

# ---------------------------------------------------------

# Log-Normal Distribution
# A log-normal distribution is a continuous, heavy-tailed probability distribution 
# of a random variable whose logarithm is normally distributed.

# Examples:
# - Length of comments on internet forums
# - User dwell time on online articles
# - Length of chess games
# - Income of 97–99% of the population (log-normally distributed)

# This is a skewed distribution.

# ---------------------------------------------------------

# Pareto Distribution
# The Pareto distribution models the distribution of wealth, income, and other variables 
# that follow a power-law behavior.

# What is Power Law?
# A power law is a functional relationship between two variables, where one is proportional 
# to a power of the other: y = k * x^a

# Examples:
# - Size of human settlements
# - File size distribution in internet traffic (TCP)

# ---------------------------------------------------------
# How to Detect Pareto Distribution: Log-Log Plot
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
alpha = 3
xm = 1

# Generate x values
x = np.linspace(0.1, 10, 1000)

# Calculate Pareto y values
y = alpha * (xm**alpha) / (x**(alpha + 1))

# Plot log-log
plt.plot(np.log(x), np.log(y))
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Pareto Distribution (Log-Log Plot)')
plt.show()

# ---------------------------------------------------------
# QQ Plot to Validate Pareto Distribution Fit
import scipy.stats as stats
import statsmodels.api as sm

# Generate sample data
x = np.linspace(1, 10, 1000)

# Fit Pareto distribution
params = stats.pareto.fit(x, floc=0)

# Create Pareto distribution with fitted parameters
dist = stats.pareto(b=params[0], scale=params[2])

# Generate QQ plot
fig = sm.qqplot(x, dist=dist, line='45')
plt.title('QQ Plot of Pareto Distribution with Pareto Fit')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()
