# ======================================
# Statistical Moments & Kurtosis
# ======================================

# In statistics, there are four key moments:
# 1. Mean                → Central tendency
# 2. Standard Deviation  → Dispersion
# 3. Skewness            → Asymmetry of the distribution
# 4. Kurtosis            → Tailedness (fat tails or outliers)

# --------------------------------------
# What is Kurtosis?
# --------------------------------------

# Kurtosis is the 4th statistical moment. In probability theory and statistics,
# kurtosis (meaning "curved" or "arching") measures the tailedness of the 
# probability distribution of a real-valued random variable.
# Like skewness, kurtosis helps describe the shape of the distribution.
# It tells how heavy or light the tails of the distribution are — i.e., 
# how likely extreme values (outliers) are.

# Higher kurtosis ⇒ more extreme outliers (fat tails)
# Lower kurtosis ⇒ fewer extreme outliers (thin tails)

# --------------------------------------
# Practical Use-case in Finance
# --------------------------------------

# In finance, kurtosis risk refers to the risk associated with extreme outcomes 
# or “fat tails” in the distribution of returns of a particular asset or portfolio.

# ▶ A high kurtosis means a higher likelihood of large gains or losses.
# ▶ Investors may adjust their strategies to account for kurtosis risk.

# --------------------------------------
# Excess Kurtosis & Types
# --------------------------------------

# Excess Kurtosis:
# It measures how much more peaked or flat a distribution is compared to a 
# normal distribution (which has a kurtosis of 3).
# Excess kurtosis = Sample kurtosis − 3

# ➤ Types of Kurtosis:

# 1. Leptokurtic (Positive Excess Kurtosis)
# - Fat tails, more extreme values.
# - Riskier and more volatile.
# - Example: Financial assets with sudden price jumps.

# 2. Platykurtic (Negative Excess Kurtosis)
# - Thin tails, fewer extreme values.
# - Less risky and more stable.
# - Example: Assets with gradual price movements.

# 3. Mesokurtic (Zero Excess Kurtosis)
# - Similar to normal distribution.
# - Balanced risk and return.
# - Example: Ideal asset return distribution in theory.

# ======================================
# How to Check if Data is Normally Distributed?
# ======================================

# 1. Visual Inspection (Histogram/KDE)
# 2. QQ Plot (Quantile-Quantile Plot)
# 3. Statistical Tests (e.g., Shapiro-Wilk, Anderson-Darling)

# --------------------------------------
# 1. Visual Inspection
# --------------------------------------

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = sns.load_dataset('iris')
sns.kdeplot(df['sepal_length'])
plt.title("KDE Plot - Sepal Length")
plt.show()

# --------------------------------------
# 2. QQ Plot (Quantile-Quantile Plot)
# --------------------------------------

import numpy as np
from scipy import stats

# Generate quantiles from sample data
data = sorted(df['sepal_length'].tolist())
y_quantiles = [np.percentile(data, i) for i in range(1, 101)]

# Generate quantiles from normal distribution
normal_sample = np.random.normal(loc=0, scale=1, size=1000)
x_quantiles = [np.percentile(normal_sample, i) for i in range(1, 101)]

# Plot QQ plot
sns.scatterplot(x=x_quantiles, y=y_quantiles)
plt.xlabel("Theoretical Quantiles (Normal Dist)")
plt.ylabel("Sample Quantiles (Data)")
plt.title("QQ Plot: Sample vs Normal Distribution")
plt.grid(True)
plt.show()

# QQ Plot Interpretation:
# ➤ If the points fall along a straight line → the distribution is approximately normal.
# ➤ Deviations from the line → distribution is not normal.

# --------------------------------------
# Does QQ Plot Only Test Normality?
# --------------------------------------

# No. QQ plots can compare data to **any distribution**, not just normal.

import statsmodels.api as sm

# Fit a uniform distribution
x = df['sepal_length']
params = stats.uniform.fit(x)  # Get parameters for uniform fit
dist = stats.uniform(loc=params[0], scale=params[1])

