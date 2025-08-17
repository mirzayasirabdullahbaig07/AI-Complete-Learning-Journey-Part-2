# ======================================================
# Sampling Distribution (Basics)
# ======================================================
# A sampling distribution is the probability distribution 
# of a statistic (like mean or proportion) obtained from 
# repeated random samples of a population.
#
# Why it matters:
# - Helps in inferential statistics (estimating population 
#   from sample).
# - Forms the basis for confidence intervals & hypothesis tests.
#
# Key Terms:
# - Population: Whole group being studied.
# - Sample: Subset of the population.
# - Parameter: Value from population (e.g., μ, σ).
# - Statistic: Value from sample (e.g., x̄, s).
# - Standard Error (SE): Std. deviation of sampling distribution.
# - CLT (Central Limit Theorem): Sample means approach a 
#   normal distribution as n ↑.
#
# ------------------------------------------------------
# Types of Sampling Distributions
# ------------------------------------------------------
# 1. Sampling Distribution of Mean:
#    - Mean of sample means = μ
#    - Std. dev. = σ / √n   (n = sample size)
#
# 2. Sampling Distribution of Proportion:
#    - Sample proportion p̂ = x/n
#
# 3. T-Distribution:
#    - Used when n is small or σ unknown.
#    - Formula: t = (x̄ - μ) / (s / √n)
#
# ------------------------------------------------------
# Example:
# Population mean μ = 13,525, σ = 4,180, n = 100
# Mean of sample means = μ = 13,525
# Std. dev. of sample means = σ / √n = 4180 / 10 = 418
# ------------------------------------------------------



# ======================================================
# Chi-Square Test (χ² Test) – Simplified Guide
# ======================================================

# Definition
# The Chi-Square test is a statistical method used to check
# if there is a relationship (association) between two 
# categorical variables.
#
# It compares observed frequencies (actual data) with
#    expected frequencies (if no relationship existed).

# Example:
#   Variable 1 = Favorite Color
#   Variable 2 = Favorite Ice Cream
#   H0 (Null Hypothesis): No relationship
#   H1 (Alternative Hypothesis): There is a relationship

# ------------------------------------------------------
# Formula
#   χ² = Σ (Oi - Ei)² / Ei
#
# Where:
#   Oi = Observed frequency
#   Ei = Expected frequency

# ------------------------------------------------------
# Steps of Chi-Square Test
# 1. Define Hypothesis:
#    - H0: Variables are independent
#    - H1: Variables are dependent
#
# 2. Collect Data:
#    - Example (Contingency Table: Ice Cream vs Gender):
#         Chocolate  Vanilla  Strawberry
#   Male     20        15        10
#   Female   25        20        30
#
# 3. Calculate Expected Frequency:
#    Ei = (Row Total × Column Total) / Grand Total
#    Example: Male-Chocolate = (45×45)/120 = 16.875
#
# 4. Apply Formula:
#    χ² = Σ (Oi - Ei)² / Ei
#
# 5. Degrees of Freedom:
#    df = (rows - 1) × (columns - 1)
#
# 6. Compare χ² value with Chi-Square Table:
#    - If χ² > critical value → Reject H0
#    - Otherwise → Fail to reject H0
#
# 7. Interpret Results:
#    - p < 0.05 → Significant relationship exists
#    - p > 0.05 → No significant relationship

# ------------------------------------------------------
# Assumptions
# - Observations are independent.
# - Each cell should have at least 5 expected counts.
# - Chi-Square shows association, not causation.

# ------------------------------------------------------
# Types of Chi-Square Tests
# 1. Test of Independence:
#    - Checks if two variables are related.
#    - Example: Gender vs Ice Cream Preference.
#
# 2. Goodness-of-Fit Test:
#    - Checks if data fits a specific distribution.
#    - Example: Is a die fair? (Expected = equal outcomes).

# ------------------------------------------------------
# Applications
# - Market Research (customer preferences)
# - Healthcare (treatment vs outcome)
# - Machine Learning (feature selection)
# - A/B Testing (website version A vs B)
# - NLP (word frequency analysis)
#
# ------------------------------------------------------
# Quick Example (Coin Toss)
# - Flip coin 100 times → 55 heads, 45 tails
# - Expected: 50 heads, 50 tails
# - Use χ² formula → Check if difference is due to chance
# ------------------------------------------------------

