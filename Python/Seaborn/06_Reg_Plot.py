# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px  # Not used here but imported for interactive plotting if needed later

# Load the 'tips' dataset from seaborn's sample datasets
tips = sns.load_dataset('tips')

# =====================
# What is regplot?
# =====================
# regplot is an axes-level function in Seaborn that combines a scatterplot with a linear regression model.
# It fits and plots a regression line (y ~ x) along with a 95% confidence interval by default.
# It is useful for visualizing the linear relationship between two numeric variables.

# Simple regression plot using regplot
# NOTE: regplot does not support the 'hue' parameter (use lmplot for that functionality)
sns.regplot(data=tips, x='total_bill', y='tip')
plt.title('regplot: Total Bill vs Tip')  # Add title for clarity
plt.show()


# =====================
# What is lmplot?
# =====================
# lmplot is a figure-level function in Seaborn that combines regplot with FacetGrid.
# It allows for more flexibility, including grouping by categories using 'hue', 'col', and 'row'.
# Useful for comparing regression lines across different groups.

# Regression plot with grouping by 'sex' using hue
sns.lmplot(data=tips, x='total_bill', y='tip', hue='sex')
plt.title('lmplot: Total Bill vs Tip by Sex')  # Title applies to the whole figure
plt.show()


# =====================
# What is residplot?
# =====================
# residplot is used to plot the residuals (the difference between observed and predicted values) of a linear regression.
# Helps in diagnosing the quality of the regression fit — residuals should appear randomly scattered.

# Residual plot to check the quality of the linear regression fit
sns.residplot(data=tips, x='total_bill', y='tip')
plt.title('residplot: Residuals of Total Bill vs Tip')
plt.show()
