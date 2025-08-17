# What is Conditional Probability?
# Conditional probability is the measure of the probability of an event (A) occurring 
# given that another event (B) has already occurred.
# It is denoted as:  P(A|B)
#
# Mathematically:
# P(A|B) = P(A ∩ B) / P(B)
# where:
# - P(A ∩ B) = probability that both A and B occur
# - P(B) = probability that event B occurs

# ------------------------------
# Example 1: Tossing 3 unbiased coins
# Question: What is the conditional probability that at least 2 coins show heads,
#           given that at least 1 coin shows heads?
#
# Step 1: Sample space for 3 coins = 8 outcomes
#         {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}
#
# Step 2: Event B = at least 1 head
#         B = {HHH, HHT, HTH, THH, HTT, THT, TTH}
#         => P(B) = 7/8
#
# Step 3: Event A = at least 2 heads
#         A = {HHH, HHT, HTH, THH}
#
# Step 4: A ∩ B = outcomes where both A and B happen
#         = {HHH, HHT, HTH, THH} (same as A, since all these contain at least 1 head)
#         => P(A ∩ B) = 4/8
#
# Step 5: Conditional Probability
#         P(A|B) = P(A ∩ B) / P(B)
#                 = (4/8) / (7/8)
#                 = 4/7
#
# Final Answer: P(A|B) = 4/7

# ------------------------------
# Example 2: Rolling 2 fair dice
# Question: What is the conditional probability that the sum is 7,
#           given that the first die shows an odd number?
#
# Step 1: Sample space of 2 dice = 36 outcomes
#
# Step 2: Event B = first die shows odd number
#         Odd numbers on first die = {1, 3, 5}
#         For each choice, second die can be 1–6
#         => total outcomes in B = 3 * 6 = 18
#         => P(B) = 18/36 = 1/2
#
# Step 3: Event A = sum of dice = 7
#         Possible pairs: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1)
#         => total outcomes in A = 6
#         => P(A) = 6/36 = 1/6
#
# Step 4: A ∩ B = cases where sum = 7 AND first die odd
#         (1,6), (3,4), (5,2)
#         => total outcomes = 3
#         => P(A ∩ B) = 3/36 = 1/12
#
# Step 5: Conditional Probability
#         P(A|B) = P(A ∩ B) / P(B)
#                 = (1/12) / (1/2)
#                 = 1/6
#
# Final Answer: P(A|B) = 1/6

# ------------------------------
# Intuition behind Conditional Probability Formula:
# - When we say P(A|B), it means "probability of A given that B has happened".
# - So, we shrink our universe to only those outcomes where B happens.
# - The denominator (P(B)) tells us the probability of being inside this new universe.
# - The numerator (P(A ∩ B)) tells us how many of these outcomes also satisfy A.
# - Dividing them gives us the proportion of cases where A occurs inside the world of B.
#
# In summary:
# Conditional probability helps us measure how likely A is,
# once we already know that B has happened.
