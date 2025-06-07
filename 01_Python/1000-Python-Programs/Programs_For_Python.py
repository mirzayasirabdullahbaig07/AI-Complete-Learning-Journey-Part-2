# ============================================
# A. Variables & Data Types (15 Questions)
# Goal: Logic Building, DSA, and Python Mastery
# ============================================

# 1. Declare a variable with your name and print it.
name_variable = "Yasir"
print("1. Name Variable:", name_variable)

# 2. Swap two variables without using a third variable.
a = 5
b = 4
a = a + b
b = a - b
a = a - b
print("2. Swapped Variables -> a:", a, "b:", b)

# 3. Convert a string into an integer.
convert_string = "07"
converted_int = int(convert_string)
print("3. Converted String to Integer:", converted_int)

# 4. Store the result of a float division in an integer variable.
float_store = 0.7
int_result = int(float_store)  # Truncates the decimal part
print("4. Float to Integer:", int_result)

# 5. Convert a given integer to binary, octal, and hexadecimal.
int_value = 98
print("5. Binary:", bin(int_value))
print("5. Octal:", oct(int_value))
print("5. Hexadecimal:", hex(int_value))
