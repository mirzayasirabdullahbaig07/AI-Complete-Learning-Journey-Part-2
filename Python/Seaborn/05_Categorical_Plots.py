import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load sample datasets from seaborn
tips = sns.load_dataset('tips')     # Dataset of restaurant tips
iris = sns.load_dataset('iris')     # Dataset of iris flower measurements

# Basic scatter plot (numerical vs numerical)
sns.scatterplot(data=tips, x='total_bill', y='tip')  # Scatter plot of total bill vs tip
plt.title("Scatter Plot: Total Bill vs Tip")
plt.show()

# ---------------------- #
# Categorical Scatter Plots
# ---------------------- #

# Strip Plot - shows all observations along a categorical axis with possible jitter
sns.stripplot(data=tips, x='day', y='total_bill')
plt.title("Strip Plot without Jitter")
plt.show()

# Strip Plot with jitter - spreads points to avoid overlap
sns.stripplot(data=tips, x='day', y='total_bill', jitter=True)
plt.title("Strip Plot with Jitter")
plt.show()

# Catplot with kind='strip' - figure-level function version of strip plot
sns.catplot(data=tips, x='day', y='total_bill', kind='strip')
plt.suptitle("Catplot (Strip)", y=1.02)
plt.show()

# Strip plot with jitter and hue (color by category)
sns.catplot(data=tips, x='day', y='total_bill', kind='strip', jitter=0.3, hue='sex')
plt.suptitle("Strip Plot with Hue (Sex)", y=1.02)
plt.show()

# Swarm Plot - similar to strip plot but avoids overlapping points
sns.swarmplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title("Swarm Plot")
plt.show()

# Swarm plot using catplot
sns.catplot(data=tips, x='day', y='total_bill', kind='swarm')
plt.suptitle("Catplot (Swarm)", y=1.02)
plt.show()

# ---------------------------- #
# Categorical Distribution Plots
# ---------------------------- #

# Box Plot - shows distribution using 5-number summary (min, Q1, median, Q3, max)
sns.boxplot(data=tips, x='day', y='total_bill')
plt.title("Box Plot by Day")
plt.show()

# Single-variable boxplot
sns.boxplot(data=tips, y='total_bill')
plt.title("Single Variable Box Plot")
plt.show()

# Box plot with hue using catplot
sns.catplot(data=tips, x='day', y='total_bill', kind='box', hue='sex')
plt.suptitle("Box Plot with Hue (Sex)", y=1.02)
plt.show()

# Violin Plot - combines boxplot and KDE (kernel density estimation)
sns.violinplot(data=tips, x='day', y='total_bill')
plt.title("Violin Plot by Day")
plt.show()

# Violin plot using catplot
sns.catplot(data=tips, x='day', y='total_bill', kind='violin')
plt.suptitle("Catplot (Violin)", y=1.02)
plt.show()

# Violin plot with hue (split view for better comparison)
sns.catplot(data=tips, x='day', y='total_bill', kind='violin', hue='sex', split=True)
plt.suptitle("Violin Plot with Hue (Sex) - Split", y=1.02)
plt.show()

# ------------------------ #
# Categorical Estimate Plots
# ------------------------ #

# Bar Plot - shows central tendency (mean by default) with confidence interval
sns.barplot(data=tips, x='sex', y='total_bill')
plt.title("Bar Plot: Average Total Bill by Sex")
plt.show()

# Bar plot with hue
sns.barplot(data=tips, x='sex', y='total_bill', hue='smoker')
plt.title("Bar Plot: Total Bill by Sex and Smoking Status")
plt.show()

# Bar plot with custom estimator (min instead of mean)
sns.barplot(data=tips, x='sex', y='total_bill', hue='smoker', estimator=np.min)
plt.title("Bar Plot with Min Estimator")
plt.show()

# Point Plot - shows point estimates and confidence intervals
sns.pointplot(data=tips, x='sex', y='total_bill')
plt.title("Point Plot: Total Bill by Sex")
plt.show()

# Point plot with hue and without confidence interval
sns.pointplot(data=tips, x='sex', y='total_bill', hue='smoker', ci=None)
plt.title("Point Plot with Hue and No CI")
plt.show()

# Count Plot - shows counts of observations for each category
sns.countplot(data=tips, x='sex')
plt.title("Count Plot: Sex Distribution")
plt.show()

# Count plot with hue
sns.countplot(data=tips, x='sex', hue='day')
plt.title("Count Plot: Sex Distribution by Day")
plt.show()

# ---------------------------- #
# Faceting (Subplot by Category)
# ---------------------------- #

# Facet plots using catplot to compare subgroups
sns.catplot(data=tips, x='sex', y='total_bill', col='smoker')
plt.suptitle("Facet Catplot: Smoker vs Total Bill", y=1.02)
plt.show()

sns.catplot(data=tips, x='sex', y='total_bill', col='smoker', kind='box')
plt.suptitle("Facet Box Plot by Smoking Status", y=1.02)
plt.show()

# Facet with both row and column dimensions
sns.catplot(data=tips, x='sex', y='total_bill', col='smoker', row='time', kind='box')
plt.suptitle("Facet Box Plot by Smoker and Time", y=1.02)
plt.show()
