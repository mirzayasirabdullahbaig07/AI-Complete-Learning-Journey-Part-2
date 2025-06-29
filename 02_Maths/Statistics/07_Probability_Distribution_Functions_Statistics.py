# What is a Probability Distribution Function?
# It is one of the most important concepts in the world of statistics and probability.

# What are Algebraic Variables?
# In algebra, a variable (like x) represents unknown values.
# Example: x + 5 = 10. Find x. The value of x is 5.

# What are Random Variables in Statistics and Probability?
# A random variable is a variable that takes on a set of possible values from a random experiment.

# What is a Random Experiment?
# A random experiment is an experiment where the outcome is uncertain.
# Example 1: Flipping a coin – result can be Head or Tail, and it is random.
# Example 2: Rolling a dice – the result can be 1, 2, 3, 4, 5, or 6, randomly.
# In statistics, random variables are often represented using capital letters like X, Y, or Z.

# Example:
# X = {1, 0}
# Y = {1, 2, 3, 4, 5, 6}  # This is the sample space of a random experiment.
# Random variables store multiple values.

# The possible outcomes from X and Y, such as {1, 0} and {1,2,3,4,5,6}, are called sample spaces in probability.

# Types of Random Variables:
# 1 - Discrete Random Variables:
#     These variables take on finite, distinct values (e.g., 1, 2, 3). They do not take on fractional values like 1.2.
# 2 - Continuous Random Variables:
#     These variables can take on any value within a given range (e.g., height, weight, temperature).

# What is a Probability Distribution?
# A probability distribution is a list of all the possible values of a random variable with their corresponding probabilities.

# Example 1: Coin Flip
# Outcome: 0 or 1
# Probability: P(0) = 1/2, P(1) = 1/2

# Example 2: Rolling a Dice
# Probability for each value (1 to 6): 1/6

# Now consider the case of rolling 2 dice. Let's construct a probability distribution:
# Minimum value = 2 (1+1), Maximum value = 12 (6+6)
# You can create a 6x6 grid of outcomes and sum the results.

# Probability distribution of sums when rolling 2 dice:
# P(2)  = 1/36
# P(3)  = 2/36
# P(4)  = 3/36
# P(5)  = 4/36
# P(6)  = 5/36
# P(7)  = 6/36
# P(8)  = 5/36
# P(9)  = 4/36
# P(10) = 3/36
# P(11) = 2/36
# P(12) = 1/36

# This tabular form is fine for small datasets.
# But what if we deal with very large sample spaces?

# For example: height of people, or rolling 10 dice together
# In such cases, creating a table is tedious or even impossible.

# Solution:
# Instead of a table, we use a mathematical function to model the relationship between outcomes and their probabilities.

# This approach is called a Probability Distribution Function (PDF).

# Types of Probability Distribution Functions:
# 1. Discrete Probability Distribution Functions
# 2. Continuous Probability Distribution Functions

# Common Probability Distributions include:
# - Normal Distribution
# - Uniform Distribution
# - Beta Distribution
# - Bernoulli Distribution
# - Binomial Distribution
# - Exponential Distribution
# - Log-normal Distribution
# These distributions are widely used in statistics and data science.

# Why is PDF Important?
# 1. It gives insight into the shape or nature of the data distribution.
# 2. If data follows a known distribution, we can make strong inferences based on that knowledge.

# Parameters in PDFs:
# Parameters are numerical values that define the shape, location, and scale of a distribution.
# Each type of distribution has its own set of parameters. Understanding them is essential for statistical analysis.

# Another Simple Definition of a PDF:
# A Probability Distribution Function is a mathematical function that describes the probability of different outcomes for a random variable.

# There are 3 main types of probability distribution functions:
# 1. Probability Mass Function (PMF)
# 2. Probability Density Function (PDF)
# 3. Cumulative Distribution Function (CDF)

# 1. Probability Mass Function (PMF):
# PMF is used for discrete random variables.
# It assigns a probability to each possible value of the variable.

# Conditions for a valid PMF:
# 1. The probability for each value must be non-negative.
# 2. The sum of all probabilities must equal 1.

# Example of PMF using simulation (rolling a single dice 10,000 times):
import pandas as pd
import random

L = []
for i in range(10000):
    L.append(random.randint(1, 6))
    
# Display the first 5 values
L[:5]

