# What is a scatter plot in statistics?

# If you have 2 columns and want to study the relationship between them, there are three main scenarios:

# 1. Both columns are categorical → Use a **crosstab** or **contingency table** to analyze frequency.
# 2. One column is categorical and the other is numerical → Use a **side-by-side histogram** or **boxplot**.
#    This helps visualize how the numerical data is distributed across categories.
# 3. Both columns are numerical → Use a **scatter plot**.

# A scatter plot is used to visualize the relationship between two **continuous (numerical)** variables.

# We've already created many scatter plots, but how do we measure the actual **relationship** between the two variables?

#  To measure the relationship, we use **correlation**:
# - **Positive correlation**: as one variable increases, the other also increases.
# - **Negative correlation**: as one increases, the other decreases.
# - **No correlation**: no clear pattern.

#  Use Pearson correlation coefficient (r) to quantify this relationship:
# - r close to 1 → strong positive correlation
# - r close to -1 → strong negative correlation
# - r near 0 → no linear correlation

#  You can calculate this using:
#     df['col1'].corr(df['col2'])   # Using Pandas
#     scipy.stats.pearsonr(col1, col2)  # Using Scipy for more detail (returns coefficient and p-value)
