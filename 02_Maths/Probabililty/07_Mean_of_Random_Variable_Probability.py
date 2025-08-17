# What is the Mean (Expected Value) of a Random Variable?
# -------------------------------------------------------
# The mean of a random variable, often called the Expected Value (E[X]),
# represents the long-run average outcome of a random process repeated many times.
# 
# In simple words:
# If you repeat the experiment (like rolling a die) thousands of times,
# the average result you get will approach the expected value.
#
# Mathematically:
#   E[X] = Σ [ x * P(x) ]
#
# Where:
# - x = possible outcome
# - P(x) = probability of that outcome

# Example 1: Rolling a fair die
# ------------------------------
# Possible outcomes (x): {1, 2, 3, 4, 5, 6}
# Probability of each outcome: 1/6 (since die is fair)
#
# E[X] = (1 * 1/6) + (2 * 1/6) + (3 * 1/6) + (4 * 1/6) + (5 * 1/6) + (6 * 1/6)
#      = (1+2+3+4+5+6) / 6
#      = 21 / 6
#      = 3.5
#
# So, the expected value (mean) of rolling a die = 3.5
# Notice that 3.5 is not a possible outcome of the die, but it is the *average*
# over a very large number of rolls.

# Python Code Simulation
# -----------------------
import random
import numpy as np

outcomes = []
for i in range(10000):   # simulate rolling a die 10,000 times
    outcomes.append(random.randint(1, 6))

print("Simulated Mean:", np.mean(outcomes))
print("Theoretical Mean:", 3.5)
