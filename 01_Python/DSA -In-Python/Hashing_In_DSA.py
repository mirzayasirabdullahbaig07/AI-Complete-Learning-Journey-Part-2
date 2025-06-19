# ================================
# 🔑 What is Hashing in DSA?
# ================================

# Hashing is a technique used to map data (keys) to a fixed-size structure (hash table)
# using a special function called a hash function.
# It allows fast access, insertion, and deletion operations — usually in O(1) time.

# ==========================================
# ❓ Why Hashing is Important and Its Need
# ==========================================

# - Linear Search takes O(n) time in the worst case.
# - Binary Search is faster with O(log n) time, but it requires sorted data.
# - Hashing provides constant time complexity O(1) on average for:
#   * Search
#   * Insert
#   * Delete
# Hence, hashing is crucial when working with large datasets efficiently.

# ==========================================
# 🔍 Comparison of Searching Techniques
# ==========================================

# | Method         | Time Complexity | Sorting Required? |
# |----------------|------------------|-------------------|
# | Linear Search  | O(n)             | No                |
# | Binary Search  | O(log n)         | Yes               |
# | Hashing        | O(1) (avg case)  | No                |

# ========================================
# ⚠️ Issue in Simple Hashing (Direct Mapping)
# ========================================

# Let's say we want to store values: {1, 2, 3, 10000}
# If we use direct indexing (array[key] = value), it would require an array of size 10001.
# Even though we only store 4 values, memory is wasted on unused indices.
# This leads to high space complexity and inefficiency.

# =================================
# ✅ Solution: Use a Hash Function
# =================================

# Instead of using direct indices, we use a hash function like:
# Example:
#     index = key % table_size
#     e.g., 10000 % 10 = 0, so key 10000 is stored at index 0.

# This way, we reduce the size of the table and avoid memory wastage.

# =====================================
# 📌 Hashing Collision Resolution Methods
# =====================================

# Some techniques used to handle collisions (when multiple keys map to the same index):
# - Chaining
# - Open Addressing
# - Linear Probing
# - Quadratic Probing
# - Double Hashing

# (These techniques will be discussed in detail below.)
