# ============================================================
# TYPES OF PROBABILITY
# ============================================================

# In probability theory, there are 2 main types of probability:
#   1. Empirical Probability (Experimental Probability)
#   2. Theoretical Probability (Classical Probability)

# ------------------------------------------------------------
# 1. EMPIRICAL PROBABILITY
# ------------------------------------------------------------
# Empirical probability (also called Experimental Probability) 
# is based on actual observations or experiments.
#
# Formula:
#   Empirical Probability of Event A = 
#       (Number of times Event A occurs) / (Total number of trials)
#
# Key Idea:
#   - Instead of assuming equal likelihood, we rely on real data.
#   - The more trials we perform, the closer empirical probability 
#     gets to the theoretical probability.

# Example 1: Coin Toss
# Suppose we toss a fair coin 100 times.
#   - Heads appeared 55 times
#   - Tails appeared 45 times
# Empirical probability of getting a Head:
#   = 55 / 100 
#   = 0.55 (or 55%)

# Example 2: Marbles in a Bag
# Bag contains 50 marbles in total:
#   - 20 red, 15 blue, 15 green
# We draw marbles 200 times (with replacement), and record:
#   - Red marbles = 80 times
#   - Blue marbles = 70 times
#   - Green marbles = 50 times
# Empirical probability of getting a Red marble:
#   = 80 / 200
#   = 0.40 (or 40%)

# ------------------------------------------------------------
# 2. THEORETICAL PROBABILITY
# ------------------------------------------------------------
# Theoretical (Classical) Probability is used when all outcomes 
# in a sample space are equally likely to occur.
#
# Formula:
#   Theoretical Probability of Event A = 
#       (Number of favourable outcomes) / (Total number of outcomes)
#
# Key Idea:
#   - This is based on mathematical reasoning, not experiment.
#   - Works well in controlled situations like dice, coins, or cards.

# Example A: Tossing a coin 3 times
# Sample space size = 2^3 = 8 outcomes
# All possible outcomes: {HHH, HHT, HTH, THH, HTT, THT, TTH, TTT}
# Event: Getting exactly 2 heads
# Favourable outcomes = {HHT, HTH, THH} = 3
# Probability = 3 / 8 = 0.375 (or 37.5%)

# Example B: Rolling 2 dice
# Total possible outcomes = 6 * 6 = 36
# Event: Getting a sum of 7
# Favourable outcomes = {(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)} = 6
# Probability = 6 / 36 = 1 / 6 ≈ 0.167 (or 16.7%)

# ============================================================
# SUMMARY
# ============================================================
# - Empirical Probability → based on observed data or experiments.
# - Theoretical Probability → based on equally likely outcomes.
# - With a large number of trials, empirical probability tends 
#   to approach theoretical probability (Law of Large Numbers).
