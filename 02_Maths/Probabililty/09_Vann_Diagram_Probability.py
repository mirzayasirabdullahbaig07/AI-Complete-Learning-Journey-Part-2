# -------------------------------
# Venn Diagrams in Probability
# -------------------------------
# A Venn diagram is a visual way to represent sets and their relationships.
# In probability, sets represent events, and the diagram helps us understand
# how events overlap (intersections), combine (unions), or remain separate.

# -------------------------------
# Set Theory Basics
# -------------------------------
# 1. Universal Set (U): 
#    The set of all possible outcomes of an experiment. 
#    Example: Tossing a die → U = {1, 2, 3, 4, 5, 6}
#
# 2. Subset (A ⊆ U):
#    A set that contains some (or all) outcomes from the universal set.
#    Example: A = {2, 4, 6} (event of rolling an even number)
#
# 3. Complement (A'):
#    The set of outcomes that are in U but not in A.
#    Example: A' = {1, 3, 5} (event of rolling an odd number)
#
# 4. Union (A ∪ B):
#    All outcomes in either A or B (or both).
#    Example: A = {2, 4, 6}, B = {1, 2} → A ∪ B = {1, 2, 4, 6}
#
# 5. Intersection (A ∩ B):
#    Outcomes that are in both A and B.
#    Example: A = {2, 4, 6}, B = {1, 2} → A ∩ B = {2}
#
# 6. Probability of Universal Set:
#    P(U) = 1 (since the universal set contains all possible outcomes)

# -------------------------------
# Venn Diagram Example (Conceptual)
# -------------------------------
# Tossing a die → U = {1, 2, 3, 4, 5, 6}
#
# Let A = {2, 4, 6} → Event: rolling even number
# Let B = {1, 2, 3} → Event: rolling ≤ 3
#
# Union: A ∪ B = {1, 2, 3, 4, 6}
# Intersection: A ∩ B = {2}
# Complement of A: A' = {1, 3, 5}
#
# Venn Diagram visually shows:
# - Circle A overlaps Circle B at {2}
# - All outcomes remain inside universal set U

# -------------------------------
# Python Example with Sets
# -------------------------------
U = {1, 2, 3, 4, 5, 6}
A = {2, 4, 6}
B = {1, 2, 3}

print("Universal Set U:", U)
print("Set A (even numbers):", A)
print("Set B (numbers ≤ 3):", B)
print("A ∪ B (Union):", A.union(B))
print("A ∩ B (Intersection):", A.intersection(B))
print("A' (Complement of A):", U - A)
