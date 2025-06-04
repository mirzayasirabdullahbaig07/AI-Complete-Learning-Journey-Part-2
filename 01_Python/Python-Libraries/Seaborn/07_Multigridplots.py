import seaborn as sns
import matplotlib.pyplot as plt

# Load example datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')

# ------------------------------------------------------------------------------
# FACETGRID - A figure-level function to plot multi-plot grids for one variable.
# Allows fine control over the layout, customization with .map(), legends, etc.
# ------------------------------------------------------------------------------
g = sns.FacetGrid(data=tips, col='day', row='time')
g.map(sns.violinplot, 'sex', 'total_bill')

# With hue for sub-categories like smoker vs. non-smoker
g = sns.FacetGrid(data=tips, col='day', row='time', hue='smoker')
g.map(sns.scatterplot, 'total_bill', 'tip')
g.add_legend()

# ------------------------------------------------------------------------------
# PAIRPLOT - Quick, high-level interface to create pairwise plots (scatter + hist)
# Automatically shows relationships between all numeric variables
# ------------------------------------------------------------------------------
sns.pairplot(iris, hue='species')  # Automatically colors by species

# ------------------------------------------------------------------------------
# PAIRGRID - More customizable version of pairplot. Use map_diag, map_upper, map_lower
# to control what kind of plot goes where in the grid.
# ------------------------------------------------------------------------------
# Basic scatterplot for all pairs
g = sns.PairGrid(data=iris)
g.map(sns.scatterplot)

# Customized diagonal and off-diagonal plots
g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.boxplot)
g.map_offdiag(sns.scatterplot)

# Even more customized: upper = scatterplot, lower = KDE plot
g = sns.PairGrid(data=iris, hue='species')
g.map_diag(sns.boxplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)

# Only for specific variables
g = sns.PairGrid(data=iris, hue='species', vars=['sepal_width', 'petal_width'])
g.map_diag(sns.boxplot)
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)

# ------------------------------------------------------------------------------
# JOINTPLOT - High-level function to draw a bivariate plot with univariate histograms
# on top and to the side. Great for showing distribution + relationship.
# ------------------------------------------------------------------------------
sns.jointplot(data=tips, x='total_bill', y='tip', kind='hist')
sns.jointplot(data=tips, x='total_bill', y='tip', kind='reg')
sns.jointplot(data=tips, x='total_bill', y='tip', kind='hist', hue='sex')

# ------------------------------------------------------------------------------
# JOINTGRID - Lower-level version of jointplot for more customization.
# You specify what goes in the main plot and marginal plots.
# ------------------------------------------------------------------------------
g = sns.JointGrid(data=tips, x='total_bill', y='tip')
g.plot(sns.scatterplot, sns.histplot)

g = sns.JointGrid(data=tips, x='total_bill', y='tip')
g.plot(sns.scatterplot, sns.boxplot)

# ------------------------------------------------------------------------------
# CATPLOT - Figure-level function for categorical plots.
# Supports multiple kinds like 'violin', 'box', 'strip', 'swarm', etc.
# Supports facets (col, row)
# ------------------------------------------------------------------------------
sns.catplot(data=tips, x='sex', y='total_bill', kind='violin', col='day', row='time')

plt.show()
