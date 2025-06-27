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