# QQ Plot with uniform distribution
fig = sm.qqplot(x, dist=dist, line='45')
plt.title("QQ Plot: Uniform Distribution Fit")
plt.xlabel("Theoretical Quantiles (Uniform)")
plt.ylabel("Sample Quantiles")
plt.grid(True)
plt.show()

# ======================================
# Summary
# ======================================

# ✔ Kurtosis measures the extremity of outliers in the data.
# ✔ Leptokurtic → More extreme values (fat tails)
# ✔ Platykurtic → Fewer extreme values (thin tails)
# ✔ Mesokurtic  → Normal tail thickness
# ✔ QQ plots help compare any dataset against any theoretical distribution.
# ✔ Use visual plots + statistical tests to confirm normality assumptions.


# What is Uniform Distribution and Its Types
# In probability theory and statistics, a uniform distribution is a probability distribution 
# where all outcomes are equally likely within a given range. This means that if you select a random 
# value from this range, any value would be as likely as any other.

# Types:
# - Discrete Uniform Distribution
# - Continuous Uniform Distribution

# Notation:
# X ~ U(a, b)

# Examples:
# a. The height of a randomly selected person from a group with heights ranging from 5'6" to 6'0" 
#    follows a continuous uniform distribution.
# b. The time a machine takes to produce a product, ranging from 5 to 10 minutes.
# c. The distance a car travels on a full tank, ranging from 300 to 400 miles.
# d. The weight of an apple from a basket, weighing between 100 and 200 grams.

# Applications in Machine Learning and Data Science:
# a. Random Initialization:
#    Used in algorithms like neural networks and k-means to ensure all initial values have equal chance.
# b. Sampling:
#    Useful for selecting representative subsets from balanced datasets.
# c. Data Augmentation:
#    Generate synthetic data points within a defined range using uniform distribution.
# d. Hyperparameter Tuning:
#    Uniform priors allow random search over hyperparameter space.

# ---------------------------------------------------------

# Log-Normal Distribution
# A log-normal distribution is a continuous, heavy-tailed probability distribution 
# of a random variable whose logarithm is normally distributed.

# Examples:
# - Length of comments on internet forums
# - User dwell time on online articles
# - Length of chess games
# - Income of 97–99% of the population (log-normally distributed)

# This is a skewed distribution.

# ---------------------------------------------------------

# Pareto Distribution
# The Pareto distribution models the distribution of wealth, income, and other variables 
# that follow a power-law behavior.

# What is Power Law?
# A power law is a functional relationship between two variables, where one is proportional 
# to a power of the other: y = k * x^a

# Examples:
# - Size of human settlements
# - File size distribution in internet traffic (TCP)

# ---------------------------------------------------------
# How to Detect Pareto Distribution: Log-Log Plot
import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
alpha = 3
xm = 1

# Generate x values
x = np.linspace(0.1, 10, 1000)

# Calculate Pareto y values
y = alpha * (xm**alpha) / (x**(alpha + 1))

# Plot log-log
plt.plot(np.log(x), np.log(y))
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('Pareto Distribution (Log-Log Plot)')
plt.show()

# ---------------------------------------------------------
# QQ Plot to Validate Pareto Distribution Fit
import scipy.stats as stats
import statsmodels.api as sm

# Generate sample data
x = np.linspace(1, 10, 1000)

# Fit Pareto distribution
params = stats.pareto.fit(x, floc=0)

# Create Pareto distribution with fitted parameters
dist = stats.pareto(b=params[0], scale=params[2])

# Generate QQ plot
fig = sm.qqplot(x, dist=dist, line='45')
plt.title('QQ Plot of Pareto Distribution with Pareto Fit')
plt.xlabel('Theoretical Quantiles')
plt.ylabel('Sample Quantiles')
plt.show()


# 📊 Normalizing Skewed Data for Machine Learning Models
# ------------------------------------------------------

# 🧠 Why Transform Data?
# Many machine learning models (like Linear Regression, Logistic Regression, etc.)
# assume that input features follow a normal distribution. 
# To meet this assumption, we apply **feature transformations**.

