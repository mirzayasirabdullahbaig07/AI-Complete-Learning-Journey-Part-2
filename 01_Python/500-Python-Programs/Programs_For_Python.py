
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

# 6. Write a program to check the data type of user input.
user_input = input("Enter something: ")
print("Data type of input is:", type(user_input))  # always str unless converted

# 7. Multiply a string by a number and display the result.
multiply_string = "yasir"
print(multiply_string * 2)  # Output: yasiryasir

# 8. Concatenate integer and string types after conversion.
num = 10
text = " is my lucky number"
result = str(num) + text
print(result)  # Output: 10 is my lucky number

# 9. Store and print your age using a variable.
my_Age = 24
print(my_Age)

# 10. Check if a variable is of type int.
a = 7
print(type(a) == int)  # True

# 11. Convert a number into a string and add it to another string.
a = 2              # integer
b = str(a)         # convert integer to string, b = "2"
c = "yasir"        # string
d = b + c          # string concatenation: "2" + "yasir"
print(d)           # Output: 2yasir

# 12. Write a program to accept your name and roll number and display them.
student_name = input("Enter your name: ")
student_roll_no = int(input("Enter your roll number: "))
print("Name:", student_name)
print("Roll Number:", student_roll_no)

# 13. Check whether the input is an integer or a float.
value = input("Enter a number: ")
try:
    int_val = int(value)
    print("It's an integer.")
except ValueError:
    try:
        float_val = float(value)
        print("It's a float.")
    except ValueError:
        print("It's neither int nor float.")

# 14. Take input from the user and print it in reverse order.
user_input = input("Enter something to reverse: ")
reverse_str = user_input[::-1]
print("Reversed:", reverse_str)

# 15. Display the memory address of a variable.
variable_memory = [1, 2, 3, 4, 5]
print("Memory address:", id(variable_memory))

# ============================================
#  B. Operators (Arithmetic, Comparison, Logical) — 20 Questions
# Goal: Logic Building, DSA, and Python Mastery
# ============================================

# 16. Perform all arithmetic operations on two numbers.
num_arth = 2
num_arth1 = 4
print(num_arth + num_arth1)    # Addition
print(num_arth * num_arth1)    # Multiplication
print(num_arth - num_arth1)    # Subtraction
print(num_arth / num_arth1)    # Division
print(num_arth % num_arth1)    # Modulo

# 17. Write a program to find the square and cube of a number.
num_square = int(input("Enter your number: "))
print("Square:", num_square ** 2)
print("Cube:", num_square ** 3)

# 18. Use comparison operators to check if two numbers are equal.
number_checker = int(input("Enter num 1: "))
number_checker2 = int(input("Enter num 2: "))
if number_checker == number_checker2:
    print("Equal")
else:
    print("Not equal")

# 19. Check if a number is greater than 10 and less than 50 using logical operators.
num_op = int(input("Enter a number: "))
if num_op > 10 and num_op < 50:
    print("Number is between 10 and 50")
else:
    print("Number is NOT in the range (10, 50)")

# 20. Demonstrate and, or, and not operators with examples.
a = 5
b = 10
c = 15

# AND operator
print((a < b) and (b < c))  # True

# OR operator
print((a > b) or (b < c))   # True

# NOT operator
print(not(a > b))           # True

# 21. Write a program to divide two numbers and round the result to 2 decimal places.
num_div1 = int(input("Enter your first number: "))
num_div2 = int(input("Enter your second number: "))
print(round(num_div1 / num_div2, 2))

