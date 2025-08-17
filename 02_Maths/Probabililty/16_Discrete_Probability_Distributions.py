# Discrete Probability Distribution 
# -------------------------------------------------
# Definition:
# A Discrete Probability Distribution gives the probabilities of outcomes 
# for a discrete random variable (a variable that takes only countable values like 0, 1, 2, ...).
#
# It tells us how likely each outcome is.
#
# Examples:
#   - Number of heads in coin toss
#   - Number of emails in an hour
#   - Rolling a die
#
# -------------------------------------------------
# Conditions:
# 1) Probability must be between 0 and 1 → 0 ≤ P(X=x) ≤ 1
# 2) Total probability = 1 → Σ P(X=x) = 1
#
# -------------------------------------------------
# Example – Tossing 2 coins:
#
# Sample Space = {HH, HT, TH, TT}
# Let X = number of Tails
#
#  X (no. of tails)   Outcomes      P(X=x)
#  ----------------------------------------
#       0             {HH}          1/4
#       1             {HT, TH}      2/4
#       2             {TT}          1/4
#
# Total Probability = 1/4 + 2/4 + 1/4 = 1
#
# -------------------------------------------------
# Important Formulas:
#
# PMF (Probability Mass Function):
#       f(x) = P(X=x)
#   Example: Tossing 2 coins → P(X=1) = 2/4
#
# CDF (Cumulative Distribution Function):
#       F(x) = P(X ≤ x)
#   Example: Rolling a 4-sided die:
#       P(1 < X ≤ 3) = F(3) – F(1) = 0.7 – 0.2 = 0.5
#
# Mean (Expected Value):
#       E[X] = Σ (x · P(X=x))
#
# Variance:
#       Var[X] = Σ ( (x – μ)² · P(X=x) )
#
# -------------------------------------------------
# Steps to Find a Discrete Probability Distribution:
#
# Step 1: Write the sample space
# Step 2: Define the random variable X
# Step 3: Assign probabilities for each value of X
# Step 4: Make a probability distribution table
#
# -------------------------------------------------



# ================================================================
# Types of Discrete Probability Distributions
# ================================================================
# In discrete probability distributions, the random variable takes 
# distinct values (like 0,1,2,…). 
# Some common types are:
# 1. Bernoulli Distribution
# 2. Binomial Distribution
# 3. Poisson Distribution
# 4. Geometric Distribution
# ================================================================


# ----------------------------------------------------------------
# 1. Bernoulli Distribution
# ----------------------------------------------------------------
# Definition:
# - A random experiment with only TWO possible outcomes:
#     Success (1) with probability p
#     Failure (0) with probability 1-p
#
# Probability Mass Function (PMF):
#   P(X = x) = p      if x = 1
#               1 - p if x = 0
#
# Example:
# - Toss a coin once:
#   Let Success = Head → p = 0.5
#   Failure = Tail → 1-p = 0.5
#
#   So,
#   P(X=1) = 0.5, P(X=0) = 0.5


# ----------------------------------------------------------------
# 2. Binomial Distribution
# ----------------------------------------------------------------
# Definition:
# - Repeated Bernoulli trials (n times).
# - Counts the number of successes in 'n' independent trials.
# - Each trial has probability of success = p, failure = 1-p.
#
# Probability Mass Function (PMF):
#   P(X = x) = (n choose x) * p^x * (1-p)^(n-x)
#   where (n choose x) = n! / [x! * (n-x)!]
#
# Example:
# - Toss a coin 3 times (n=3, p=0.5)
#   Find probability of getting exactly 2 Heads.
#
#   P(X=2) = (3 choose 2) * (0.5)^2 * (0.5)^1
#          = 3 * 0.25 * 0.5
#          = 0.375


# ----------------------------------------------------------------
# 3. Poisson Distribution
# ----------------------------------------------------------------
# Definition:
# - Describes the probability of a given number of events 
#   happening in a fixed interval of time or space.
# - Controlled by parameter λ (mean number of events).
#
# Probability Mass Function (PMF):
#   P(X = x) = (λ^x * e^(-λ)) / x!
#
# Example:
# - A call center receives on average 5 calls per minute (λ=5).
#   Find probability of receiving exactly 3 calls in a minute.
#
#   P(X=3) = (5^3 * e^(-5)) / 3!
#          = (125 * e^(-5)) / 6
#          ≈ 0.1404


# ----------------------------------------------------------------
# 4. Geometric Distribution
# ----------------------------------------------------------------
# Definition:
# - Models the number of trials until the first success occurs.
# - Probability of success = p, probability of failure = (1-p).
#
# Probability Mass Function (PMF):
#   P(X = x) = (1 - p)^(x-1) * p
#   where X = number of trial in which first success happens.
#
# Example:
# - Toss a coin until first Head appears (p=0.5).
#   Find probability that the first Head appears on the 3rd toss.
#
#   P(X=3) = (1 - 0.5)^(3-1) * 0.5
#          = (0.5)^2 * 0.5
#          = 0.125