# 🔁 Common Mathematical Transformations (Transformers):
# - Log Transformation: Handles right-skewed data (no negative values).
# - Box-Cox Transformation: Only works with positive data.
# - Power Transformation: Includes Box-Cox and Yeo-Johnson.
# - Quantile Transformation: Makes data follow a uniform or normal distribution.
# - Reciprocal Transformation: Inverts the values (large become small and vice versa).
# - Square/Square Root Transformation: Used for skewness correction.
# - FunctionTransformer (Sklearn): Custom or built-in transformations.

# ------------------------------------------------------

# 🛠️ Import Libraries
import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer

# 📥 Load Dataset (Titanic sample)
df = pd.read_csv('train.csv', usecols=['Age', 'Fare', 'Survived'])

# 🧼 Data Cleaning - Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)

# 🎯 Feature and Target Split
X = df[['Fare', 'Survived']]
y = df['Age']

# 📚 Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 📈 Data Visualization - Distribution and Normality Check
plt.figure(figsize=(14, 4))

# Probability Density Function (PDF)
plt.subplot(1, 2, 1)
sns.histplot(y_train, kde=True, color='blue')
plt.title('Age Distribution (PDF)')

# QQ Plot to check normality
plt.subplot(1, 2, 2)
stats.probplot(y_train, dist="norm", plot=plt)
plt.title('Age QQ Plot')

plt.tight_layout()
plt.show()

# 🧪 You can now try applying transformations like:
# - np.log1p()   --> for log transformation
# - np.sqrt()    --> for square root
# - 1 / x        --> for reciprocal
# - PowerTransformer or QuantileTransformer from sklearn

# ----------------------------------------
# 🔢 Log, Box-Cox, and Yeo–Johnson Transforms
# ----------------------------------------

# 📌 1. Log Transform
# ------------------------
# The log transform is used to reduce right skewness in data.
# It helps in making the data more normally distributed.

# Example:
# If x = 100, then log(x) = 4.605 (natural log)
# Common use case: Apply to positively skewed data (e.g., income, prices)

# Code Example:
import numpy as np

data = [1, 10, 100, 1000, 10000]
log_data = np.log(data)
print("Log-transformed data:", log_data)

# ----------------------------------------
# 📌 2. Box-Cox Transform
# ------------------------
# Formula:
#     x(λ) = (x^λ - 1) / λ      if λ ≠ 0
#     x(λ) = ln(x)              if λ = 0
#
# 📘 Note:
# - x must be positive (x > 0)
# - λ (lambda) is a parameter in the range [-5, 5]
# - The goal is to find the best λ that normalizes the data
# - Used in regression and ML preprocessing to reduce skewness

# Code Example:
from scipy import stats

positive_data = [1, 2, 3, 4, 5, 10, 20]
boxcox_data, lambda_val = stats.boxcox(positive_data)
print("Box-Cox transformed data:", boxcox_data)
print("Optimal λ:", lambda_val)

# ----------------------------------------
# 📌 3. Yeo–Johnson Transform
# ------------------------
# This is an extension of the Box-Cox transformation.
# ✅ It works for both positive and negative values.

# Formula:
# For xi ≥ 0:
#     x(λ) = [(xi + 1)^λ - 1] / λ              if λ ≠ 0
#     x(λ) = ln(xi + 1)                        if λ = 0
#
# For xi < 0:
#     x(λ) = - [(-xi + 1)^(2 - λ) - 1] / (2 - λ)  if λ ≠ 2
#     x(λ) = - ln(-xi + 1)                       if λ = 2

# 📘 Note:
# - Useful when data includes negative values.
# - Maintains continuity with Box-Cox logic.
# - Used in data preprocessing for skewed data with mixed signs.

# Code Example:
from sklearn.preprocessing import PowerTransformer

mixed_data = [[-5], [-1], [0], [2], [5], [10]]
pt = PowerTransformer(method='yeo-johnson')
yj_data = pt.fit_transform(mixed_data)
print("Yeo-Johnson transformed data:", yj_data)
print("λ used by transformer:", pt.lambdas_)

# ----------------------------------------
# ✅ Summary:
# - Use Log or Box-Cox if your data is strictly positive and skewed.
# - Use Yeo–Johnson if your data includes zero or negative values.
# - All transformations help to stabilize variance and make data more normal.