# Compute PMF
s = (pd.Series(L).value_counts() / pd.Series(L).value_counts().sum()).sort_index()

# Plot the PMF
s.plot(kind='bar')

# Now simulate for two dice
L = []
for i in range(10000):
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    L.append(a + b)

# Check total entries
len(L)

# Compute PMF
s = (pd.Series(L).value_counts() / pd.Series(L).value_counts().sum()).sort_index()

# Plot the PMF
s.plot(kind='bar')

# Cumulative Distribution Function (CDF):
# The CDF, denoted F(x), describes the probability that a random variable X will take a value less than or equal to x.
# Mathematically: F(x) = P(X ≤ x)

# In PMF, f(x) gives probability for an exact value.
# In CDF, F(x) gives cumulative probability up to and including x.

# Example: Dice CDF
# F(1) = 1/6, F(2) = 2/6, F(3) = 3/6, F(4) = 4/6, and so on.

# Let's calculate and plot CDF:
import numpy as np

# Compute cumulative sum
np.cumsum(s)

# Plot the CDF
np.cumsum(s).plot(kind='bar')
# ------------------------------
# PDF - Probability Density Function
# ------------------------------

# A Probability Density Function (PDF) is a mathematical function that describes the probability distribution of a continuous random variable.

# Difference between Mass Function and Density Function:
# - In probability mass function (PMF), y-axis represents **actual probabilities** for discrete variables.
# - In PDF, y-axis represents **probability density**, not the actual probability.
# - The x-axis in PDF spans continuous values (potentially infinite range).

# Why use probability density and not exact probability?
# For continuous values (like marks or measurements), the probability of any **exact value** (e.g., exactly 9.878) is almost zero.
# Instead, we find the probability in a **range**, e.g., between 9 and 10, which is represented by the **area under the curve**.

# What does the area under the PDF curve represent?
# - The **area** under the curve between two points gives the **probability** that the variable lies within that range.
# - The total area under the entire curve is always **1** (100%).

# How do we calculate the PDF?
# We use **density estimation** based on data:
# 1. Parametric density estimation
# 2. Non-parametric density estimation

# --------------------------------
# Parametric Density Estimation
# --------------------------------

# This method assumes the data follows a known distribution (like normal, exponential, Poisson).
# We estimate parameters like **mean (μ)** and **standard deviation (σ)**, then fit the curve.

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import normal
from scipy.stats import norm
import seaborn as sns

# Generate normal distributed sample data
sample = normal(loc=50, scale=10, size=1000)  # mean = 50, std = 10