# ======================================================
# F-Test in Statistics – Simplified Guide
# ======================================================

# Definition
# The F-test checks whether the variances of two populations
# (or samples) are equal. It is based on the F-distribution.

# ------------------------------------------------------
# F-Statistic Formula
# For samples:
#   F = (s1² / s2²)
#   (where s1² ≥ s2², i.e., always divide larger variance by smaller)
#
# df1 = n1 - 1   → numerator degrees of freedom
# df2 = n2 - 1   → denominator degrees of freedom

# ------------------------------------------------------
# Hypotheses
# 1. Right-tailed (most common):
#    H0: σ1² = σ2²   (variances equal)
#    H1: σ1² > σ2²   (variance 1 greater)
#
# 2. Left-tailed:
#    H0: σ1² = σ2²
#    H1: σ1² < σ2²
#
# 3. Two-tailed:
#    H0: σ1² = σ2²
#    H1: σ1² ≠ σ2²

# ------------------------------------------------------
# Decision Rule
# - Get critical F value from F-distribution table using α, df1, df2
# - If Fcalc > Ftable → Reject H0 (variances different)
# - If Fcalc ≤ Ftable → Fail to reject H0 (variances equal)

# ------------------------------------------------------
# Steps
# 1. Compute sample variances (s1², s2²)
# 2. Formulate H0 & H1
# 3. Compute F = s1² / s2²  (larger ÷ smaller)
# 4. Find df1, df2
# 5. Get F critical from F table (α = 0.05 unless given)
# 6. Compare Fcalc vs Ftable → Make decision

# ------------------------------------------------------
# Example
# Sample 1: σ = 10.47, n = 41
# Sample 2: σ =  8.12, n = 21
#
# s1² = 109.63, s2² = 65.99
# Fcalc = 109.63 / 65.99 = 1.66
# df1 = 40, df2 = 20
# Ftable (α=0.025, two-tailed) = 2.287
#
# Since 1.66 < 2.287 → Fail to reject H0
# Variances are equal.

# ------------------------------------------------------
# Applications
# - Compare variances of two groups
# - Basis for ANOVA (comparing >2 groups)
# - Model comparison in regression
# ------------------------------------------------------

# ======================================================
# Student’s t-Distribution – Simplified Notes
# ======================================================

# Definition
# - A probability distribution used when:
#   1) Sample size is small (n ≤ 30)
#   2) Population standard deviation (σ) is unknown
# - Similar to normal distribution but has heavier tails
# - Discovered by W.S. Gosset (pen name: "Student")

# ------------------------------------------------------
# Formula for t-Score
#   t = (x̄ - μ) / (s / √n)
#   where,
#   x̄ = sample mean
#   μ = population mean
#   s = sample standard deviation
#   n = sample size

# ------------------------------------------------------
# When to Use
# - Small sample sizes
# - σ unknown
# - Population ~ normal (symmetric, unimodal)

# ------------------------------------------------------
# Properties
# - Symmetric & bell-shaped (like normal)
# - Mean = 0 (for df > 1)
# - Variance = df / (df - 2)  [for df > 2]
# - More spread (heavier tails) for small df
# - As df → ∞, t-distribution → normal distribution

# ------------------------------------------------------
# Confidence Interval Example
# Suppose:
#   n = 20,  x̄ = 4,  s = 1.5
#   df = 19, t* (90% CI) = 1.729
# CI = 4 ± (1.729 * 1.5 / √20)
#    = (3.58, 4.42)  → population mean lies in this range

# ------------------------------------------------------
# t-scores & p-values
# - t-score = how far sample mean is from population mean (in SD units)
# - p-value = probability of observing result if H0 is true
#   Decision: If p < α → reject H0

# ------------------------------------------------------
# Applications
# 1. Test population mean (one-sample t-test)
# 2. Compare two means (independent samples)
# 3. Compare paired means (dependent samples)
# 4. Test correlation coefficients

# ------------------------------------------------------
# Difference: t vs Normal
# - t-distribution → small sample, σ unknown, heavier tails
# - Normal distribution → large sample, σ known, lighter tails

# ------------------------------------------------------
# Limitations
# - Sensitive to outliers
# - Assumes population is normal
# - For large n, normal distribution is preferred
# ======================================================
