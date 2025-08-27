# ============================================
# --------------------------------------------
# 500 Python Program Basic to Advanced Level
# ============================================
# --------------------------------------------


# Every Part have multiple sections of a particular concept and all the questions are in sequences


# ============================================
# PART 1: Python Basics (Variables, Data Types, Operators) — 50 Questions
# ============================================

# --------------------------------------------
# A. Variables & Data Types (15 Questions)
# --------------------------------------------

# 1.	Declare a variable with your name and print it.
varName = "Mirza Yasir Abdullah Baig"
print(varName)

# 2.	Swap two variables without using a third variable.
aVar = "Yasir"
bVar = "Abdullah"
aVar, bVar = bVar, aVar
print(aVar, bVar)

# 3.	Convert a string into an integer.
str_ = "Mirza Yasir Adullah Baig"
str_int = int(str_)
print(str_int)

# 4.	Store the result of a float division in an integer variable.
float_ = 0.07
float_int = int(float_)
print(float_int)

# 5.	Convert a given integer to binary, octal, and hexadecimal.
intVar = 7
int_binary = bin(intVar)
int_octal = oct(intVar)
int_hexadecimal = hex(intVar)
print(int_binary, int_octal, int_hexadecimal)

# 6.	Write a program to check the data type of user input.
user_ = input("Mirza Yasir Abdullah Baig")
print(type(user_))

# 7.	Multiply a string by a number and display the result.
str_multiply = "Yasir"
print(str_multiply * 3)

# 8.	Concatenate integer and string types after conversion.
int_ = 7
str_ = "yasir"
result = str(int_) + " " + str_
print(result)

# 9.	Store and print your age using a variable.
age_ = 24
print(age_)

# 10.	Check if a variable is of type int.
var_ = 7
print(type(var_))

# 11.	Convert a number into a string and add it to another string.
var_ = 7
str_ = "Yasir"
str_var = str(var_)
result = str_ + " " + str_var
print(result)

# 12.	Write a program to accept your name and roll number and display them.
name_enter = str(input("enter your name = "))
roll_number = int(input("enter your roll number = "))
display_name = name_enter, roll_number
print(display_name)

# 13.	Check whether the input is an integer or a float.
input_ = input("enter the value = ")
print(type(input_))

# 14.	Take input from the user and print it in reverse order.
input_ = input("enter the value = ")
reversed = input_[::-1]
print(reversed)

# 15.	Display the memory address of a variable.
value_ = "Yasir"
print(id(value_))

# --------------------------------------------
# B. Operators (Arithmetic, Comparison, Logical) — 20 Questions
# --------------------------------------------
