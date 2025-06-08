# What are Arrays in DSA?
# Arrays are linear data structures.
# They store multiple items of the same data type in contiguous memory locations.

# For example, if you want to store the marks of 100 students,
# an array will occupy 100 continuous memory blocks to store those values.
# These memory locations are sequential like: 1000, 1001, 1002, 1003, and so on.
# If you know the base (first) memory address, you can access any element using indexing.

# Advantages of Arrays:
# - Fast access to elements using index.
# - Efficient memory usage when size is known.
# - Simple implementation.

# Disadvantages of Arrays:
# - Fixed size: You must define the size at the time of declaration.
# - Homogeneous: Can only store elements of the same data type.
# - Lack of flexibility in resizing.
# - Insertion and deletion operations are costly in terms of time complexity.

# ----------------------------------------------
# Call by Value (Static Arrays)
# - In a normal array, the values are stored directly in contiguous memory locations.
# - The data is tightly packed and accessed using indexing.
# - This is known as Call by Value behavior.

# ----------------------------------------------
# Referential Arrays (Call by Reference)
# - In referential arrays, actual values are stored at different memory locations,
#   like 401, 504, 609, etc.
# - The array stores memory addresses (references) instead of direct values.
# - This allows storing heterogeneous data types.

# Why do we use referential arrays?
# - Let’s say we have an array [1, 2, 3, 4, 5] with memory addresses [201, 299, 433, 665, 588].
# - If you want to replace the value at index 2 (which is 3) with a string like "Yasir",
#   you can do it because only the reference is stored.
# - The array becomes heterogeneous, but the references stay consistent.
# - Python lists are a real-world example of referential arrays.

# Disadvantages of Referential Arrays:
# - Extra memory is required to store references.
# - Slightly slower performance due to indirect access.

# ----------------------------------------------
# Dynamic Arrays
# - Dynamic arrays solve the fixed-size limitation of static arrays.
# - You don’t need to define the size in advance.
# - When the current array is full and a new element is added,
#   a larger array is created (usually double the size),
#   and all existing elements are copied to the new array.

# Example:
# Initial static array = [1]
# Add element 2 → resize to size 2 → [1, 2]
# Add element 3 → resize to size 4 → [1, 2, 3, _]

# Notes:
# - Dynamic arrays automatically resize in the background.
# - Python lists are also implemented as dynamic arrays internally.

# Summary:
# Arrays are foundational data structures.
# Static arrays use contiguous memory and are efficient for fixed-size data.
# Referential arrays (like Python lists) allow flexibility and heterogeneous types.
# Dynamic arrays solve size limitations, making them ideal for flexible applications.
