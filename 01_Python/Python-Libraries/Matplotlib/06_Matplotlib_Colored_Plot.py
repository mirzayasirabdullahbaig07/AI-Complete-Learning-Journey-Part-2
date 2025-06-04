# -------------------------------------------------------------
# Colored Scatter Plot Using Iris Dataset
# -------------------------------------------------------------

# Libraries Used:
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
iris = pd.read_csv('/content/Iris.csv')  # Load the dataset
iris.sample(5)  # Show 5 random samples to understand data structure

# 2. Basic Scatter Plot (No color distinction)
plt.scatter(iris['SepalLengthCm'], iris['PetalLengthCm'])
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')
plt.title('Basic Scatter Plot')
plt.show()

# 3. Encode Target Variable
# Convert Species from text to numeric labels for visualization
iris['Species'] = iris['Species'].replace({
    'Iris-virginica': 0,
    'Iris-versicolor': 1,
    'Iris-setosa': 2
})
iris.sample(5)

# 4. Colored Scatter Plot
# Each class of species is shown in different color using 'c' parameter
plt.figure(figsize=(15, 7))
plt.scatter(
    iris['SepalLengthCm'],
    iris['PetalLengthCm'],
    c=iris['Species'],             # Color depends on species
    cmap='winter',                 # Color map
    alpha=0.3                      # Transparency
)

# Add plot labels and color bar
plt.xlabel('SepalLengthCm')
plt.ylabel('PetalLengthCm')
plt.title('Colored Scatter Plot of Iris Species')
plt.colorbar(label='Species')
plt.show()
