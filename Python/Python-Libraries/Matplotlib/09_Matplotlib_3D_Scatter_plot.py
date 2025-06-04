# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# ---------------------------
# Load Batter Dataset
# ---------------------------
batters = pd.read_csv('/content/batter.csv')

# ---------------------------
# 3D Scatter Plot: runs vs avg vs strike_rate
# ---------------------------
# Create a 3D scatter plot to visualize batters' performance
fig = plt.figure()
ax = plt.subplot(projection='3d')  # Create a 3D subplot
ax.scatter(batters['runs'], batters['avg'], batters['strike_rate'])

# Add labels and title
ax.set_title("3D Scatter Plot: Batters' Performance")
ax.set_xlabel('Runs')
ax.set_ylabel('Average')
ax.set_zlabel('Strike Rate')  # Needed for 3D Z-axis

# ---------------------------
# 3D Line and Scatter Plot with Sample Data
# ---------------------------
x = [0, 1, 6, 3]
y = [0, 6, 5, 5]
z = [0, 2, 9, 4]

fig = plt.figure()
ax = plt.subplot(projection='3d')
ax.scatter3D(x, y, z, s=(100, 100, 100, 100))  # 3D scatter with size
ax.plot3D(x, y, z)  # 3D line connecting the points

# ---------------------------
# 3D Surface Plot
# ---------------------------
# Create a meshgrid for surface plotting
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
xx, yy = np.meshgrid(x, y)

# Define a 3D surface: z = x^2 + y^2
z = xx**2 + yy**2

# Plot the surface
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(projection='3d')
q = ax.plot_surface(xx, yy, z, cmap='viridis')  # Surface plot with color map
fig.colorbar(q)  # Add color bar to indicate z values

# ---------------------------
# Another 3D Surface: sin(x) + cos(y)
# ---------------------------
z = np.sin(xx) + np.cos(yy)
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot(projection='3d')
q = ax.plot_surface(xx, yy, z, cmap='viridis')

# ---------------------------
# 2D Contour Plot (converted from 3D)
# ---------------------------
# This plot shows the 3D surface in 2D using filled contours
fig = plt.figure(figsize=(12, 8))
ax = plt.subplot()
q = ax.contourf(xx, yy, z, cmap='viridis')  # Filled contour plot
fig.colorbar(q)  # Show the scale of values

# ---------------------------
# Load IPL Dataset
# ---------------------------
record = pd.read_csv("/content/IPL_Ball_by_Ball_2008_2022.csv")

# ---------------------------
# Filter Data: Only sixes in first 6 balls of an over
# ---------------------------
temp_dp = record[(record['ballnumber'].isin([1, 2, 3, 4, 5, 6])) & 
                 (record['batsman_run'] == 6)]

# ---------------------------
# Create Pivot Table for Heatmap
# ---------------------------
# Pivot table: counts of sixes per over and ball number
grid = temp_dp.pivot_table(index='overs', 
                           columns='ballnumber', 
                           values='batsman_run', 
                           aggfunc='count')

# ---------------------------
# Visualize with Heatmap
# ---------------------------
plt.figure(figsize=(12, 8))
plt.imshow(grid, cmap='viridis', aspect='auto')  # Heatmap using imshow
plt.colorbar()  # Color scale legend
plt.title("Number of Sixes per Ball Number in Each Over")
plt.xlabel("Ball Number")
plt.ylabel("Overs")

# ---------------------------
# Optional: Improve with Seaborn
# ---------------------------
# sns.heatmap(grid, annot=True, cmap='viridis')  # Better alternative
