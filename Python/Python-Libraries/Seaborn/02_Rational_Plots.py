# What is relational plot in seaborn?
# Relational plots are used to show relationships between two numeric variables.

# scatter plot
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# load dataset
tips = sns.load_dataset('tips')
tips  # show the dataset

# this is axis level function
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='sex', style='time', size='size')

# this is figure level function
sns.relplot(kind='scatter', data=tips, x='total_bill', y='tip', hue='sex', style='time', size='size')

# line plot

# we use line plots to create time series graphs
gap = px.data.gapminder()
gap  # show the gapminder dataset

# filter data for India
temp_df = gap[gap['country'] == 'India']
temp_df

# axis level line plot
sns.lineplot(data=temp_df, x='year', y='lifeExp')

# figure level line plot
sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp')

# compare multiple countries
temp_df = gap[gap['country'].isin(['India', 'United Kingdom', 'Pakistan'])]
temp_df

# axis level multiple lines
sns.lineplot(data=temp_df, x='year', y='lifeExp', hue='country')

# figure level multiple lines with more styling
sns.relplot(kind='line', data=temp_df, x='year', y='lifeExp', hue='country', style='continent', size='continent')  # here legend is outside

# facet plot - only works on figure level function - works with relplot, not with scatterplot and lineplot

# facet by column
sns.relplot(kind='scatter', x='total_bill', y='tip', col='sex', data=tips)

# facet by row
sns.relplot(kind='scatter', x='total_bill', y='tip', row='sex', data=tips)

# facet by column and row
sns.relplot(kind='scatter', x='total_bill', y='tip', col='sex', row='smoker', data=tips)

# facet by column and day
sns.relplot(kind='scatter', x='total_bill', y='tip', col='sex', row='day', data=tips)

# facet plot with col_wrap
sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year')

# use col_wrap to control plots per row
sns.relplot(data=gap, x='lifeExp', y='gdpPercap', kind='scatter', col='year', col_wrap=4)
