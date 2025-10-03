# ================================
# 📌 Week Topic: Systems of Linear Equations
# ================================
# In this week, you will learn:
# - What a system of linear equations is
# - Different ways to represent them:
#       1. As a set of lines in a plane
#       2. As a matrix (array of numbers)
# - What singular and non-singular systems are
# - Why these concepts are important in Linear Algebra
#
# 🔑 Importance:
# Linear Algebra is widely applied in science and technology.
# In Machine Learning, it is one of the most essential mathematical foundations.
# Example: Linear Regression (most popular application).

# ================================
# 📌 Linear Regression (Application in ML)
# ================================
# Linear Regression is a supervised ML method.
# - "Supervised" means we already have data (inputs & outputs).
# - Goal: Discover the relationship between inputs (features) and outputs (targets).

# 🌀 Example:
# Suppose you want to predict the electrical power output from a wind turbine.
# - Input feature (x-axis): Wind Speed
# - Output target (y-axis): Power Output
#
# When you plot the data points, you see a pattern.
# The goal of Linear Regression is to find the "line of best fit".

# ================================
# 📌 The Linear Model Equation
# ================================
# Familiar form: y = mx + b
# - y = target/output (power output)
# - x = input/feature (wind speed)
# - m = slope (weight of feature)
# - b = intercept (bias)
#
# In Machine Learning:
#   y = w * x + b
# - w = weight (like slope, adjusts input effect)
# - b = bias (shifts the line up/down)

# 🌀 Example Prediction:
# If wind speed = 5 (m/s), model might predict:
# Power Output ≈ 1500 kW
#
# Note: The line won't be perfect. Actual data points are scattered,
# but the model gives a reasonable estimate.

# ================================
# 📌 Extending to Multiple Features
# ================================
# What if we add more features like:
# - Wind Speed
# - Temperature
# - Humidity
# - Pressure, etc.
#
# Then the equation becomes:
#   y = w1 * (wind speed) + w2 * (temperature) + ... + wn * (other features) + b
#
# - Each feature gets its own weight (w1, w2, ..., wn).
# - Bias (b) still shifts the prediction.
#
# Visualization:
# - With 1 feature → Line in 2D
# - With 2 features → Plane in 3D
# - With many features → Hyperplane in higher dimensions
#
# Concept remains the same:
# Find the best weights (w1, w2, ..., wn) and bias (b) that minimize error
# and make accurate predictions under the assumption of linear relationships.

# ================================
# 📌 Key Takeaway
# ================================
# - Systems of linear equations are foundational in Linear Algebra.
# - Linear Regression applies these ideas directly in Machine Learning.
# - By adjusting weights and bias, the model can predict outcomes from inputs.
