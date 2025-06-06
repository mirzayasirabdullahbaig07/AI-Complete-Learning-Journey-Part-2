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


# ---------------------------------------------
# DSA & Programming: Understanding Time Complexity
# ---------------------------------------------

# Best Time Complexities: O(1), O(log n), O(n)
# → Highly scalable and efficient

# Good in Practice: O(n log n)
# → Common in real-world problems like sorting

# Avoid for Large Inputs: O(n²) and worse
# → Acceptable only for small data sets or if unavoidable


# ---------------------------------------------
# 18 Programs to Understand Order of Growth
# ---------------------------------------------

# Program 1: Sum and Product of List Elements
L = [1, 2, 3, 4, 5]

sum = 0
for i in L:
    sum += i
print(sum)

product = 1
for i in L:
    product *= i
print(product)

# Time Complexity: O(n) + O(n) = O(2n) → O(n)
# Linear time — if input doubles, time also doubles


# Program 2: Nested Loops — Cartesian Product
L = [1, 2, 3, 4, 5]
for i in L:
    for j in L:
        print('({}, {})'.format(i, j))

# Time Complexity: O(n²)
# Quadratic — 2 nested loops → performance drops fast with input growth


# Program 3: Linear Search
# Time Complexity: O(n)
# Example: doubling array size doubles time

# Program 4: int to string conversion (logarithmic)
def intToStr(i):
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i % 10] + result
        i = i // 10
    return result

# Time Complexity: O(log n)
# Because the number is divided by 10 in each iteration


# Program 5: Nested Loop with log time inner loop
n = 1000
i = n // 3
while i <= n:
    j = 2
    while j < n:
        k = n // 2
        j *= 2
    i += 1

# Time Complexity: O(n log n)
# Outer loop = O(n), Inner loop = O(log n)


# Program 6: Binary Search (Divide and Conquer)
# Time Complexity: O(log n)
# Every step reduces the problem size by half


# Program 7: Nested Loops over List
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    for j in range(i + 1, len(L)):
        print('({}, {})'.format(L[i], L[j]))

# Time Complexity: O(n²)
# Nested loops — upper triangle of combinations


# Program 8: Compare elements from two different arrays
A = [1, 2, 3, 4]
B = [2, 3, 4, 5, 6]
for i in A:
    for j in B:
        if i < j:
            print('({}, {})'.format(i, j))

# Time Complexity: O(n²)
# Nested loops with same size input → quadratic


# Program 9: Triple Nested Loops
A = [1, 2, 3, 4]
B = [2, 3, 4, 5]
for i in A:
    for j in B:
        for k in range(100000):
            print('({}, {})'.format(i, j))

# Time Complexity: O(n² * k) → Constant loop k → Still O(n²)


# Program 10: Reverse a List
L = [1, 2, 3, 4, 5]
for i in range(0, len(L) // 2):
    other = len(L) - i - 1
    temp = L[i]
    L[i] = L[other]
    L[other] = temp
print(L)

# Time Complexity: O(n)
# Single loop over half the list — linear


# Program 11: Recursive Factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))

# Time Complexity: O(n)
# One recursive call per input unit


# Program 12: Recursive Fibonacci (naive)
def fib(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Time Complexity: O(2^n)
# Exponential — repeated subproblems, not efficient


# Program 13: Logarithmic Power Calculation
def power(num):
    if num < 1:
        return 0
    elif num == 1:
        print(1)
        return 1
    else:
        prev = power(num // 2)
        curr = prev * 2
        print(curr)
        return curr
power(45)

# Time Complexity: O(log n)
# Number gets halved every call


# Program 14: Modulo without %
def mod(a, b):
    if b <= 0:
        return -1
    div = a // b
    return a - div * b
mod(2, 4)

# Time Complexity: O(1)
# Simple arithmetic — constant time


# Program 15: Sum of Digits
def sum_digits(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    return sum
sum_digits(123)

# Time Complexity: O(log n)
# Number of digits = log(n), since base is 10


# Program 16: Exponential Recurrence Relation
# T(n) = 3T(n-1) + constant → Time Complexity: O(3^n)


# Program 17: Another Recurrence Relation
# T(n) = 2T(n-1) - 1 → Time Complexity: O(2^n)


# Program 18: Generating Power Set
# Example: [1, 2, 3]
# Output: [], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]
# Time Complexity: O(2^n)
# Exponential — each element either included or not
