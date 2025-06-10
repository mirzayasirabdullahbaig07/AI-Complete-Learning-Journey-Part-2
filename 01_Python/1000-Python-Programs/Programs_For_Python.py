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
