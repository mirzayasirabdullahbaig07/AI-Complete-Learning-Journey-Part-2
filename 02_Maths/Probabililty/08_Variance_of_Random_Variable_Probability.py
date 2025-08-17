# What is the variance of a random variable in terms of probability?
# The variance of a random variable is a measure of how much the possible values 
# of the variable differ (spread out) from the mean (expected value).
# 
# In simple terms:
# - The mean tells us the "average outcome".
# - The variance tells us "how far away" the outcomes are from that average, on average.
#
# Formula (Discrete Random Variable):
# Var(X) = Σ [ (xᵢ - μ)² * P(xᵢ) ]
# where:
#   xᵢ = possible values
#   μ  = mean (expected value)
#   P(xᵢ) = probability of each outcome
#
# Example:
# Rolling a single die
# Possible outcomes: {1, 2, 3, 4, 5, 6}
# Each with equal probability = 1/6
# Mean μ = (1+2+3+4+5+6)/6 = 3.5
# Variance = Σ [ (x - 3.5)² * (1/6) ] for x in {1,...,6}

# Short Python Code Example
import numpy as np

# Define possible outcomes of a fair die
outcomes = np.array([1, 2, 3, 4, 5, 6])

# Probability of each outcome (equal for a fair die)
probabilities = np.array([1/6] * 6)

# Mean (expected value)
mean = np.sum(outcomes * probabilities)

# Variance calculation using the formula
variance = np.sum(((outcomes - mean) ** 2) * probabilities)

print("Mean (Expected Value):", mean)
print("Variance:", variance)
