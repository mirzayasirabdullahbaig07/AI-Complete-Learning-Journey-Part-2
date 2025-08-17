# What is Joint Probability?
# -----------------------------------------------------------
# Joint probability refers to the probability of two events happening together.
# If we have two random variables X and Y, the joint probability is denoted as:
#       P(X = x, Y = y)
# This represents the probability that:
#   - X takes a specific value x, AND
#   - Y takes a specific value y simultaneously.

# Example:
# -----------------------------------------------------------
# Let's take the Titanic dataset as an example.
# X = Passenger Class (Pclass)
# Y = Survival Status (Survived)
# The joint probability answers questions like:
#   "What is the probability that a passenger was in 1st class AND survived?"

# In Python, we can use pandas crosstab to compute this:

import pandas as pd

# Example Titanic dataset snippet
data = {
    'Survived': [1, 0, 1, 0, 1, 0, 0, 1],
    'Pclass':   [1, 1, 2, 3, 3, 2, 1, 3]
}
df = pd.DataFrame(data)

# Frequency counts (how many times each combination occurs)
print(pd.crosstab(df['Survived'], df['Pclass']))

# Joint probability (each cell divided by total)
print(pd.crosstab(df['Survived'], df['Pclass'], normalize='all', margins=True))

# Conditional probability by column (P(Survived | Pclass))
print(pd.crosstab(df['Survived'], df['Pclass'], normalize='columns'))

# -----------------------------------------------------------
# What are Joint Probability Contributions?
# -----------------------------------------------------------
# Joint probability contribution refers to the share of probability
# each (X, Y) combination contributes to the overall probability distribution.
# For example:
#   - P(Survived = 1, Pclass = 1) might be 0.20
#   - P(Survived = 0, Pclass = 1) might be 0.10
# Together, they explain how survival depends on class.

# Titanic Example:
# -----------------------------------------------------------
# Let's say in Titanic dataset we found:
#   P(Survived = 1, Pclass = 1) = 0.15  (15% of total passengers)
#   P(Survived = 0, Pclass = 1) = 0.10  (10% of total passengers)
# Contribution Interpretation:
#   - Out of the whole population, 15% were "1st class & survived".
#   - Out of the whole population, 10% were "1st class & did not survive".
# These contributions help us understand how each group
# affects the overall survival probability distribution.

# In short:
# -----------------------------------------------------------
# - Joint probability = probability of two events happening together.
# - Joint probability contributions = each cell's contribution
#   to the total probability distribution.
