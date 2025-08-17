# -----------------------------
# What is Marginal Probability?
# -----------------------------
# - Marginal probability is the probability of a single event occurring,
#   regardless of the outcome of other random variables.
# - It is also called:
#     1. Simple Probability
#     2. Unconditional Probability
#
# Example:
#   Let X = Passenger Class (Pclass)
#   Let Y = Survival Status (Survived)
#
# The marginal probability of X = 1 (first class) is the probability
# that a passenger is in 1st class, regardless of whether they survived.
# The marginal probability of Y = 1 (survived) is the probability
# that a passenger survived, regardless of their class.
#
# -----------------------------------
# Example with Titanic Dataset (pandas)
# -----------------------------------
import pandas as pd
import seaborn as sns

# Load Titanic dataset
df = sns.load_dataset('titanic')

# Drop missing values for clean calculation
df = df[['class', 'survived']].dropna()

# Marginal probability of survival (P(Y=1))
marginal_survival = df['survived'].value_counts(normalize=True)
print("Marginal Probability of Survival:\n", marginal_survival)

# Marginal probability of passenger class (P(X))
marginal_class = df['class'].value_counts(normalize=True)
print("\nMarginal Probability of Passenger Class:\n", marginal_class)


# -----------------------------
# What is Marginal Distribution?
# -----------------------------
# - A marginal probability distribution shows probabilities of a single
#   random variable, ignoring (marginalizing over) others.
# - Example: Distribution of Pclass (ignoring survival).
#
# Example with Titanic:
marginal_dist_class = df['class'].value_counts(normalize=True)
print("\nMarginal Distribution of Pclass:\n", marginal_dist_class)

marginal_dist_survival = df['survived'].value_counts(normalize=True)
print("\nMarginal Distribution of Survival:\n", marginal_dist_survival)
