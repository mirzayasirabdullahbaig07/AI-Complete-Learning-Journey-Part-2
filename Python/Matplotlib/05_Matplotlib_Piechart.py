# Pie Chart Examples
# ------------------
# A Pie Chart is used to represent **proportional data**.
# It is ideal for **categorical data** where you want to show **parts of a whole**.

import pandas as pd
import matplotlib.pyplot as plt

# 1. Basic Pie Chart Example
data = [23, 35, 65, 58, 42, 21]
subjects = ['Maths', 'English', 'Urdu', 'Biology', 'Physics', 'Chemistry']

plt.figure(figsize=(6, 6))
plt.pie(data, labels=subjects, autopct='%1.1f%%', startangle=90)
plt.title("Subject-wise Score Distribution")
plt.show()

# 2. Pie Chart from CSV (e.g., batsman runs)
df = pd.read_csv("gayle-175.csv")

# Optional: preview the DataFrame
print(df)

# Pie chart showing batsman run distribution
plt.figure(figsize=(8, 8))
plt.pie(df['batsman_runs'],
        labels=df['batsman'],
        autopct='%0.1f%%',
        colors=['blue', 'green', 'yellow', 'red', 'pink', 'orange'],
        startangle=140)
plt.title("Run Contribution per Batsman")
plt.show()

# 3. Pie Chart with Explode and Shadow
# Explode the first slice (typically to highlight)
explode_values = [0.1, 0, 0, 0, 0, 0]  # Adjust size and length as needed

plt.figure(figsize=(8, 8))
plt.pie(df['batsman_runs'],
        labels=df['batsman'],
        autopct='%0.1f%%',
        explode=explode_values,
        shadow=True,
        startangle=140)
plt.title("Run Distribution with Highlight")
plt.show()

# 4. Optional: Check Available Plot Styles
print("Available Styles:\n", plt.style.available)

# 5. Apply a Predefined Style
plt.style.use('fivethirtyeight')