# Step 1: Plot histogram to understand distribution
plt.hist(sample, bins=10)
plt.title("Histogram of Sample Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# Step 2: Calculate sample statistics
sample_mean = sample.mean()
sample_std = sample.std()

# Step 3: Fit a normal distribution using these parameters
dist = norm(sample_mean, sample_std)
values = np.linspace(sample.min(), sample.max(), 100)
pdf = [dist.pdf(val) for val in values]

# Step 4: Plot histogram with PDF curve
plt.hist(sample, bins=10, density=True, alpha=0.6, label='Histogram')
plt.plot(values, pdf, color='red', label='PDF')
plt.title("Parametric PDF Fit")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

# Using Seaborn for simpler visualization
sns.distplot(sample, kde=True)
plt.title("PDF using Seaborn")
plt.show()

# Why is this called 'parametric'?
# Because it depends on known parameters like mean and standard deviation.

# -----------------------------------------------------
# Non-Parametric Density Estimation (KDE - Kernel)
# -----------------------------------------------------

# In many cases, the data doesn't follow a known distribution.
# Non-parametric methods like **Kernel Density Estimation (KDE)** make no assumptions.

# KDE uses a kernel (usually Gaussian) to estimate density for each point.
# - Bandwidth controls the smoothness.
# - Smaller bandwidth → sharper spikes.
# - Larger bandwidth → smoother curve.

# Generate sample with no clear single distribution (2 peaks)
sample1 = normal(loc=20, scale=10, size=300)
sample2 = normal(loc=40, scale=5, size=700)
sample = np.hstack((sample1, sample2))

# Plot histogram to view distribution
plt.hist(sample, bins=50)
plt.title("Mixture Histogram")
plt.show()

# Fit KDE model using sklearn
from sklearn.neighbors import KernelDensity

sample = sample.reshape((len(sample), 1))  # reshape to 2D array for sklearn
model = KernelDensity(bandwidth=3, kernel='gaussian')
model.fit(sample)

# Evaluate KDE model
values = np.linspace(sample.min(), sample.max(), 1000).reshape(-1, 1)
log_density = model.score_samples(values)
density = np.exp(log_density)

# Plot histogram and KDE curve
plt.hist(sample, bins=50, density=True, alpha=0.5, label='Histogram')
plt.plot(values[:, 0], density, color='red', label='KDE')
plt.title("Non-Parametric Density Estimation (KDE)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

# KDE using Seaborn (simpler and automatic bandwidth handling)
sns.kdeplot(sample.reshape(1000))
plt.title("KDE using Seaborn")
plt.show()

# Summary:

# Parametric Estimation:
# - Assumes distribution type (Normal, Exponential, etc.)
# - Needs parameters like mean and std
# - Fast and interpretable

# Non-Parametric Estimation:
# - No assumption about underlying distribution
# - Flexible for real-world data
# - Slower, but more accurate for complex distributions



# How to Use PDF and CDF in Data Science

# --------------------------
# Introduction
# --------------------------

# In data science, understanding the distribution of data is crucial for making informed decisions.
# Two important tools for analyzing data distributions are:
# - PDF (Probability Density Function)
# - CDF (Cumulative Distribution Function)

# These tools help us in:
# 1. Understanding the probability distribution of features.
# 2. Performing feature selection by identifying which features help differentiate between classes.

# --------------------------
# Use Case: Feature Selection
# --------------------------

# In a dataset, some features are more helpful in predicting the target variable than others.
# Feature selection techniques help isolate such valuable features.

# One such approach is to visualize the PDF of features to see how well they separate different classes.

# --------------------------
# Dataset: Iris
# --------------------------

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
df.head()

# Plotting the PDF (using KDE plots) for different features to analyze their distribution
sns.kdeplot(data=df, x='sepal_length', hue='species')
plt.title("PDF of Sepal Length")
plt.show()

sns.kdeplot(data=df, x='sepal_width', hue='species')
plt.title("PDF of Sepal Width")
plt.show()

sns.kdeplot(data=df, x='petal_length', hue='species')
plt.title("PDF of Petal Length")
plt.show()

sns.kdeplot(data=df, x='petal_width', hue='species')
plt.title("PDF of Petal Width")
plt.show()

# --------------------------
# Feature Selection Using PDF
# --------------------------

# Suppose someone asks: "Select the two most useful features from the four above."
# We use the PDF plots to evaluate this.

# Key Observation:
# - Petal Length and Petal Width show clear separation between species.
#   For example:
#     - petal_length < 2.3 => likely 'setosa'
#     - 2.3 < petal_length < 5 => likely 'versicolor'
#     - petal_length > 5 => likely 'virginica'

# Hence, petal_length and petal_width are the most informative features for classifying species.

# --------------------------
# Using CDF (Cumulative Distribution Function)
# --------------------------

# CDF gives the cumulative probability for values of a variable.
# It's helpful in understanding how data accumulates and in comparing distributions.

# PDF vs CDF:
# - PDF shows how dense the data is at different points.
# - CDF shows cumulative probability up to each point.

# Plotting CDF (ECDF in seaborn)

sns.kdeplot(data=df, x='petal_width', hue='species')
plt.title("PDF of Petal Width")
plt.show()

sns.ecdfplot(data=df, x='petal_width', hue='species')
plt.title("CDF of Petal Width")
plt.show()

# --------------------------
# Another Example: Titanic Dataset
# --------------------------

# Load Titanic dataset (replace with correct path or URL)
titanic = pd.read_csv("link/to/titanic.csv")
titanic.head()

# Plot the PDF of Age grouped by Survival status
sns.kdeplot(data=titanic, x='Age', hue='Survived')
plt.title("PDF of Age by Survival Status")
plt.show()

# --------------------------
# 2D KDE Plot (Joint Distribution)
# --------------------------

# We can also visualize the joint distribution of two features using 2D KDE (PDF in 2D)
sns.jointplot(data=df, x='petal_length', y='sepal_width', kind='kde', fill=True, cbar=True)
# Darker regions indicate higher density of data points
