# =====================================================================
# What is Probability Distribution of a Random Variable?
# =====================================================================

# A probability distribution is the set of all possible outcomes 
# of a random variable along with their corresponding probability values.
#
# We will first cover this topic by looking at it from the 
# perspective of discrete random variables.
#
# In simple words:
# - Random Variable → A function that assigns a number to each outcome
# - Probability Distribution → Tells us how likely each outcome is

# =====================================================================
# Example 1: Tossing a Coin
# =====================================================================
# Random Variable (X): 
#   X = 1 if Head comes
#   X = 0 if Tail comes
#
# Sample Space: {Head, Tail}
# Random Variable Values: {0, 1}
#
# Probability Distribution:
#   P(X=1) = 0.5
#   P(X=0) = 0.5
#
# Meaning → The probability of getting Head or Tail is equal (50%-50%).


# =====================================================================
# Example 2: Rolling a Single Die
# =====================================================================
# Sample Space: {1, 2, 3, 4, 5, 6}
# Random Variable (X): The number that appears on the die
#
# Random Variable Values: {1, 2, 3, 4, 5, 6}
#
# Probability Distribution:
#   P(X=k) = 1/6 for each k in {1,2,3,4,5,6}
#
# Meaning → Each face of the die has an equal chance of 1/6.


# =====================================================================
# Example 3: Rolling Two Dice
# =====================================================================
# Sample Space: {(1,1), (1,2), ..., (6,6)}  → total 36 outcomes
#
# Random Variable (X): The sum of the numbers on the two dice
#
# Possible Values of X: {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
#
# Probability Distribution:
#   P(X=2)  = 1/36   → only (1,1)
#   P(X=3)  = 2/36   → (1,2), (2,1)
#   P(X=4)  = 3/36   → (1,3), (2,2), (3,1)
#   P(X=5)  = 4/36   → (1,4), (2,3), (3,2), (4,1)
#   P(X=6)  = 5/36   → (1,5), (2,4), (3,3), (4,2), (5,1)
#   P(X=7)  = 6/36   → (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
#   P(X=8)  = 5/36   → (2,6), (3,5), (4,4), (5,3), (6,2)
#   P(X=9)  = 4/36   → (3,6), (4,5), (5,4), (6,3)
#   P(X=10) = 3/36   → (4,6), (5,5), (6,4)
#   P(X=11) = 2/36   → (5,6), (6,5)
#   P(X=12) = 1/36   → (6,6)
#
# Meaning → The probability of getting sums is not uniform.
# Example: Getting a 7 is the most likely (6/36 = 1/6),
# while getting 2 or 12 is the least likely (1/36).

# =====================================================================
# Summary
# =====================================================================
# - Probability Distribution describes how probabilities are 
#   assigned to each value of a random variable.
# - For discrete random variables, it is given in terms of a 
#   probability mass function (PMF).
# - Examples (coin, die, two dice) help understand how probabilities
#   are distributed across outcomes.