# 22. Find the remainder without using the % operator.
num_for_division = 101
divisor = 6
remainder = num_for_division - (divisor * (num_for_division // divisor))
print("Remainder is:", remainder)

# 23. Write a program that checks whether two strings are equal.
str_one = "yasir"
str_one1 = "ABDULLAH"
if str_one == str_one1:
    print("equal")
else:
    print("not equal")

# 24. Check if the number is even using the modulus operator.
number_even = int(input("Enter the number: "))
if number_even % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

# 25. Write a program that calculates simple interest.
principal = 10
rate = 500
time = 60
simple_interest = (principal * rate * time) / 100
print("Simple Interest is:", simple_interest)

# 26. Multiply two floating-point numbers.
floating_point_num = 0.99
floating_point_num1 = 2.43
print(floating_point_num * floating_point_num1)

# 27. Write a program to check if a number is positive, negative, or zero.
number_checker_01 = int(input("Enter the number: "))
if number_checker_01 > 0:
    print("The number is positive")
elif number_checker_01 < 0:
    print("The number is negative")
else:
    print("The number is zero")

# 28. Convert minutes into hours using arithmetic.
total_mins = 180
print(total_mins / 60, "hours")

# 29. Write a program to calculate the perimeter of a rectangle.
width_of_rect = 10
height_of_rect = 5
print("Perimeter of rectangle is:", 2 * (width_of_rect + height_of_rect))

# 30. Write a program to increase a salary by 10% using operators.
total_salary = 500000
increased_salary = total_salary + (total_salary * 10 / 100)
print("Increased salary is:", increased_salary)

# 31. Use exponent operator to calculate power.
comp_num1 = 4
comp_num2 = 3
print(comp_num1 ** comp_num2)

# 32. Write a program to find the average of three numbers.
avg_num1 = 3
avg_num2 = 4
avg_num3 = 5
avg = (avg_num1 + avg_num2 + avg_num3) / 3
print("Average is:", avg)

# 33. Write a program that finds the largest of two numbers using ternary operator.
num_largest_finder = int(input("Enter first number: "))
num_largest_finder1 = int(input("Enter second number: "))
print("Largest number is:", num_largest_finder if num_largest_finder > num_largest_finder1 else num_largest_finder1)

# 34. Check if a number is divisible by both 3 and 5.
divisible_number = int(input("Enter the number: "))
if divisible_number % 3 == 0 and divisible_number % 5 == 0:
    print("The number is divisible by both 3 and 5")
else:
    print("The number is not divisible by both 3 and 5")

# 35. Calculate the Body Mass Index (BMI) using given formula.
weight = 65  # in kg
height = 1.68  # in meters
bmi = weight / (height ** 2)
print("BMI is:", round(bmi, 2))



# C. Input & Output (15 Questions)

# 36.	Take name input from the user and greet them.
greet_input = input("enter your name")
print(greet_input, "welcome to the python program")

# 37.	Take age input and calculate the year when user will turn 100.
age = int(input("Enter your age: "))
current_year = 2025
year_when_100 = current_year + (100 - age)
print(f"You will turn 100 years old in the year {year_when_100}.")

# 38.	Accept three numbers and print their sum.
get_num1 = int(input("Enter first number: "))
get_num2 = int(input("Enter second number: "))
get_num3 = int(input("Enter third number: "))
result = get_num1 + get_num2 + get_num3
print("The sum is:", result)

# 39.	Read two strings and concatenate them with a space.
str1 = "my name is yasir"
str2 = "my age is 24"
print(str1 + " " + str2)

# 40.	Take user input in one line and split them into separate variables.
a, b, c = input("Enter three numbers separated by space: ").split()
print("First:", a)
print("Second:", b)
print("Third:", c)

# 41.	Take a number as input and print it as float.
input_float = float(input("enter the value"))
print(input_float)

# 42.	Read a sentence and print its first word.
sentence = "yasir abdullah"
first_word = sentence.split()[0]
print(first_word)

# 43.	Format a sentence using variables (f-strings).
a = "yasir"
b = "abdullah"
print(f"this is {a} and {b}")

# 44.	Display your full name in reverse order.
name_reverse = "yasir"
print(name_reverse[::-1])

# 45.	Take 3 numbers from the user and print their multiplication.
take_first_num = int(input("enter the first number"))
take_sec_num = int(input("enter the second number"))
take_third_num = int(input("enter the third number"))
print(take_first_num * take_sec_num * take_third_num)

# 46.	Write a program to print user age after 5 years.
user_age = int(input("enter the age"))
age_after_5 = user_age + 5
print(age_after_5)

# 47.	Take a floating number from user and round it to the nearest integer.
floating_num = float(input("Enter a float number: "))
rounded = round(floating_num)
print(rounded)

# 48.	Accept temperature in Celsius and convert to Fahrenheit.
celsius_temp = float(input("Enter temperature in Celsius: "))
fahrenheit_temp = (celsius_temp * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit_temp}")

# 49.	Print a line 5 times using a single print statement.
single_statement = "My name is yasir"
print(("This is a repeated line.\n" * 5).strip())

# 50.	Take input of a product name and its price, then print a bill
product_name = "SOAP"
price = 100
print(f"the {product_name} price is {price}")


# ✅ PART 2: Conditional Statements (if, elif, else) — 50 Logic-Building Questions
# These questions will help you strengthen your decision-making and logic-building skills in Python using conditional statements.
# ________________________________________
# 📌 A. Basic If Conditions (25 Questions)

# 51.	Check if a number is positive.
even_checker = int(input("Enter the number: "))
if even_checker > 0:
    print("This is a positive number")
else: 
    print("The number is not positive")

# 52.	Check if a number is odd or even.
number_check = int(input("Enter the number: "))
if number_check % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# 53.	Check if a number is divisible by 7.
checker_divisble = int(input("Enter the number: "))
if checker_divisble % 7 == 0:    print("The number is divisible by 7")
else:
    print("The number is not divisible by 7")

# 54.	Check if a person is eligible to vote (age ≥ 18).
vote_checker_age = int(input("Enter the age: "))
if vote_checker_age >= 18:
    print("He is eligible to vote")
else:
    print("He is not eligible to vote")

# 55.	Check if a number is a single-digit number.
checker_number_size = int(input("Enter the number: "))
if -9 <= checker_number_size <= 9:
    print("Number is a single-digit number")
else:
    print("This is not a single-digit number")

# 56. Check if a given year is a leap year
the_current_year = int(input("Enter a year to check if it's a leap year: "))
if (the_current_year % 4 == 0 and the_current_year % 100 != 0) or (the_current_year % 400 == 0):
    print("This is a leap year\n")
else:
    print("This is not a leap year\n")

# 57. Check if a given character is a vowel or consonant
vowel_checker = input("Enter a character to check if it's a vowel: ").lower()
if len(vowel_checker) == 1 and vowel_checker.isalpha():
    if vowel_checker in ['a', 'e', 'i', 'o', 'u']:
        print("This is a vowel\n")
    else:
        print("This is a consonant\n")
else:
    print("Invalid input. Please enter a single alphabet character.\n")

# 58. Check if a string is empty or not
empty_string = input("Enter a string to check if it's empty: ")
if empty_string == "":
    print("This is an empty string\n")
else:
    print("This is not an empty string\n")

# 59. Check if a number is less than 100 and greater than 50
checker_number_len = int(input("Enter a number: "))
if 50 < checker_number_len < 100:
    print("The number is greater than 50 and less than 100\n")
else:
    print("The number is not in the range (50, 100)\n")

# 60. Accept a password and check if it matches the stored password
password_store = "yasir123"
entered_password = input("Enter your password: ")
if entered_password == password_store:
    print("The password is correct\n")
else:
    print("Password is wrong\n")


    # the pending questions will be provided here
    ### so be in touch



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