# ================================================================
# Continuous Probability Distributions (CPDs) in Machine Learning
# ================================================================
# CPDs describe probabilities for continuous random variables
# (e.g., height, time, prices). Values can take ANY number in a range.
#
# Key Functions:
# 1. PDF (Probability Density Function):
#    - Probability "density" at a point.
#    - Area under curve = probability.
#
# 2. CDF (Cumulative Distribution Function):
#    - P(X ≤ x), probability variable is less than/equal to x.
#    - CDF = ∫ PDF, PDF = derivative of CDF.
#
# Importance in ML:
# - Models uncertainty in predictions.
# - Gaussian assumptions in regression & Bayesian networks.
# - Used in MLE (Maximum Likelihood Estimation).
# - Bayesian inference for updating beliefs.
# - Generative models (GMMs, VAEs) rely on them.
# ================================================================


# ----------------------------------------------------------------
# 1. Normal (Gaussian) Distribution
# ----------------------------------------------------------------
# - Bell-shaped, symmetric around mean μ.
# - Defined by mean (μ) and std. deviation (σ).
#
# Formula:
#   f(x) = 1/(σ√(2π)) * exp(-(x-μ)^2 / (2σ^2))
#
# Rule of thumb:
# - 68% data within μ ± σ
# - 95% data within μ ± 2σ
# - 99.7% data within μ ± 3σ


# ----------------------------------------------------------------
# 2. Uniform Distribution
# ----------------------------------------------------------------
# - All values between [a, b] equally likely.
#
# Formula:
#   f(x) = 1 / (b-a),   for a ≤ x ≤ b
#
# Mean = (a+b)/2
# Var  = (b-a)^2 / 12


# ----------------------------------------------------------------
# 3. Exponential Distribution
# ----------------------------------------------------------------
# - Time between events in a Poisson process.
# - Defined by rate λ (events per unit time).
#
# Formula:
#   f(x) = λ * e^(-λx),   for x ≥ 0
#
# Mean = 1/λ
# Var  = 1/λ^2


# ----------------------------------------------------------------
# 4. Chi-Squared Distribution
# ----------------------------------------------------------------
# - Special case of Gamma distribution.
# - Used in hypothesis testing (χ² test).
# - Defined by degrees of freedom (k).
#
# Mean = k
# Var  = 2k


# ----------------------------------------------------------------
# 5. Beta Distribution
# ----------------------------------------------------------------
# - Models probabilities (values strictly in [0,1]).
# - Defined by shape parameters α and β.
#
# Formula:
#   f(x) ∝ x^(α-1) * (1-x)^(β-1),   for 0 ≤ x ≤ 1
#
# Mean = α / (α+β)
# Var  = (αβ) / [(α+β)^2 * (α+β+1)]
#
# Uses: Bayesian inference (priors/posteriors for probabilities).


# ----------------------------------------------------------------
# 6. Gamma Distribution
# ----------------------------------------------------------------
# - Generalization of exponential distribution.
# - Defined by shape parameter k and rate λ.
#
# Formula:
#   f(x) = (λ^k / Γ(k)) * x^(k-1) * e^(-λx),   for x ≥ 0
#
# Mean = k / λ
# Var  = k / λ^2
#
# Uses: Modeling waiting times, Bayesian statistics.
# ----------------------------------------------------------------
