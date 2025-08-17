# Difference Between INDEPENDENT Events and MUTUALLY EXCLUSIVE Events
# (deep but concise, with clear examples)

# ---------------------------------------------------------------
# DEFINITIONS
# ---------------------------------------------------------------
# Independent events (A, B):
#   Knowing that B happened does NOT change the chance of A.
#   Formulas (equivalent when P(B)>0 and P(A)>0):
#     P(A | B) = P(A)
#     P(B | A) = P(B)
#     P(A ∩ B) = P(A) * P(B)

# Mutually exclusive events (A, B):
#   They CANNOT happen together in a single trial.
#   Formula:
#     A ∩ B = ∅  ⇒  P(A ∩ B) = 0
#   Note: If P(A)>0 and P(B)>0, mutually exclusive events are NOT independent
#         (because independence would require P(A ∩ B) = P(A)P(B) > 0).

# Intuition (Venn):
#   - Independent: circles overlap in proportion to their areas (product rule).
#   - Mutually exclusive: circles do not overlap at all.

# ---------------------------------------------------------------
# INDEPENDENT: WORKED EXAMPLES
# ---------------------------------------------------------------
# Example 1: Coin + Die
#   A = “coin shows Heads”  → P(A) = 1/2
#   B = “die shows 4”       → P(B) = 1/6
#   Joint: P(A ∩ B) = P(H and 4) = (1/2)*(1/6) = 1/12
#   Since P(A ∩ B) = P(A)P(B), A and B are independent.

# Example 2: Two dice (classic non-trivial independence)
#   Roll two fair dice (ordered pair).
#   A = “sum is 7” → favorable: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1) → 6/36 = 1/6
#   B = “first die is odd” → first die ∈ {1,3,5}, second die any → 18/36 = 1/2
#   A ∩ B = {(1,6),(3,4),(5,2)} → 3/36 = 1/12
#   Check: P(A)P(B) = (1/6)*(1/2) = 1/12 = P(A ∩ B)
#   ⇒ A and B are independent.

# Example 3: Cards WITH replacement (independent draws)
#   A = “first draw is an Ace” → 4/52
#   B = “second draw is an Ace (after replacing the first)” → still 4/52
#   P(A ∩ B) = (4/52)*(4/52) = P(A)P(B) ⇒ independent.

# ---------------------------------------------------------------
# DEPENDENT (for contrast): WORKED EXAMPLE
# ---------------------------------------------------------------
# Cards WITHOUT replacement (dependent draws)
#   A = “first draw is an Ace” → 4/52
#   B = “second draw is an Ace”
#   P(B | A) = 3/51 (one Ace removed)
#   P(B | Aᶜ) = 4/51 (no Ace removed)
#   Since P(B | A) ≠ P(B | Aᶜ), the second draw depends on the first.
#   Also P(A ∩ B) = (4/52)*(3/51) ≠ P(A)P(B).

# ---------------------------------------------------------------
# MUTUALLY EXCLUSIVE: WORKED EXAMPLES
# ---------------------------------------------------------------
# Example 1: Single coin toss
#   A = “Heads”, B = “Tails”
#   A ∩ B = ∅ ⇒ P(A ∩ B) = 0
#   With P(A)=P(B)=1/2, independence would require P(A ∩ B)=1/4, but it’s 0.
#   ⇒ A and B are mutually exclusive and NOT independent.

# Example 2: Single die roll
#   A = “roll a 2”, B = “roll a 5”
#   A ∩ B = ∅ ⇒ P(A ∩ B)=0 (cannot show both 2 and 5 in one roll).
#   With P(A)=P(B)=1/6, independence would require 1/36, but joint is 0.
#   ⇒ Mutually exclusive ⇒ NOT independent (unless one event has probability 0).

# ---------------------------------------------------------------
# KEY TAKEAWAYS (CHEATSHEET)
# ---------------------------------------------------------------
# Independent:
#   - Can occur together.
#   - “No information gain” on A after learning B.
#   - Product rule holds: P(A ∩ B) = P(A)P(B).

# Mutually Exclusive:
#   - Cannot occur together: P(A ∩ B) = 0.
#   - If both have positive probability, they are automatically NOT independent.
#   - The only way to be both mutually exclusive and independent is trivial:
#     one event has probability 0 (so product and joint are both 0).

# Quick self-check:
#   1) If you can see them happen simultaneously in one trial → not mutually exclusive.
#   2) If learning B changes the chance of A → not independent.
#   3) If circles overlap proportional to areas → independent; if no overlap → mutually exclusive.
