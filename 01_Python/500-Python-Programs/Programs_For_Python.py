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

# 16.	Perform all arithmetic operations on two numbers.
num1 = 5
num2 = 4
print("addition:", num1 + num2)
print("substraction:", num1 - num2)
print("multiplication:", num1 * num2)
print("division:", num1 / num2)
print("modulus:", num1 % num2)

# 17.	Write a program to find the square and cube of a number.
num_ = 5
print(num_ * num_)
print(num_** num_)

# 18.	Use comparison operators to check if two numbers are equal.
num1 = 5
num2 = 4
print(num1 == num2)

# 19.	Check if a number is greater than 10 and less than 50 using logical operators.
num1 = 4
if num1 > 10 and num1 < 50:
    print("number is under 50")
else:
    print("number is smaller than 10 or greater than 50")

# 20.	Demonstrate and, or, and not operators with examples. 
num1 = 5
num2 = 4
if num1 > 2 and num2 > 2:
    print("AND: Both conditions are True")
if num1 < 3 or num2 < 10:
    print("OR: At least one condition is True")
if not num1 > 10:
    print("NOT: Condition is False, so this runs")

# 21.	Write a program to divide two numbers and round the result to 2 decimal places.
num1 = 2
num2 = 4
result = (num1/num2)
print(round(result, 2))

# 22.	Find the remainder without using the % operator.
num1 = 2
num2 = 4
quotient = num1 // num2
remainder = num1 - (num2 * quotient)
# remainder = dividend – (divisor × quotient)
print(remainder)

# 23.	Write a program that checks whether two strings are equal.
str_1 = "Yasir"
str_2 = "Baig"
print(str_1 == str_2)

# 24.	Check if the number is even using the modulus operator.
num1 = 33
print(num1 % 2 == 0)

# 25.	Write a program that calculates simple interest.
principal = 60000
rate = 5       # 5% per year
time = 2       # 2 years
interest = (principal * rate * time) / 100
print("Simple Interest:", interest)

# 26.	Multiply two floating-point numbers.
num1 = 34.5
num2 = 343.5
print(num1 * num2)

# 27.	Write a program to check if a number is positive, negative, or zero.
input_num = int(input("enter the number = "))
if input_num > 0:
    print("The number is Positive")
elif input_num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

# 28.	Convert minutes into hours using arithmetic.
minutes = 500
hours = minutes // 60       # whole hours
remaining_minutes = minutes % 60   # leftover minutes
print(f"{hours} hours and {remaining_minutes} minutes")

# 29.	Write a program to calculate the perimeter of a rectangle.
rectangle_len = 5.5
rectangle_width = 3
perimeter = 2 * (rectangle_len + rectangle_width)
print("Perimeter of Rectangle:", perimeter)

# 30.	Write a program to increase a salary by 10% using operators.
# new salary=old salary+(old salary×0.10)
total_salary = 600000
new_salary = total_salary * 1.10
print("Old Salary:", total_salary)
print("New Salary after 10% increment:", new_salary)

# 31.	Use exponent operator to calculate power.
num1 = 4
print(num1 ** 3)

# 32.	Write a program to find the average of three numbers.
num1 = 3
num2 = 4
num3 = 5
average_Num = ((num1 + num2 + num3 )/ 3) 
print(average_Num)

# 33.	Write a program that finds the largest of two numbers using ternary operator.
num1 = 4
num2 = 5
largest = num1 if num1 > num2 else num2
print("Largest number is:", largest)

# 34.	Check if a number is divisible by both 3 and 5.
num1 = int(input("Enter the number: "))
if num1 % 3 == 0 and num1 % 5 == 0:
    print("This number is divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

# 35.	Calculate the Body Mass Index (BMI) using given formula.
# Input weight (kg) and height (m)
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print("Your BMI is:", round(bmi, 2))

# --------------------------------------------
# C. Input & Output (15 Questions)
# --------------------------------------------

# 36.	Take name input from the user and greet them.
user_input = input("What is your name? ")
print("Hello", user_input + "!", "Welcome ")
# 37.	Take age input and calculate the year when user will turn 100.
from datetime import datetime
user_age = int(input("What is your age? "))
current_year = datetime.now().year
year_turn_100 = current_year + (100 - user_age)
print("You will turn 100 years old in the year:", year_turn_100)

# 38.	Accept three numbers and print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
total = num1 + num2 + num3
print("The sum of the three numbers is:", total)

# 39.	Read two strings and concatenate them with a space.
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = str1 + " " + str2
print("Concatenated string:", result)

# 40.	Take user input in one line and split them into separate variables.
x, y, z = input("Enter three numbers separated by space: ").split()
print("First value:", x)
print("Second value:", y)
print("Third value:", z)
