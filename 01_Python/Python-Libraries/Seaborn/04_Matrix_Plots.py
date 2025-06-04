# What is Matrix Plot in Seaborn?
# Matrix plots are used to visualize rectangular data.
# There are two main types of matrix plots in Seaborn:
# 1. Heatmap - color encoded 2D matrix
# 2. Clustermap - hierarchically clustered heatmap

# HEATMAP
# Plots rectangular data as a color-encoded matrix
# First, we convert our dataset into a wide-form using pivot

# Pivot the dataset: rows = country, columns = year, values = life expectancy
temp_df = gap.pivot(index='country', columns='year', values='lifeExp')
temp_df

# Plot the heatmap (Axes-level function)
plt.figure(figsize=(15, 15))
sns.heatmap(temp_df)

# Filter only for Europe and pivot again
temp_df = gap[gap['continent'] == 'Europe'].pivot(index='country', columns='year', values='lifeExp')

# Plot heatmap with more options
# annot=True displays values in the cells
# linewidth=0.5 adds space between cells
# cmap changes the color map
plt.figure(figsize=(15, 15))
sns.heatmap(temp_df, annot=True, linewidth=0.5, cmap='summer')


# CLUSTER MAP
# Plots a matrix dataset as a hierarchically-clustered heatmap
# Automatically clusters rows and columns to show structure in the data
# Requires scipy library to be installed

# Load the iris dataset
iris = px.data.iris()
iris

# Use only the numeric columns for clustering
sns.clustermap(iris.iloc[:, [0, 1, 2, 3]])
