# What is a Contingency Table in Probability?
# A contingency table (also called a cross-tabulation or crosstab) is a type of table in probability/statistics
# that shows the frequency distribution of variables. 
# It helps us understand the relationship between two categorical variables.

# Example:
# Suppose we roll a die 100 times with 100 students.
# We want to analyze whether the outcome is "Even" or "Odd".
# One variable = "Even/Odd" outcome
# Another variable = "Greater than 3" or "Less than or equal to 3"

# Contingency Table Example (for 100 rolls):
# ----------------------------------------------------
#               | <= 3            | > 3             | Total
# ----------------------------------------------------
# Even Numbers  | 20              | 30              | 50
# Odd Numbers   | 25              | 25              | 50
# ----------------------------------------------------
# Total         | 45              | 55              | 100
# ----------------------------------------------------
# This table shows the counts of how many outcomes fall in each category.

# Interpretation:
# - Total number of outcomes = 100 (since die rolled 100 times by students).
# - Even numbers (2,4,6) came up 50 times, Odd numbers (1,3,5) came up 50 times.
# - Among Even numbers, 20 were <= 3 (only "2"), and 30 were > 3 (like 4,6).
# - Among Odd numbers, 25 were <= 3 (1,3) and 25 were > 3 (5).
# This helps analyze probability in multiple categories at once.

# Formula Reminder:
# P(Event) = Frequency of Event / Total Outcomes
# Example: P(Even AND >3) = 30 / 100 = 0.3

# Python Code Example: Generating a contingency table
import random
import pandas as pd

# Simulating 100 rolls of a die
rolls = [random.randint(1, 6) for _ in range(100)]

# Categorizing rolls into "Even/Odd" and "<=3 or >3"
data = {
    "Even/Odd": ["Even" if r % 2 == 0 else "Odd" for r in rolls],
    "Range": ["<=3" if r <= 3 else ">3" for r in rolls]
}

# Creating a contingency table using pandas
df = pd.DataFrame(data)
contingency_table = pd.crosstab(df["Even/Odd"], df["Range"], margins=True)

print(contingency_table)
