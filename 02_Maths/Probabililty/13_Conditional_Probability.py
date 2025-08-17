# what is marginal probability?
# it is also called simple probability
# it is also called unconditional probability
#
# Marginal probability refers to the probability of an event occurring 
# irrespective of the outcome of some other event. 
#
# When dealing with random variables, the marginal probability of a random variable 
# is simply the probability of that variable taking a certain value, regardless of 
# the values of other variables.
#
# Example:
# Let X be the random variable associated with the passenger class (Pclass) of a Titanic passenger.
# Let Y be the random variable associated with the survival status (Survived) of the passenger.
#
# Then the marginal probability of X = 1 (1st class passenger) is the probability 
# that a randomly selected passenger is in 1st class, regardless of whether they survived or not.
#
# Similarly, the marginal probability of Y = 1 (Survived) is the probability that a 
# passenger survived, regardless of which class they belonged to.
#
# Example of code in Python:

import pandas as pd

# Load Titanic dataset
data = {
    "Pclass": [1, 1, 2, 3, 3, 2, 1, 3],
    "Survived": [1, 0, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(data)

# Marginal probability of Pclass
pclass_probs = df["Pclass"].value_counts(normalize=True)

# Marginal probability of Survived
survival_probs = df["Survived"].value_counts(normalize=True)

print("Marginal Probability of Pclass:\n", pclass_probs)
print("\nMarginal Probability of Survival:\n", survival_probs)


# what is marginal probability distribution?
# It is also called unconditional probability distribution P(A).
#
# A marginal probability distribution describes the probabilities of the values 
# of a single random variable, irrespective of the values of other random variables.
#
# In other words, it gives the distribution of one variable after summing 
# (or integrating) out the other variables.
#
# Example:
# - The marginal probability distribution of Pclass shows how likely each passenger class is 
#   in the dataset (1st, 2nd, 3rd), regardless of survival.
# - The marginal probability distribution of Survived shows the probability of survival (0 or 1), 
#   regardless of class.

# Example in Python:

# Marginal distribution of Pclass
print("\nMarginal Probability Distribution of Pclass:")
print(pclass_probs)

# Marginal distribution of Survived
print("\nMarginal Probability Distribution of Survived:")
print(survival_probs)
