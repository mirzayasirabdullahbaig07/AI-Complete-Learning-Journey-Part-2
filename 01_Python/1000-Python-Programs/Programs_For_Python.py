
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

