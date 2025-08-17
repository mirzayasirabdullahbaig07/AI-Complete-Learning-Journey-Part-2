# ============================================================
# FIVE MOST IMPORTANT TERMINOLOGIES IN PROBABILITY
# ============================================================

# 1. RANDOM EXPERIMENT
# A random experiment is an action or process that leads to 
# one of several possible outcomes, and it is not possible 
# to predict the exact outcome in advance.
# Conditions:
#   - It has more than one possible outcome.
#   - The exact outcome cannot be predicted in advance.
#
# Example:
# Rolling a die → outcomes can be 1, 2, 3, 4, 5, or 6.
# Tossing a coin → outcomes can be Head or Tail.
# Titanic dataset example → whether a passenger survived or not.

# ------------------------------------------------------------

# 2. TRIAL
# A trial refers to a single execution of a random experiment.
# Each trial produces exactly one outcome.
#
# Example:
# Rolling a die once is a trial.
# Tossing a coin once is a trial.
# Checking survival of one Titanic passenger is a trial.

# ------------------------------------------------------------

# 3. OUTCOME
# An outcome is a single possible result of a trial.
#
# Example:
# Rolling a die → outcome can be "4".
# Tossing a coin → outcome can be "Head".
# Titanic dataset → outcome can be "Passenger survived".

# ------------------------------------------------------------

# 4. SAMPLE SPACE
# The sample space of a random experiment is the set of all 
# possible outcomes that can occur. Usually, one random 
# experiment has one sample space.
#
# Example:
# Rolling a die → {1, 2, 3, 4, 5, 6}
# Tossing a coin twice → {HH, HT, TH, TT}
# Titanic dataset → {Survived, Not Survived}

# ------------------------------------------------------------

# 5. EVENT
# An event is a specific subset of outcomes from a sample 
# space. An event can include one or more outcomes.
#
# Example:
# Rolling a die:
#   Event "Getting an even number" → {2, 4, 6}
# Tossing a coin twice:
#   Event "Getting exactly one Head" → {HT, TH}
# Titanic dataset:
#   Event "Selecting a female passenger who survived" → 
#   Subset of sample space filtered by gender and survival.
