# What is a Random Variable?
# A random variable is NOT like a normal variable that stores values. 
# Instead, it is a FUNCTION that maps outcomes of a random process 
# (sample space) to real numbers. 
# This is one of the most confusing concepts at first, but it gets clear with examples.

# In probability theory:
# - A random variable takes an outcome from the sample space (input)
# - And assigns a real number to it (output)

# INPUT: An outcome from a random process (e.g., rolling a die → {1, 2, 3, 4, 5, 6})
# OUTPUT: A real number assigned to each outcome (e.g., 1 → 1, 2 → 2, etc.)

# The way outcomes are mapped to numbers depends on how we define the random variable.
# This choice depends on what aspect of the random process we are studying.

# --------------------------------------------------------
# Example: Rolling a fair die 🎲
# Sample Space (S) = {1, 2, 3, 4, 5, 6}
# Random Variable X = "the number that appears on the die"
#   Outcome: Die shows 4 → X = 4
#   Outcome: Die shows 6 → X = 6
# Here, X is a random variable because its value depends on chance.

# --------------------------------------------------------
# Types of Random Variables:
# 1) Discrete Random Variable:
#    - Takes COUNTABLE values (finite or countably infinite)
#    - Example: Rolling a die → {1, 2, 3, 4, 5, 6}
#    - Example: Number of students present in a class

# 2) Continuous Random Variable:
#    - Takes values from an INTERVAL of real numbers (uncountable)
#    - Example: Height of students (can be 160.2 cm, 170.55 cm, ...)
#    - Example: Time taken to run 100m (12.01s, 12.015s, ...)

# --------------------------------------------------------
# In short:
# - Random variable = a function that assigns numbers to outcomes
# - Discrete = countable outcomes
# - Continuous = uncountable outcomes
