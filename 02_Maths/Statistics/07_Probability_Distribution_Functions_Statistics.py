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
