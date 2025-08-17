# ================================
# Bayes' Theorem in Probability
# ================================
# Bayes' Theorem is a rule in probability that helps us update 
# the probability of an event (hypothesis) when we get new evidence.
#
# Formula:
#     P(A | B) = [ P(A) * P(B | A) ] / P(B)
#
# Where:
# - P(A): Prior probability of event A (before seeing evidence)
# - P(B | A): Likelihood (probability of observing B given A is true)
# - P(B): Marginal probability of B (total probability of evidence)
# - P(A | B): Posterior probability (updated probability of A after seeing B)
#
# -------------------------------
# Derivation Intuition
# -------------------------------
# From conditional probability:
#     P(A | B) = P(A ∩ B) / P(B)
#     P(B | A) = P(A ∩ B) / P(A)
#
# Rearranging:
#     P(A ∩ B) = P(A) * P(B | A)
#
# Substitute into first equation:
#     P(A | B) = [ P(A) * P(B | A) ] / P(B)
#
# -------------------------------
# Usage in Machine Learning
# -------------------------------
# - Naive Bayes Classifier (spam detection, sentiment analysis, etc.)
# - Medical diagnosis (disease probability given test results)
# - Fraud detection (probability of fraud given a transaction pattern)
# - Bayesian inference (updating beliefs with new data)
#
# -------------------------------
# Example Problem
# -------------------------------
# A medical test detects a disease:
# - P(Disease) = 0.01 (1% people have disease)
# - P(Positive | Disease) = 0.99 (99% sensitivity)
# - P(Positive | No Disease) = 0.05 (5% false positive rate)
#
# Question: What is the probability that a person has the disease 
#           given that their test result is positive?
#
# Using Bayes:
#   P(Disease | Positive) = [ P(Disease) * P(Positive | Disease) ] 
#                           / P(Positive)
#
#   where P(Positive) = P(Disease)*P(Positive|Disease) + P(No Disease)*P(Positive|No Disease)
#
# -------------------------------
# Python Code Example
# -------------------------------

# Probabilities
P_disease = 0.01
P_no_disease = 1 - P_disease
P_positive_given_disease = 0.99
P_positive_given_no_disease = 0.05

# Total probability of positive test
P_positive = (P_disease * P_positive_given_disease) + \
             (P_no_disease * P_positive_given_no_disease)

# Apply Bayes' Theorem
P_disease_given_positive = (P_disease * P_positive_given_disease) / P_positive

print("Probability of having the disease given a positive test result:", 
      round(P_disease_given_positive, 4))
# Output: ~0.166 (16.6%)
#
# Meaning: Even if the test is positive, the chance of actually having 
# the disease is only 16.6%, because the disease is rare.
