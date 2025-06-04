# what is distribution plots in seaborn?
# it is used for univariate analysis 
# used to find out the distribution
# range of observation
# central tendency
# is the data bimodal
# are there outliers?

# plots under distribution plot
# histplot
# kdeplot
# rugplot

# figure level - displot
# axes level - histplot, kdeplot, rugplot

# histplot
sns.histplot(data = tips, x = 'total_bill')

# using displot (figure level)
sns.displot(data = tips, x = 'total_bill', kind = 'hist' )

# bin parameter
sns.displot(data = tips, x = 'total_bill', kind = 'hist', bins = 20)

# fewer bins
sns.displot(data = tips, x = 'total_bill', kind = 'hist', bins = 2)

# hist on categorical data (this is actually a count plot, not a true histogram)
sns.displot(data = tips, x = 'day', kind = 'hist' )

# hue parameter to compare distributions
sns.displot(data = tips, x = 'tip', kind = 'hist', hue = 'sex')

# element = 'step' shows histogram outline
sns.displot(data = tips, x = 'tip', kind = 'hist', hue = 'sex', element = 'step')

# example with titanic dataset
titanic = sns.load_dataset('titanic')
titanic

# histogram with hue and step element
sns.displot(data = titanic, x = 'age', kind = 'hist', element ='step', hue = 'sex')

# faceting using col and row
sns.displot(data = tips, x = 'tip', kind = 'hist', col = 'sex', row = 'day')

# kdeplot
# instead of bars, kde uses gaussian kernels to smooth the distribution
sns.kdeplot(data = tips, x = "total_bill")

# kde using displot
sns.displot(data = tips, x = 'total_bill', kind = 'kde', hue = 'sex', fill = True)

# rugplot
# shows ticks along axis to visualize data distribution
sns.kdeplot(data = tips, x = 'total_bill')
sns.rugplot(data = tips, x = 'total_bill')

# bivariate histogram
# shows counts as color intensity for two variables
sns.histplot(data = tips, x = 'total_bill', y = 'tip')

# bivariate histogram using displot
sns.displot(data = tips, x = 'total_bill', y = 'tip', kind = 'hist')

# bivariate kde plot
# smooths both x and y using 2D gaussian
sns.kdeplot(data = tips, x = 'total_bill', y = 'tip')
