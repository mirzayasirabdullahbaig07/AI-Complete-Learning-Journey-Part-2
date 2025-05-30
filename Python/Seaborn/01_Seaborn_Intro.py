# What is Seaborn?
# Seaborn is a Python data visualization library based on Matplotlib.
# It provides a high-level interface for drawing attractive and informative statistical graphics.

# Why to study Seaborn?
# - Provides a layer of abstraction, making it simpler to use than Matplotlib.
# - Offers better aesthetics, which means the graphs look more beautiful and modern.
# - Supports a wide variety of graphs useful for data analysis.
# - Very famous and widely used in the data science and machine learning community.

# Roadmap to Seaborn:
# 1. Learn to install and import seaborn.
# 2. Explore built-in datasets like 'tips', 'iris', 'flights'.
# 3. Understand the two types of functions:
#    - Axis-level functions: Return a single plot on an Axes (e.g., sns.scatterplot()).
#    - Figure-level functions: Create full figures with subplots (e.g., sns.relplot()).
# 4. Learn plot categories (see below).
# 5. Practice customizing styles, palettes, labels, titles, legends.
# 6. Work on advanced usage: combining plots, using FacetGrid, PairGrid, etc.

# Confusion in Seaborn?
# - Two functions might give the same graph, e.g.:
#   sns.scatterplot() vs sns.relplot(kind='scatter')
# - Understand the difference between figure-level and axis-level functions.

# Main classification of Seaborn plots:

# 1. Relational Plots:
#    - sns.scatterplot()     # For scatter plots
#    - sns.lineplot()        # For line plots
#    - sns.relplot()         # Figure-level wrapper for scatter and line plots

# 2. Distribution Plots:
#    - sns.histplot()        # For histograms
#    - sns.kdeplot()         # For kernel density estimate plots
#    - sns.rugplot()         # For rug plots

# 3. Categorical Plots:
#    - sns.barplot()         # Bar chart with summary statistic (mean, etc.)
#    - sns.countplot()       # Bar chart of counts
#    - sns.boxplot()         # Box-and-whisker plot
#    - sns.swarmplot()       # Scatter plot with non-overlapping points
#    - sns.violinplot()      # Combination of KDE and box plot

# 4. Regression Plots:
#    - sns.regplot()         # Regression line with scatter plot
#    - sns.lmplot()          # Figure-level regression plot

# 5. Matrix Plots:
#    - sns.heatmap()         # Color-encoded matrix plot
#    - sns.clustermap()      # Hierarchical clustering heatmap

# 6. Multi-plot Grids:
#    - sns.jointplot()       # Combines scatter + histogram + KDE
#    - sns.pairplot()        # Pairwise plots of entire dataframe

# Seaborn is a key library for data visualization and analysis.
# Learning it well will help in creating professional and insightful plots with ease.
