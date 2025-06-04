# What is DSA?
# DSA (Data Structures and Algorithms) helps in writing optimized and scalable programs.

# DSA is used to write efficient programs.

# How to create data types in Python using DSA concepts?
# You’ll learn concepts like hashing, time complexity, searching, sorting, and many other skills.

# DATA STRUCTURES AND ALGORITHMS
# This is very important for software development and your career.

# How efficient is your code for real-world projects?

# Time complexity and space complexity

# 01 = What is efficiency in programming?
# Efficiency can be measured by evaluating the time and space a program consumes.

# Always remember to optimize for both time and space.

# Example of time efficiency:
# Google Search Engine - It ranks web pages and gives results in 0.5 seconds.
# Google's fast response time is an example of excellent time efficiency.
# Google uses the PageRank algorithm.

# Example of space efficiency:
# A mobile game was 3.2 GB in size, and it crashed on low-end devices.
# Later, companies like Gameloft released lighter versions like Asphalt Lite and Facebook Lite to reduce space usage and increase accessibility.

# Another example of space efficiency:
# Imagine you're Mark Zuckerberg (CEO of Facebook), hiring a programmer to optimize a CSS file from 20 KB to a smaller size.
# Developer A says 19 KB and asks 10 Lacs. Developer B says 18 KB and asks for 30 Lacs.

# Facebook has ~200 Cr Daily Active Users.
# Each user loading a 1 KB smaller file means: 200 * 10^7 * 1 KB saved = 2000 GB saved daily.
# Over a year, this adds up significantly.
# With cloud bandwidth costing ₹10 per GB, a yearly saving of 73 Lacs is achieved.
# So, even if Developer B is more expensive, he saves much more in infrastructure cost.

# So space efficiency also matters a lot.


# Today’s focus is all about Time Efficiency.
# Techniques to measure time efficiency:

# Measuring time to execute
# Counting operations involved
# Abstract notion of order of growth


# 1- Measuring Time
import time
start = time.time()
for i in range(1, 101):
    print(i)
print(time.time() - start)

# But this technique is not reliable.
# It varies by machine performance (RAM, storage, CPU speed).

# Another variation using while loop
import time
start = time.time()
i = 1
while i < 101:
    print(i)
    i += 1
print(time.time() - start)

# Though both achieve the same result, the method changes the time.

# As programs get complex, it's hard to pinpoint exactly what increased the time.

# This approach is not preferred in the industry:
# Pros:
# Shows time differences for different algorithm types.

# Cons:
# Time varies with implementation.
# Time differs on different machines.
# Not reliable for small input sizes.
# Input size changes don’t show a consistent relationship in timing.


# 2- Counting operations
# Assume these operations take constant time:
# - Mathematical operations
# - Comparison operations
# - Memory access

# Count number of operations as a function of input size.

# Example 1
def c_to_f(c):
    return c * 9.0 / 5 + 3

# Example 2
def mysum(x):
    total = 0
    for i in range(x + 1):
        total += i
    return total

# Pros:
# Shows different operations for different algorithms.
# Machine-independent.
# Input variation gives better insights.

# Cons:
# Changes if code is implemented differently.
# No clear rule for which operations to count.


# 3- Abstract notion: Order of Growth

# Different inputs can drastically change how the program behaves.

# Example: Searching an element in a list
def search_for_element(L, e):
    for i in L:
        if i == e:
            return True
    return False

# Best Case: e is at the beginning.
# Worst Case: e is not in the list.
# Average Case: e is somewhere in the middle.

# In DSA, we usually analyze the **worst case**.

# Goals of Order of Growth approach:
# - Evaluate program efficiency for large inputs.
# - Express how runtime grows as input size increases.
# - Use a tight upper bound for growth rate.
# - No need to measure exact time.
# - Focus on dominant term in complexity expression.

# Hence, we use Big O notation for this.


# Example: Factorial function
def fact_iter(n):
    answer = 1
    while n > 1:
        answer *= n
        n -= 1
    return answer

# Number of steps: 1 + 5n
# Remove constants: → 5n
# Drop coefficient: → O(n) → Linear time


# More Examples:

# Expression: n^2 + 2n + 2
# Drop constants → n^2 + 2n
# Drop coefficients → n^2 + n
# Drop smaller terms → O(n^2) → Quadratic time

# Expression: n^2 + 100000n + 3^1000
# Ignore constants and lower-order terms → O(n^2)

# Expression: log(n) + n + 4
# Drop constants → O(n)

# Expression: 0.0001 * n * log(n) + 300n
# Drop constants and lower-order term → O(n log n)

# Expression: 2n^30 + 3n
# Exponential growth → O(2^n^30) is worse than polynomial → O(n)


# Common Orders of Growth:
# Constant Time - O(1)
# Linear Time - O(n)
# Quadratic Time - O(n^2)
# Logarithmic Time - O(log n)
# Linearithmic Time - O(n log n)
# Exponential Time - O(2^n)

# Give me 2 examples each for these growth types and explain which is best in DSA/programming.


# O(1) – Constant Time
# The execution time doesn't increase with input size.

# Examples:
# Accessing an element in an array by index
# → No matter the size of the array, arr[1000] takes the same time.

# Checking if a number is even or odd
# → num % 2 == 0 runs in constant time regardless of the number’s size.

# Best for efficiency. Ideal when achievable.


# O(n) – Linear Time
# Time increases directly in proportion to input size.

# Examples:
# Reading each book in a shelf of n books one by one.
# → More books = more time.

# Summing numbers from 1 to n by adding each individually.
# → More numbers = more loop iterations.

# Good for medium-sized tasks.


# 🪜 O(log n) – Logarithmic Time
# Time increases slowly even as input grows large.

# Examples:
# Binary Search on a sorted list.
# → Each step cuts the input in half.

# Guessing a number between 1 to 100 using divide-and-conquer.
# → First guess 50 → then 25 or 75 → and so on.

# Highly efficient for large datasets.


# O(n log n) – Linearithmic Time
# Combination of linear and logarithmic growth. Common in efficient sorting.

# Examples:
# Merge Sort or Heap Sort on n items.

# Building a balanced tree from unsorted data.

# Standard for optimized sorting and some search algorithms.


# O(n²) – Quadratic Time
# Time increases as the square of input size.

# Examples:
# Comparing every student with every other student in a class (pairwise comparison).

# Basic Bubble Sort / Selection Sort.

# Becomes slow quickly — avoid for large inputs.


# O(2ⁿ) – Exponential Time
# Time doubles with each additional input item.

# Examples:
# Solving the Traveling Salesman Problem using brute-force.

# Generating all possible subsets of a set.

# Becomes unusable even for moderately large inputs.


# O(n!) – Factorial Time
# Worse than exponential. Grows extremely fast.

# Examples:
# Generating all possible permutations of n elements.

# Solving puzzles like the n-Queens problem using brute-force.

# Avoid at all costs unless n is extremely small (like 5–10).


# Which is best in DSA & programming?
# Best: O(1), O(log n), O(n)
# → Scalable and efficient

# Good in practice: O(n log n)
# → Used in many real-world problems like sorting

# Avoid for large inputs: O(n²) and worse
# → Only acceptable for small data sets or unavoidable use cases
