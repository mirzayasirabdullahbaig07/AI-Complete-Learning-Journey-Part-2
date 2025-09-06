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

# 41. Take a number as input and print it as float.
num = input("Enter a number: ")
print(float(num))

# 42. Read a sentence and print its first word.
sentence = input("Enter a sentence: ")
print(sentence.split()[0])

# 43. Format a sentence using variables (f-strings).
name = "Yasir"
age = 20
print(f"My name is {name} and I am {age} years old.")

# 44. Display your full name in reverse order.
full_name = input("Enter your full name: ")
print(full_name[::-1])

# 45. Take 3 numbers from the user and print their multiplication.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("Multiplication:", a * b * c)

# 46. Write a program to print user age after 5 years.
age = int(input("Enter your age: "))
print("After 5 years, your age will be:", age + 5)

# 47. Take a floating number from user and round it to the nearest integer.
float_num = float(input("Enter a floating number: "))
print("Rounded value:", round(float_num))

# 48. Accept temperature in Celsius and convert to Fahrenheit.
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 49. Print a line 5 times using a single print statement.
print(("Hello World! " * 5).strip())

# 50. Take input of a product name and its price, then print a bill.
product = input("Enter product name: ")
price = float(input("Enter price: "))
print(f"Product: {product}\nPrice: {price} USD")

# ============================================
# PART 2: Conditional Statements (if, elif, else) — 50 Logic-Building Questions
# ============================================

# --------------------------------------------
# A. Basic If Conditions (25 Questions)
# --------------------------------------------

# 1. Check if a number is positive.
num = int(input("Enter a number: "))
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# 2. Check if a number is odd or even.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 3. Check if a number is divisible by 7.
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

# 4. Check if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 5. Check if a number is a single-digit number.
num = int(input("Enter a number: "))
if -9 <= num <= 9:
    print("It is a single-digit number")
else:
    print("It is not a single-digit number")

# 6. Check if a given year is a leap year.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# 7. Check if a given character is a vowel or consonant.
char = input("Enter a character: ").lower()
if char in "aeiou":
    print("Vowel")
else:
    print("Consonant")

# 8. Check if a string is empty or not.
s = input("Enter a string: ")
if len(s) == 0:
    print("String is empty")
else:
    print("String is not empty")

# 9. Check if a number is less than 100 and greater than 50.
num = int(input("Enter a number: "))
if 50 < num < 100:
    print("Number is between 50 and 100")
else:
    print("Number is not in range")

# 10. Accept a password and check if it matches the stored password.
stored_password = "python123"
password = input("Enter password: ")
if password == stored_password:
    print("Access Granted")
else:
    print("Access Denied")

# 11. Check if a number is both even and greater than 100.
num = 102
if num % 2 == 0 and num > 100:
    print("Number is even and greater than 100")
else:
    print("Condition not satisfied")

# 12. Check if a character is a digit.
char = "4"
if char.isdigit():
    print("It is a digit")
else:
    print("It is not a digit")

# 13. Check if the user input is uppercase.
input_user = "YASIR"
if input_user.isupper():
    print("Input is uppercase")
else:
    print("Input is not uppercase")

# 14. Check if two numbers are equal.
num1 = 3
num2 = 2
if num1 == num2:
    print("Numbers are equal")
else:
    print("Numbers are not equal")

# 15. Check if a number is divisible by both 3 and 5.
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")

# 16. Check if a number lies between 1 and 10.
num = 3
if num > 1 and num < 10:
    print("Number lies between 1 and 10")
else:
    print("Number is not in range 1-10")

# 17. Take an input name and check if it matches your name.
name = "yasir"
user_input = input("Enter the name: ")
if name == user_input:
    print("The name is the same")
else:
    print("Name is not the same")

# 18. Check if a number ends with digit 5.
num = 2245
if str(num).endswith("5"):
    print("The number ends with 5")
else:
    print("The number does not end with 5")

# 19. Accept a float number and check if it’s less than 10.5.
num_float = float(input("Enter a float number: "))
if num_float < 10.5:
    print("It is less than 10.5")
else:
    print("It is greater than or equal to 10.5")

# 20. Take a name input and check if it starts with “A”.
name_value = "Abdullah"
if name_value.startswith("A"):
    print("The name starts with A")
else:
    print("The name does not start with A")

# 21. Check if a number is not zero.
num = 7
if num != 0:
    print("Number is not zero")
else:
    print("Number is zero")

# 22. Check if a string contains more than 5 characters.
string_val = "HelloWorld"
if len(string_val) > 5:
    print("String contains more than 5 characters")
else:
    print("String does not contain more than 5 characters")

# 23. Check if the first and last character of a string are the same.
string_val = "radar"
if string_val[0] == string_val[-1]:
    print("First and last character are the same")
else:
    print("First and last character are not the same")

# 24. Check if a character is a special symbol (@, #, $, etc.).
char = "@"
if char in "@#$%&*!":
    print("It is a special symbol")
else:
    print("It is not a special symbol")

# 25. Take marks input and check if the student has passed (marks ≥ 40).
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Student has passed")
else:
    print("Student has failed")

# --------------------------------------------
# B. If...Else and Elif Conditions (25 Questions)
# --------------------------------------------

# 26. Write a program to find the greatest of two numbers.
num = 3
num2 = 33
if num > num2:
    print("num is greater")
elif num2 > num:
    print("it is larger")
else:
    print("it is same")

# 27. Write a program to find the greatest of three numbers.
num1 = 4
num2 = 5
num3 = 6
if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the greatest")
elif num2 >= num1 and num2 >= num3:
    print(f"{num2} is the greatest")
else:
    print(f"{num3} is the greatest")

# 28. Write a program to assign grades based on marks: • A (90+), B (80–89), C (70–79), Fail (Below 70).
marks = 85
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# 29. Take input of a number and check if it’s a multiple of 2 or 3.
num = int(input("Enter a number: "))
if num % 2 == 0 or num % 3 == 0:
    print(f"{num} is a multiple of 2 or 3")
else:
    print(f"{num} is not a multiple of 2 or 3")

# 30. Check whether the given character is a lowercase or uppercase alphabet.
ch = input("Enter a character: ")
if ch.isupper():
    print("Uppercase")
elif ch.islower():
    print("Lowercase")
else:
    print("Not an alphabet")

# 31. Write a program to print "Good Morning", "Good Afternoon", or "Good Night" based on time input.
time = int(input("Enter time in 24-hour format: "))
if 5 <= time < 12:
    print("Good Morning")
elif 12 <= time < 18:
    print("Good Afternoon")
else:
    print("Good Night")

# 32. Check if a number is negative, zero, or positive.
num = -5
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

# 33. Check if a person is a child (0–12), teenager (13–19), or adult (20+).
age = 15
if age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
else:
    print("Adult")

# 34. Write a program to compare lengths of two strings.
str1 = "apple"
str2 = "banana"
if len(str1) == len(str2):
    print("Both strings are equal in length")
elif len(str1) > len(str2):
    print("First string is longer")
else:
    print("Second string is longer")

# 35. Write a program to check login: ask for username and password.
username = "yasir"
password = "5656"
user_name = input("Enter username: ")
user_pass = input("Enter password: ")
if user_name == username and user_pass == password:
    print("Login successful")
else:
    print("Invalid credentials")

# 36. Take a number and print whether it’s a Prime or not.
num = 29
is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
print("Prime" if is_prime else "Not Prime")

# 37. Write a program to check if the year is a century year or not.
year = 2000
if year % 100 == 0:
    print("Century Year")
else:
    print("Not a Century Year")

# 38. Write a program to find the type of triangle (equilateral, isosceles, scalene).
a, b, c = 5, 5, 8
if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

# 39. Write a program to check whether a number is a perfect square.
num = 49
if int(num ** 0.5) ** 2 == num:
    print("Perfect Square")
else:
    print("Not a Perfect Square")

# 40. Write a program to check whether a number is an Armstrong number.
num = 153
order = len(str(num))
sum_val = sum(int(digit) ** order for digit in str(num))
if num == sum_val:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# 41. Take a character input and print whether it’s an alphabet, digit, or symbol.
ch = input("Enter a character: ")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("Symbol")

# 42. Check if a number is in the Fibonacci series (first 20 numbers).
n = 13
fib = [0, 1]
for i in range(2, 20):
    fib.append(fib[-1] + fib[-2])
if n in fib:
    print(f"{n} is in Fibonacci series")
else:
    print(f"{n} is not in Fibonacci series")

# 43. Check if a number is a palindrome (e.g. 121).
num = 121
if str(num) == str(num)[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 44. Take input from user and print if it’s a weekday or weekend.
day = input("Enter a day: ").lower()
if day in ["saturday", "sunday"]:
    print("Weekend")
else:
    print("Weekday")

# 45. Based on a person’s age, print if they are eligible for driving, voting, or both.
age = 20
if age >= 18 and age >= 16:
    print("Eligible for both driving and voting")
elif age >= 18:
    print("Eligible for voting only")
elif age >= 16:
    print("Eligible for driving only")
else:
    print("Not eligible for driving or voting")

# 46. Write a program to check whether a string is a palindrome.
text = "madam"
if text == text[::-1]:
    print("Palindrome String")
else:
    print("Not a Palindrome String")

# 47. Write a program to find the second largest number among three.
a, b, c = 10, 20, 15
nums = [a, b, c]
nums.sort()
print("Second largest is", nums[1])

# 48. Create a number guessing game using if-else.
secret = 7
guess = int(input("Guess the number: "))
if guess == secret:
    print("Correct guess!")
elif guess > secret:
    print("Too high!")
else:
    print("Too low!")

# 49. Ask the user to enter a month name and print the number of days.
month = input("Enter month: ").lower()
if month in ["january", "march", "may", "july", "august", "october", "december"]:
    print("31 days")
elif month in ["april", "june", "september", "november"]:
    print("30 days")
elif month == "february":
    print("28 or 29 days")
else:
    print("Invalid month")

# 50. Take a temperature input and categorize it as cold, warm, or hot.
temp = int(input("Enter temperature: "))
if temp < 15:
    print("Cold")
elif 15 <= temp <= 30:
    print("Warm")
else:
    print("Hot")

# ============================================
# PART 3: Loops in Python (for, while, nested) — 50 Logic-Building Questions
# ============================================

# --------------------------------------------
# A. Basic for and while Loops (25 Questions)
# --------------------------------------------
# 1.	Print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)
# 2.	Print numbers from 10 to 1 using a while loop.
i = 10
while i >=1:
    print(i)
    i =  i - 1
# 3.	Print even numbers from 1 to 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
# using while Loop 
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1
    
# 4.	Print all odd numbers between 1 and 100.
for i in range(1, 101):
    if i % 3 == 0:
        print(i)
    
# using while loop
i = 1
while i <= 101:   # loop continues until 101
    if i % 3 == 0:
        print(i)
    i = i + 1
# 5.	Print the table of 5 (e.g., 5, 10, 15,... up to 50).
for i in range(1, 55):
    if i % 5 == 0:
        print(i)

#using while loop
i = 1
while i <= 10:
    print(5 * i)
    i += 1

# 6. Print the first 10 multiples of a number entered by the user
num = int(input("Enter a number: "))
print("First 10 multiples of", num, "(for loop):")
for i in range(1, 11):
    print(num * i)

print("First 10 multiples of", num, "(while loop):")
i = 1
while i <= 10:
    print(num * i)
    i += 1

# 7. Print the sum of numbers from 1 to n (input by user)
n = int(input("Enter n: "))
sum1 = 0
for i in range(1, n + 1):
    sum1 += i
print("Sum using for loop:", sum1)

sum2, i = 0, 1
while i <= n:
    sum2 += i
    i += 1
print("Sum using while loop:", sum2)

# 8. Print the product of numbers from 1 to 10
prod = 1
for i in range(1, 11):
    prod *= i
print("Product using for loop:", prod)

prod2, i = 1, 1
while i <= 10:
    prod2 *= i
    i += 1
print("Product using while loop:", prod2)

# 9. Factorial of a number using loop
n = int(input("Enter a number to find factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print("Factorial using for loop:", fact)

fact2, i = 1, 1
while i <= n:
    fact2 *= i
    i += 1
print("Factorial using while loop:", fact2)

# 10. Reverse of a given number
num = int(input("Enter a number to reverse: "))
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10
print("Reverse:", rev)

# 11. Count digits in a number
num = int(input("Enter a number: "))
count = 0
temp = num
while temp > 0:
    temp //= 10
    count += 1
print("Digits count:", count)

# 12. Sum of digits of a number
num = int(input("Enter a number: "))
sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("Sum of digits:", sum_digits)

# 13. Check palindrome number
num = int(input("Enter a number to check palindrome: "))
temp, rev = num, 0
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
if num == rev:
    print("Palindrome")
else:
    print("Not Palindrome")

# 14. Fibonacci series up to n terms
n = int(input("Enter n terms for Fibonacci: "))
a, b = 0, 1
print("Fibonacci series:", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 15. Largest number in a list
nums = list(map(int, input("Enter numbers separated by space: ").split()))
largest = nums[0]
for num in nums:
    if num > largest:
        largest = num
print("Largest:", largest)

# 16. Smallest number in a list
smallest = nums[0]
for num in nums:
    if num < smallest:
        smallest = num
print("Smallest:", smallest)

# 17. Average of n numbers
nums = list(map(int, input("Enter numbers separated by space: ").split()))
avg = sum(nums) / len(nums)
print("Average:", avg)

# 18. Count numbers divisible by 7 (1–100)
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print("Count divisible by 7 (for loop):", count)

# 19. ASCII values of characters in a string
s = input("Enter a string: ")
for ch in s:
    print(f"{ch} -> {ord(ch)}")

# 20. Print characters of a string in reverse
s = input("Enter a string: ")
print("Reverse using for loop:")
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")
print()

# 21. Square of first n natural numbers
n = int(input("Enter n: "))
print("Squares:")
for i in range(1, n + 1):
    print(i, "->", i * i)

# 22. Cube of numbers from 1 to 20
print("Cubes from 1 to 20:")
for i in range(1, 21):
    print(i, "->", i ** 3)

# 23. Print only vowels from a string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
print("Vowels:", end=" ")
for ch in s:
    if ch in vowels:
        print(ch, end=" ")
print()

# 24. Print only consonants from a string
print("Consonants:", end=" ")
for ch in s:
    if ch.isalpha() and ch not in vowels:
        print(ch, end=" ")
print()

# 25. First 10 prime numbers
print("First 10 prime numbers:")
count, num = 0, 2
while count < 10:
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
        count += 1
    num += 1
print()

# --------------------------------------------
# B. Nested Loops & Pattern Printing (25 Questions)
# --------------------------------------------

# 26.	Print a square pattern of * with 5 rows and 5 columns.
for i in range(5):
    print("* " * 5)

# 27.	Print a right-angled triangle of *.
for i in range(1, 6):
    print("* " * i)

# 28.	Print a number triangle:
# 1
# 1 2
# 1 2 3
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 29.	Print a reverse number triangle:
# 3 2 1
# 2 1
# 1
for i in range(3, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

# 30.	Print an inverted triangle of *.
for i in range(5, 0, -1):
    print("* " * i)

# 31.	Print a multiplication table from 1 to 10.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:3}", end=" ")
    print()

# 32.	Print the sum of each row in a 2D list.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print("Row sum:", sum(row))

# 33.	Print the pattern of alternating 1s and 0s.
for i in range(5):
    for j in range(5):
        print((i+j)%2, end=" ")
    print()

# 34.	Print the following:
# A
# A B
# A B C
for i in range(1, 4):
    for j in range(65, 65+i):  # ASCII 65 = 'A'
        print(chr(j), end=" ")
    print()

# 35.	Print only even rows in a nested pattern loop.
for i in range(1, 6):
    if i % 2 == 0:
        print("* " * i)

# 36.	Print a triangle of alphabets using ASCII values.
for i in range(1, 6):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()
   
# 37.	Print the diamond pattern using *.
n = 5
for i in range(1, n+1):
    print(" "*(n-i) + "* " * i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "* " * i)

# 38.	Print pyramid of numbers:
#   1
#  1 2
# 1 2 3
for i in range(1, 6):
    print(" "*(5-i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 39.	Create a program that takes a number and prints a hollow square using *.
size = 5
for i in range(size):
    for j in range(size):
        if i==0 or i==size-1 or j==0 or j==size-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# 40.	Print numbers in the following pattern:
# 1
# 2 3
# 4 5 6
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

# 41.	Generate all pairs (i, j) such that 1 ≤ i, j ≤ 3.
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()

# 42.	Generate a multiplication chart up to 12×12.
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i*j:3}", end=" ")
    print()

# 43.	Count the number of vowels and consonants in a string using loop.
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
v_count = 0
c_count = 0
for ch in s:
    if ch.isalpha():
        if ch in vowels:
            v_count += 1
        else:
            c_count += 1
print("Vowels:", v_count, "Consonants:", c_count)

# 44.	Print all words in a sentence line by line.
sentence = input("Enter a sentence: ")
for word in sentence.split():
    print(word)

# 45.	Print even and odd numbers in different lines from a list.
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Even numbers:")
for n in nums:
    if n % 2 == 0:
        print(n, end=" ")
print("\nOdd numbers:")
for n in nums:
    if n % 2 != 0:
        print(n, end=" ")
print()

# 46.	Print a table of all odd numbers from 1 to 20.
for i in range(1, 21, 2):
    print(i, end=" ")
print()

# 47.	Find how many times a character appears in a string.
s = input("Enter a string: ")
ch = input("Enter character to count: ")
count = 0
for c in s:
    if c == ch:
        count += 1
print(f"'{ch}' appears {count} times")

# 48.	Reverse a string using a loop (don’t use slicing).
s = input("Enter a string to reverse: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

# 49.	Sum the elements of each row in a 2D matrix.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
for row in matrix:
    print("Row sum:", sum(row)) 

# 50.	Write a program to print prime numbers in a given range using nested loops.

low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))
for num in range(low, high+1):
    if num > 1:
        prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                prime = False
                break
        if prime:
            print(num, end=" ")
print()

# ============================================
# PART 4: Functions & Recursion in Python — 50 Logic-Building Questions
# ============================================

# --------------------------------------------
# A. Basic Function Logic (25 Questions)
# --------------------------------------------

# 1. Write a function to add two numbers.
def add_numbers(a, b):
    return a + b

# 2. Write a function to return the square of a number.
def square_number(n):
    return n * n

# 3. Write a function that returns the largest of three numbers.
def largest_of_three(a, b, c):
    return max(a, b, c)

# 4. Write a function to check if a number is even or odd.
def is_even_or_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 5. Write a function to check if a number is positive, negative, or zero.
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# 6. Write a function that returns the factorial of a number.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# 7. Write a function to check whether a number is prime.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 8. Write a function to print the multiplication table of a number.
def multiplication_table(n):
    return [n * i for i in range(1, 11)]

# 9. Write a function to calculate the power of a number (x^y).
def power(x, y):
    return x ** y

# 10. Write a function that returns the sum of all elements in a list.
def sum_list(lst):
    return sum(lst)

# 11. Write a function that returns the maximum element from a list.
def max_in_list(lst):
    return max(lst)

# 12. Write a function to reverse a string.
def reverse_string(s):
    return s[::-1]

# 13. Write a function to count the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 14. Write a function to check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

# 15. Write a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 16. Write a function to remove duplicates from a list.
def remove_duplicates(lst):
    return list(set(lst))

# 17. Write a function to check if a number is an Armstrong number.
def is_armstrong(n):
    digits = str(n)
    power_len = len(digits)
    return n == sum(int(d)**power_len for d in digits)

# 18. Write a function to find the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 19. Write a function to find the LCM of two numbers.
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 20. Write a function to return all even numbers in a list.
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# 21. Write a function that returns the second largest number in a list.
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

# 22. Write a function to print Fibonacci series up to n terms.
def fibonacci(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# 23. Write a function to find the length of a list without using len().
def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count

# 24. Write a function to find the average of numbers in a list.
def average_list(lst):
    return sum(lst) / len(lst) if lst else 0

# 25. Write a function to count digits in an integer.
def count_digits(n):
    return len(str(abs(n)))

# --------------------------------------------
# B. Recursion-Based Logic (25 Questions)
# --------------------------------------------

# 26. Write a recursive function to calculate factorial.
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

# 27. Write a recursive function to print numbers from 1 to n.
def print_1_to_n(n):
    if n > 0:
        print_1_to_n(n - 1)
        print(n, end=" ")

# 28. Write a recursive function to print numbers from n to 1.
def print_n_to_1(n):
    if n > 0:
        print(n, end=" ")
        print_n_to_1(n - 1)

# 29. Write a recursive function to calculate the sum of digits.
def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

# 30. Write a recursive function to reverse a number.
def reverse_number(n, rev=0):
    if n == 0:
        return rev
    return reverse_number(n // 10, rev * 10 + n % 10)

# 31. Write a recursive function to calculate x^y (power function).
def recursive_power(x, y):
    if y == 0:
        return 1
    return x * recursive_power(x, y - 1)

# 32. Write a recursive function to print Fibonacci numbers.
def recursive_fibonacci(n, a=0, b=1):
    if n > 0:
        print(a, end=" ")
        recursive_fibonacci(n - 1, b, a + b)

# 33. Write a recursive function to find GCD of two numbers.
def recursive_gcd(a, b):
    if b == 0:
        return a
    return recursive_gcd(b, a % b)

# 34. Write a recursive function to count the number of elements in a list.
def count_elements(lst):
    if lst == []:
        return 0
    return 1 + count_elements(lst[1:])

# 35. Write a recursive function to find the sum of a list.
def sum_list_recursive(lst):
    if lst == []:
        return 0
    return lst[0] + sum_list_recursive(lst[1:])

# 36. Write a recursive function to check if a string is a palindrome.
def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

# 37. Write a recursive function to find the maximum element in a list.
def max_in_list_recursive(lst):
    if len(lst) == 1:
        return lst[0]
    return max(lst[0], max_in_list_recursive(lst[1:]))

# 38. Write a recursive function to print a pattern of *.
def star_pattern(n):
    if n > 0:
        star_pattern(n - 1)
        print("*" * n)

# 39. Write a recursive function to find the nth term of a Fibonacci sequence.
def nth_fibonacci(n):
    if n <= 1:
        return n
    return nth_fibonacci(n - 1) + nth_fibonacci(n - 2)

# 40. Write a recursive function to find the sum of the first n natural numbers.
def sum_natural(n):
    if n == 0:
        return 0
    return n + sum_natural(n - 1)

# 41. Write a recursive function to check if a number is prime.
def is_prime_recursive(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime_recursive(n, i + 1)

# 42. Write a recursive function to find the product of digits of a number.
def product_of_digits(n):
    if n == 0:
        return 1
    return (n % 10) * product_of_digits(n // 10)

# 43. Write a recursive function to count vowels in a string.
def count_vowels_recursive(s):
    vowels = "aeiouAEIOU"
    if s == "":
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels_recursive(s[1:])

# 44. Write a recursive function to flatten a nested list.
def flatten_list(lst):
    if lst == []:
        return []
    if isinstance(lst[0], list):
        return flatten_list(lst[0]) + flatten_list(lst[1:])
    return [lst[0]] + flatten_list(lst[1:])

# 45. Write a recursive function to compute sum of squares of first n natural numbers.
def sum_of_squares(n):
    if n == 0:
        return 0
    return n * n + sum_of_squares(n - 1)

# 46. Write a recursive function to find the binary representation of a number.
def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return decimal_to_binary(n // 2) + str(n % 2)

# 47. Write a recursive function to check for Armstrong number.
def is_armstrong_recursive(n, power=None):
    if power is None:
        power = len(str(n))
    if n == 0:
        return 0
    return (n % 10) ** power + is_armstrong_recursive(n // 10, power)

# 48. Write a recursive function to calculate the length of a string.
def string_length(s):
    if s == "":
        return 0
    return 1 + string_length(s[1:])

# 49. Write a recursive function to generate all subsets of a set.
def subsets(lst):
    if lst == []:
        return [[]]
    first, rest = lst[0], lst[1:]
    sub_rest = subsets(rest)
    return sub_rest + [[first] + s for s in sub_rest]

# 50. Write a recursive function to calculate factorial without using return (print inline).
def factorial_inline(n, result=1):
    if n == 0:
        print("Factorial:", result)
    else:
        factorial_inline(n - 1, result * n)


# ============================================
# PART 5: String Manipulation in Python — 50 Logic-Building Questions
# ============================================

# --------------------------------------------
# A. Basic String Operations (25 Questions)
# --------------------------------------------

# 1. Count the number of characters in a string.
s = "hello world"
print(len(s))

# 2. Count the number of vowels and consonants in a string.
s = "hello world"
vowels = "aeiouAEIOU"
v_count = sum(1 for ch in s if ch in vowels)
c_count = sum(1 for ch in s if ch.isalpha() and ch not in vowels)
print("Vowels:", v_count, "Consonants:", c_count)

# 3. Reverse a string without using slicing.
s = "hello"
rev = ""
for ch in s:
    rev = ch + rev
print(rev)

# 4. Check if a string is a palindrome.
s = "madam"
print(s == s[::-1])

# 5. Count the frequency of each character in a string.
s = "banana"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)

# 6. Convert uppercase to lowercase and vice versa.
s = "HeLLo"
print(s.swapcase())

# 7. Remove all spaces from a string.
s = "hello world python"
print(s.replace(" ", ""))

# 8. Remove all vowels from a string.
s = "hello world"
vowels = "aeiouAEIOU"
print("".join(ch for ch in s if ch not in vowels))

# 9. Replace all vowels with a specific character.
s = "hello world"
print("".join("*" if ch in vowels else ch for ch in s))

# 10. Find the first non-repeating character in a string.
s = "aabbcde"
for ch in s:
    if s.count(ch) == 1:
        print("First non-repeating:", ch)
        break

# 11. Find the first repeating character in a string.
s = "abcdaef"
seen = set()
for ch in s:
    if ch in seen:
        print("First repeating:", ch)
        break
    seen.add(ch)

# 12. Count the number of words in a sentence.
s = "Hello world from Python"
print(len(s.split()))

# 13. Capitalize the first letter of each word in a sentence.
s = "hello world from python"
print(s.title())

# 14. Check if two strings are anagrams of each other.
s1, s2 = "listen", "silent"
print(sorted(s1) == sorted(s2))

# 15. Remove all special characters from a string.
import re
s = "Hello@World#123!"
print(re.sub(r'[^A-Za-z0-9 ]+', '', s))

# 16. Find the longest word in a sentence.
s = "Python is a powerful programming language"
words = s.split()
print(max(words, key=len))

# 17. Count how many times a substring occurs in a string.
s = "banana"
print(s.count("ana"))

# 18. Reverse the words in a sentence.
s = "Python is fun"
print(" ".join(reversed(s.split())))

# 19. Replace a word in a sentence with another word.
s = "I love Python"
print(s.replace("Python", "Java"))

# 20. Check if a string contains only digits.
s = "12345"
print(s.isdigit())

# 21. Count uppercase and lowercase letters separately.
s = "HeLLo World"
upper = sum(1 for ch in s if ch.isupper())
lower = sum(1 for ch in s if ch.islower())
print("Uppercase:", upper, "Lowercase:", lower)

# 22. Remove duplicate characters from a string.
s = "programming"
result = "".join(dict.fromkeys(s))
print(result)

# 23. Find the most frequent character in a string.
s = "mississippi"
freq = {}
for ch in s:
    freq[ch] = freq.get(ch, 0) + 1
print(max(freq, key=freq.get))

# 24. Check whether a string starts and ends with the same character.
s = "radar"
print(s[0] == s[-1])

# 25. Swap the first and last characters of a string.
s = "python"
if len(s) > 1:
    s = s[-1] + s[1:-1] + s[0]
print(s)



# --------------------------------------------
# B. Intermediate String Logic (25 Questions)
# --------------------------------------------

# 26. Check if two strings are rotations of each other
def are_rotations(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)
# print(are_rotations("abcd", "cdab"))  # True

# 27. Find all substrings of a string
def all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i+1, len(s)+1)]
# print(all_substrings("abc"))

# 28. Generate all permutations of a string
from itertools import permutations
def string_permutations(s):
    return [''.join(p) for p in permutations(s)]
# print(string_permutations("abc"))

# 29. Compress a string (aabbb → a2b3)
def compress_string(s):
    result, count = "", 1
    for i in range(1, len(s)+1):
        if i < len(s) and s[i] == s[i-1]:
            count += 1
        else:
            result += s[i-1] + (str(count) if count > 1 else "")
            count = 1
    return result
# print(compress_string("aabbb"))  # a2b3

# 30. Expand a compressed string (a2b3 → aabbb)
def expand_string(s):
    result, i = "", 0
    while i < len(s):
        char = s[i]
        i += 1
        num = ""
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        result += char * (int(num) if num else 1)
    return result
# print(expand_string("a2b3"))  # aabbb

# 31. Count the number of alphanumeric characters in a string
def count_alphanumeric(s):
    return sum(ch.isalnum() for ch in s)
# print(count_alphanumeric("Hello 123!"))

# 32. Check if a string contains all vowels
def contains_all_vowels(s):
    vowels = set("aeiou")
    return vowels.issubset(set(s.lower()))
# print(contains_all_vowels("education"))

# 33. Find the common characters between two strings
def common_characters(s1, s2):
    return ''.join(set(s1) & set(s2))
# print(common_characters("hello", "world"))

# 34. Remove all punctuation marks from a string
import string
def remove_punctuation(s):
    return ''.join(ch for ch in s if ch not in string.punctuation)
# print(remove_punctuation("Hello, World!"))

# 35. Find the longest palindrome substring
def longest_palindrome(s):
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l, r = l-1, r+1
        return s[l+1:r]
    longest = ""
    for i in range(len(s)):
        longest = max(longest, expand(i, i), expand(i, i+1), key=len)
    return longest
# print(longest_palindrome("babad"))

# 36. Convert a sentence to title case
def to_title_case(s):
    return ' '.join(word.capitalize() for word in s.split())
# print(to_title_case("hello world python"))

# 37. Sort the characters in a string alphabetically
def sort_string(s):
    return ''.join(sorted(s))
# print(sort_string("python"))

# 38. Group digits, letters, and special characters separately
def group_chars(s):
    digits = ''.join(ch for ch in s if ch.isdigit())
    letters = ''.join(ch for ch in s if ch.isalpha())
    specials = ''.join(ch for ch in s if not ch.isalnum())
    return digits, letters, specials
# print(group_chars("a1b2c3!@#"))

# 39. Implement find() without using it
def custom_find(s, sub):
    for i in range(len(s) - len(sub) + 1):
        if s[i:i+len(sub)] == sub:
            return i
    return -1
# print(custom_find("hello", "lo"))  # 3

# 40. Implement replace() without using it
def custom_replace(s, old, new):
    result, i = "", 0
    while i < len(s):
        if s[i:i+len(old)] == old:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result
# print(custom_replace("hello world", "world", "Python"))

# 41. Split string into list of characters without using list()
def split_chars(s):
    return [ch for ch in s]
# print(split_chars("hello"))

# 42. Replace all duplicate characters with underscores
def replace_duplicates(s):
    seen, result = set(), ""
    for ch in s:
        if ch in seen:
            result += "_"
        else:
            seen.add(ch)
            result += ch
    return result
# print(replace_duplicates("programming"))

# 43. Find the first capital letter in a string using loop
def first_capital(s):
    for ch in s:
        if ch.isupper():
            return ch
    return None
# print(first_capital("helloWorld"))

# 44. Print every alternate character from a string
def alternate_chars(s):
    return s[::2]
# print(alternate_chars("abcdef"))

# 45. Count how many times each word appears in a sentence
from collections import Counter
def word_count(sentence):
    words = sentence.split()
    return Counter(words)
# print(word_count("this is a test this is"))

# 46. Identify and print palindromic words in a sentence
def palindromic_words(sentence):
    return [word for word in sentence.split() if word == word[::-1]]
# print(palindromic_words("madam anna went to kayak"))

# 47. Remove the last word from a sentence
def remove_last_word(sentence):
    words = sentence.split()
    return ' '.join(words[:-1])
# print(remove_last_word("This is a sentence"))

# 48. Print the middle character of a string
def middle_char(s):
    mid = len(s) // 2
    return s[mid] if len(s) % 2 else s[mid-1:mid+1]
# print(middle_char("hello"))
# print(middle_char("python"))

# 49. Convert a string to a list of ASCII values
def string_to_ascii(s):
    return [ord(ch) for ch in s]
# print(string_to_ascii("abc"))

# 50. Convert a list of ASCII values back to a string
def ascii_to_string(ascii_list):
    return ''.join(chr(num) for num in ascii_list)
# print(ascii_to_string([97, 98, 99]))

# ============================================
# PART 6: Python Data Structures — 50 Logic-Building Questions  
# ============================================

# --------------------------------------------
# A. List-Based Logic (15 Questions)
# --------------------------------------------

# 1. Create a list and add 10 numbers entered by the user
nums = []
for i in range(10):
    n = int(input(f"Enter number {i+1}: "))
    nums.append(n)
print("Final List:", nums)

# 2. Find the maximum and minimum elements from a list
nums = [10, 3, 55, 7, 19]
maximum = nums[0]
minimum = nums[0]
for num in nums:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print("Max:", maximum, "Min:", minimum)

# 3. Count the number of even and odd elements in a list
nums = [1, 2, 3, 4, 5]
even_count = 0
odd_count = 0
for num in nums:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even:", even_count, "Odd:", odd_count)

# 4. Separate positive and negative numbers from a list
nums = [10, -5, 7, -2, 0]
positive = []
negative = []
for num in nums:
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)
print("Positive:", positive)
print("Negative:", negative)

# 5. Sort a list in ascending and descending order without using sort()
nums = [4, 1, 3, 9, 7]
for i in range(len(nums)):
    for j in range(len(nums) - i - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print("Ascending:", nums)
print("Descending:", nums[::-1])

# 6. Remove duplicates from a list without using set()
nums = [1, 2, 2, 3, 4, 4, 5]
unique = []
for num in nums:
    if num not in unique:
        unique.append(num)
print("Without Duplicates:", unique)

# 7. Reverse a list using loop
nums = [1, 2, 3, 4]
reversed_list = []
for i in range(len(nums) - 1, -1, -1):
    reversed_list.append(nums[i])
print("Reversed:", reversed_list)

# 8. Merge two lists and sort the result
list1 = [1, 4, 6]
list2 = [2, 3, 5]
merged = list1 + list2
for i in range(len(merged)):
    for j in range(len(merged) - i - 1):
        if merged[j] > merged[j + 1]:
            merged[j], merged[j + 1] = merged[j + 1], merged[j]
print("Merged & Sorted:", merged)

# 9. Find the second largest number in a list
nums = [10, 20, 4, 45, 99]
first = second = float('-inf')
for num in nums:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num
print("Second Largest:", second)

# 10. Rotate a list left by 2 positions
nums = [1, 2, 3, 4, 5]
k = 2
rotated = nums[k:] + nums[:k]
print("Rotated Left by 2:", rotated)

# 11. Insert an element at a specific position in a list
nums = [10, 20, 30]
pos = 2
element = 25
nums = nums[:pos] + [element] + nums[pos:]
print("After Insertion:", nums)

# 12. Remove all even numbers from a list
nums = [1, 2, 3, 4, 5, 6]
result = []
for num in nums:
    if num % 2 != 0:
        result.append(num)
print("Without Even Numbers:", result)

# 13. Count the frequency of each number in a list
nums = [1, 2, 2, 3, 1, 4, 2]
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print("Frequencies:", freq)

# 14. Flatten a nested list
nested = [[1, 2], [3, 4], [5, 6]]
flat = []
for sublist in nested:
    for item in sublist:
        flat.append(item)
print("Flattened:", flat)

# 15. Find all elements that appear more than once in a list
nums = [4, 3, 2, 7, 8, 2, 3, 1]
duplicates = []
seen = []
for num in nums:
    if num in seen and num not in duplicates:
        duplicates.append(num)
    else:
        seen.append(num)
print("Duplicates:", duplicates)


# --------------------------------------------
# B. Tuple-Based Logic (10 Questions)
# --------------------------------------------

# 16. Create a tuple of 10 elements and print it
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print("Tuple:", tup)

# 17. Find the maximum and minimum value in a tuple
tup = (10, 3, 55, 7, 19)
print("Max:", max(tup))
print("Min:", min(tup))

# 18. Convert a tuple into a list and modify it
tup = (1, 2, 3, 4)
lst = list(tup)     # Convert tuple → list
lst[1] = 99         # Modify element
print("Modified List:", lst)

# 19. Count how many times an element appears in a tuple
tup = (1, 2, 3, 2, 4, 2, 5)
print("Count of 2:", tup.count(2))

# 20. Find the index of an element in a tuple
tup = (10, 20, 30, 40, 50)
print("Index of 30:", tup.index(30))

# 21. Slice a tuple to get a sub-tuple
tup = (1, 2, 3, 4, 5, 6, 7)
sub_tup = tup[2:5]  # From index 2 to 4
print("Sub-tuple:", sub_tup)

# 22. Check if an element exists in a tuple
tup = (10, 20, 30, 40)
element = 30
if element in tup:
    print(f"{element} exists in tuple")
else:
    print(f"{element} does not exist in tuple")

# 23. Merge two tuples
tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
merged = tup1 + tup2
print("Merged Tuple:", merged)

# 24. Swap two tuples
tup1 = (10, 20, 30)
tup2 = (40, 50, 60)
tup1, tup2 = tup2, tup1
print("After Swapping:")
print("Tuple1:", tup1)
print("Tuple2:", tup2)


# 25. Convert a list of tuples into a dictionary

lst = [("a", 1), ("b", 2), ("c", 3)]
dictionary = dict(lst)
print("Dictionary:", dictionary)

# --------------------------------------------
# C. Dictionary-Based Logic (15 Questions)
# --------------------------------------------

# 26. Create a dictionary of 5 students with names and marks
students = {"Ali": 85, "Sara": 90, "John": 76, "Ayesha": 92, "David": 60}
print("Students Dictionary:", students)


# 27. Add a new key-value pair to a dictionary
students["Michael"] = 88
print("After Adding:", students)

# 28. Update the value of an existing key
students["John"] = 80
print("After Updating John's Marks:", students)

# 29. Delete a key from the dictionary
del students["David"]
print("After Deletion:", students)

# 30. Find the key with the maximum value
max_key = max(students, key=students.get)
print("Key with Maximum Value:", max_key)

# 31. Count the frequency of characters in a string using a dictionary
text = "programming"
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print("Character Frequency:", freq)

# 32. Create a dictionary from two lists (one with keys, one with values)
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print("Dictionary from Lists:", my_dict)

# 33. Check if a key exists in a dictionary
if "Sara" in students:
    print("Sara exists in dictionary")
else:
    print("Sara does not exist")

# 34. Merge two dictionaries
dict1 = {"x": 10, "y": 20}
dict2 = {"y": 30, "z": 40}
merged = {**dict1, **dict2}
print("Merged Dictionary:", merged)

# 35. Invert a dictionary (swap keys and values)
inverted = {v: k for k, v in students.items()}
print("Inverted Dictionary:", inverted)

# 36. Find common keys between two dictionaries
dictA = {"a": 1, "b": 2, "c": 3}
dictB = {"b": 4, "c": 5, "d": 6}
common_keys = dictA.keys() & dictB.keys()
print("Common Keys:", common_keys)

# 37. Sort a dictionary by values
sorted_dict = dict(sorted(students.items(), key=lambda item: item[1]))
print("Sorted by Values:", sorted_dict)

# 38. Create a nested dictionary and access inner values
nested = {
    "student1": {"name": "Ali", "marks": 85},
    "student2": {"name": "Sara", "marks": 90}
}
print("Student2 Name:", nested["student2"]["name"])
print("Student1 Marks:", nested["student1"]["marks"])

# 39. Sum all the values in a dictionary
marks_sum = sum(students.values())
print("Sum of Marks:", marks_sum)

# 40. Filter dictionary items based on condition (e.g., marks > 50)
filtered = {k: v for k, v in students.items() if v > 50}
print("Filtered (marks > 50):", filtered)

# --------------------------------------------
# D. Set-Based Logic (10 Questions)
# --------------------------------------------

# 41. Create a set and add 5 elements to it
my_set = set()
my_set.add(10)
my_set.add(20)
my_set.add(30)
my_set.add(40)
my_set.add(50)
print("Set:", my_set)

# 42. Check if an element exists in a set
element = 30
if element in my_set:
    print(f"{element} exists in set")
else:
    print(f"{element} does not exist in set")

# 43. Perform union, intersection, and difference of two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)             # or set1.union(set2)
print("Intersection:", set1 & set2)      # or set1.intersection(set2)
print("Difference:", set1 - set2)        # or set1.difference(set2)

# 44. Remove an item from a set

my_set = {1, 2, 3, 4, 5}
my_set.remove(3)   # throws error if not present
# my_set.discard(3)  # safer alternative
print("After Removing 3:", my_set)

# 45. Convert a list into a set to remove duplicates

nums = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(nums)
print("Unique Elements:", unique_set)

# 46. Find symmetric difference between two sets

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Symmetric Difference:", set1 ^ set2)   # or set1.symmetric_difference(set2)

# 47. Check if one set is a subset of another

set1 = {1, 2}
set2 = {1, 2, 3, 4}
print("Is set1 subset of set2?", set1.issubset(set2))

# 48. Iterate through a set and print its elements

my_set = {"apple", "banana", "cherry"}
for item in my_set:
    print(item)

# 49. Add multiple items to a set using update()

my_set = {1, 2}
my_set.update([3, 4, 5])
print("Updated Set:", my_set)

# 50. Find common elements in three different sets
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5}
set3 = {2, 3, 6}
common = set1 & set2 & set3
print("Common Elements:", common)


# ============================================
# PART 7: Pattern Printing & Loops — 50 Logic-Building Questions
# ============================================

# --------------------------------------------
# A. Star Patterns (25 Questions)
# --------------------------------------------

# 1. Print a square of * (n x n).
def square_pattern(n):
    for _ in range(n):
        print("* " * n)

# 2. Print a right-angled triangle pattern.
def right_triangle(n):
    for i in range(1, n+1):
        print("* " * i)

# 3. Print an inverted right-angled triangle.
def inverted_right_triangle(n):
    for i in range(n, 0, -1):
        print("* " * i)

# 4. Print a pyramid pattern of stars.
def pyramid(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

# 5. Print an inverted pyramid of stars.
def inverted_pyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)

# 6. Print a diamond pattern.
def diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "* " * i)

# 7. Print a hollow square pattern.
def hollow_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("* " * n)
        else:
            print("* " + "  " * (n-2) + "*")

# 8. Print a hollow right-angled triangle.
def hollow_right_triangle(n):
    for i in range(1, n+1):
        if i == 1 or i == n:
            print("* " * i)
        else:
            print("* " + "  " * (i-2) + "*")

# 9. Print a pattern with increasing number of stars on each line.
def increasing_stars(n):
    for i in range(1, n+1):
        print("* " * i)

# 10. Print a pattern with decreasing number of stars on each line.
def decreasing_stars(n):
    for i in range(n, 0, -1):
        print("* " * i)

# 11. Print a right-aligned triangle pattern.
def right_aligned_triangle(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

# 12. Print a left-aligned inverted triangle.
def left_aligned_inverted(n):
    for i in range(n, 0, -1):
        print(" " * (n-i) + "* " * i)

# 13. Print a pattern of stars in the shape of a cross (+).
def cross_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == n//2 or j == n//2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 14. Print a pattern of stars in the shape of an X.
def x_pattern(n):
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n-1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 15. Print a pattern where each row has stars equal to the row number.
def row_number_stars(n):
    for i in range(1, n+1):
        print("* " * i)

# 16. Print a checkerboard pattern of * and space.
def checkerboard(n):
    for i in range(n):
        for j in range(n):
            if (i+j) % 2 == 0:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 17. Print a zig-zag star pattern.
def zig_zag(n):
    for i in range(3):
        for j in range(1, n+1):
            if (i+j) % 4 == 0 or (i == 1 and j % 4 == 0):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# 18. Print a half diamond pattern.
def half_diamond(n):
    for i in range(1, n+1):
        print("* " * i)
    for i in range(n-1, 0, -1):
        print("* " * i)

# 19. Print a hollow diamond pattern.
def hollow_diamond(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "*" + " " * (2*i-3) + ("*" if i > 1 else ""))
    for i in range(n-1, 0, -1):
        print(" " * (n-i) + "*" + " " * (2*i-3) + ("*" if i > 1 else ""))

# 20. Print a star border with space inside.
def star_border(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print("* " * n)
        else:
            print("* " + "  " * (n-2) + "*")

# 21. Print a Pascal's triangle using stars.
def pascal_triangle(n):
    for i in range(n):
        print(" " * (n-i), end="")
        print("* " * (i+1))

# 22. Print a staircase pattern.
def staircase(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

# 23. Print a mirrored right triangle.
def mirrored_right_triangle(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

# 24. Print a heart shape with *.
def heart_shape(n):
    for i in range(n//2, n, 2):
        print(" " * ((n-i)//2) + "*" * i + " " * (n-i) + "*" * i)
    for i in range(n, 0, -1):
        print(" " * (n-i) + "*" * (2*i-1))

# 25. Print a butterfly pattern using stars.
def butterfly(n):
    for i in range(1, n+1):
        print("* " * i + "  " * (n-i) + "* " * i)
    for i in range(n, 0, -1):
        print("* " * i + "  " * (n-i) + "* " * i)

# --------------------------------------------
# B. Number Patterns and Loop Logic (25 Questions)
# --------------------------------------------

# 26. Print numbers from 1 to 100 using a loop.
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# 27. Print all even numbers between 1 and 50.
for i in range(2, 51, 2):
    print(i, end=" ")
print("\n")

# 28. Print all odd numbers between 1 and 50.
for i in range(1, 51, 2):
    print(i, end=" ")
print("\n")

# 29. Print multiplication table of a number (e.g., 5).
num = 5
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")
print("\n")

# 30. Print factorial of a number using a loop.
n = 5
fact = 1
for i in range(1, n+1):
    fact *= i
print("Factorial of", n, "=", fact)
print("\n")

# 31. Print the sum of the first n natural numbers.
n = 10
total = 0
for i in range(1, n+1):
    total += i
print("Sum of first", n, "natural numbers =", total)
print("\n")

# 32. Print a pattern of numbers increasing row-wise.
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print("\n")

# 33. Print a Floyd’s triangle.
num = 1
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(num, end=" ")
        num += 1
    print()
print("\n")

# 34. Print Pascal’s triangle using numbers.
from math import comb
rows = 5
for i in range(rows):
    for j in range(rows-i):
        print(" ", end="")
    for j in range(i+1):
        print(comb(i, j), end=" ")
    print()
print("\n")

# 35. Check if a number is prime using a loop.
n = 29
is_prime = True
for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        is_prime = False
        break
print(n, "is Prime?" , is_prime)
print("\n")

# 36. Generate first n prime numbers.
n = 10
count, num = 0, 2
while count < n:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1
print("\n")

# 37. Generate first n Fibonacci numbers using a loop.
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a+b
print("\n")

# 38. Reverse a number using a loop.
num = 12345
rev = 0
while num > 0:
    rev = rev*10 + num%10
    num //= 10
print("Reversed:", rev)
print("\n")

# 39. Check if a number is a palindrome using loop logic.
num = 121
temp, rev = num, 0
while temp > 0:
    rev = rev*10 + temp%10
    temp //= 10
print(num, "is Palindrome?", num == rev)
print("\n")

# 40. Count digits in a number using loop.
num = 123456
count = 0
temp = num
while temp > 0:
    count += 1
    temp //= 10
print("Digits in", num, "=", count)
print("\n")

# 41. Find the sum of digits of a number using loop.
num = 1234
sum_digits = 0
temp = num
while temp > 0:
    sum_digits += temp % 10
    temp //= 10
print("Sum of digits of", num, "=", sum_digits)
print("\n")

# 42. Check if a number is Armstrong using loop.
num = 153
temp = num
sum_pow = 0
digits = len(str(num))
while temp > 0:
    sum_pow += (temp % 10) ** digits
    temp //= 10
print(num, "is Armstrong?", sum_pow == num)
print("\n")

# 43. Find the GCD of two numbers using loop.
a, b = 56, 98
while b:
    a, b = b, a % b
print("GCD =", a)
print("\n")

# 44. Find the LCM of two numbers using loop.
x, y = 12, 15
a, b = x, y
while b:
    a, b = b, a % b
gcd = a
lcm = (x*y)//gcd
print("LCM =", lcm)
print("\n")

# 45. Generate a triangle pattern of numbers (1, 22, 333...).
rows = 5
for i in range(1, rows+1):
    print(str(i) * i)
print("\n")

# 46. Generate a pattern like: 1 2 3, 1 2, 1.
rows = 3
for i in range(rows, 0, -1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
print("\n")

# 47. Print all three-digit numbers that are Armstrong numbers.
for num in range(100, 1000):
    temp = num
    sum_pow = 0
    while temp > 0:
        sum_pow += (temp % 10) ** 3
        temp //= 10
    if sum_pow == num:
        print(num, end=" ")
print("\n")

# 48. Create a pattern with prime numbers only.
n = 5
count, num = 0, 2
while count < n:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1
print("\n")

# 49. Create a pattern with even numbers only.
rows = 5
num = 2
for i in range(1, rows+1):
    for j in range(i):
        print(num, end=" ")
        num += 2
    print()
print("\n")

# 50. Print number pyramid (1, 121, 12321...).
rows = 5
for i in range(1, rows+1):
    for j in range(1, i+1):
        print(j, end="")
    for j in range(i-1, 0, -1):
        print(j, end="")
    print()

# ============================================
# PART 8: Functions & Recursion — 50 Logic-Building Questions
# ============================================

# --------------------------------------------
# A. Basic Function-Based Logic (25 Questions)
# --------------------------------------------

# 1. Write a function to add two numbers.
def add_numbers(a, b):
    return a + b

# 2. Write a function to check if a number is even or odd.
def is_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

# 3. Write a function to find the factorial of a number.
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# 4. Write a function to calculate the square and cube of a number.
def square_cube(n):
    return n ** 2, n ** 3

# 5. Write a function that returns the maximum of three numbers.
def max_of_three(a, b, c):
    return max(a, b, c)

# 6. Write a function to count the number of vowels in a string.
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for ch in s if ch in vowels)

# 7. Write a function to find the sum of digits of a number.
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 8. Write a function to check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]

# 9. Write a function to check if a number is prime.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 10. Write a function that returns the reverse of a string.
def reverse_string(s):
    return s[::-1]

# 11. Write a function to check if a number is an Armstrong number.
def is_armstrong(n):
    digits = len(str(n))
    return n == sum(int(d) ** digits for d in str(n))

# 12. Write a function that takes a list and returns the largest element.
def largest_in_list(lst):
    return max(lst)

# 13. Write a function to count uppercase and lowercase letters in a string.
def count_case(s):
    upper = sum(1 for ch in s if ch.isupper())
    lower = sum(1 for ch in s if ch.islower())
    return upper, lower

# 14. Write a function to calculate the GCD of two numbers.
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 15. Write a function that returns the LCM of two numbers.
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 16. Write a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 17. Write a function to calculate simple interest.
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# 18. Write a function to print the Fibonacci series up to n terms.
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# 19. Write a function to convert decimal to binary.
def decimal_to_binary(n):
    return bin(n).replace("0b", "")

# 20. Write a function to remove all special characters from a string.
def remove_special_characters(s):
    return "".join(ch for ch in s if ch.isalnum() or ch.isspace())

# 21. Write a function to calculate the area of a circle.
def area_of_circle(radius):
    from math import pi
    return pi * radius * radius

# 22. Write a function to count words in a sentence.
def count_words(sentence):
    return len(sentence.split())

# 23. Write a function to convert a string into title case.
def to_title_case(s):
    return s.title()

# 24. Write a function to generate a random password.
import random, string
def generate_password(length=8):
    chars = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

# 25. Write a function to check if a number is perfect (sum of divisors = number).
def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# --------------------------------------------
# B. Recursion-Based Logic (25 Questions)
# --------------------------------------------

# 26. Write a recursive function to find the factorial of a number.
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# 27. Write a recursive function to find the nth Fibonacci number.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# 28. Write a recursive function to sum numbers from 1 to n.
def sum_recursive(n):
    if n == 0:
        return 0
    return n + sum_recursive(n - 1)

# 29. Write a recursive function to calculate power (a^b).
def power_recursive(a, b):
    if b == 0:
        return 1
    return a * power_recursive(a, b - 1)

# 30. Write a recursive function to reverse a string.
def reverse_string_recursive(s):
    if len(s) == 0:
        return ""
    return s[-1] + reverse_string_recursive(s[:-1])

# 31. Write a recursive function to count digits in a number.
def count_digits_recursive(n):
    if n == 0:
        return 0
    return 1 + count_digits_recursive(n // 10)

# 32. Write a recursive function to find the sum of digits of a number.
def sum_of_digits_recursive(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits_recursive(n // 10)

# 33. Write a recursive function to find the GCD of two numbers.
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

# 34. Write a recursive function to find the LCM of two numbers.
def lcm_recursive(a, b):
    return abs(a * b) // gcd_recursive(a, b)

# 35. Write a recursive function to find the nth term in an arithmetic progression.
def nth_ap_recursive(a, d, n):
    if n == 1:
        return a
    return nth_ap_recursive(a + d, d, n - 1)

# 36. Write a recursive function to find the maximum in a list.
def max_in_list_recursive(lst, n):
    if n == 1:
        return lst[0]
    return max(lst[n - 1], max_in_list_recursive(lst, n - 1))

# 37. Write a recursive function to check if a string is palindrome.
def is_palindrome_recursive(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])

# 38. Write a recursive function to print numbers from n to 1.
def print_n_to_1_recursive(n):
    if n == 0:
        return
    print(n, end=" ")
    print_n_to_1_recursive(n - 1)

# 39. Write a recursive function to convert a decimal number to binary.
def decimal_to_binary_recursive(n):
    if n == 0:
        return ""
    return decimal_to_binary_recursive(n // 2) + str(n % 2)

# 40. Write a recursive function to count the number of vowels in a string.
def count_vowels_recursive(s):
    if not s:
        return 0
    return (1 if s[0].lower() in "aeiou" else 0) + count_vowels_recursive(s[1:])

# 41. Write a recursive function to flatten a nested list.
def flatten_list_recursive(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat.extend(flatten_list_recursive(i))
        else:
            flat.append(i)
    return flat

# 42. Write a recursive function to find the sum of an array.
def sum_array_recursive(arr, n):
    if n == 0:
        return 0
    return arr[n - 1] + sum_array_recursive(arr, n - 1)

# 43. Write a recursive function to implement binary search.
def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)

# 44. Write a recursive function to implement linear search.
def linear_search_recursive(arr, n, target):
    if n == 0:
        return -1
    if arr[n - 1] == target:
        return n - 1
    return linear_search_recursive(arr, n - 1, target)

# 45. Write a recursive function to calculate compound interest.
def compound_interest_recursive(principal, rate, time):
    if time == 0:
        return principal
    return compound_interest_recursive(principal * (1 + rate / 100), rate, time - 1)

# 46. Write a recursive function to print a pattern (e.g., stars).
def star_pattern_recursive(n):
    if n == 0:
        return
    star_pattern_recursive(n - 1)
    print("*" * n)

# 47. Write a recursive function to calculate combinations (nCr).
def nCr_recursive(n, r):
    if r == 0 or r == n:
        return 1
    return nCr_recursive(n - 1, r - 1) + nCr_recursive(n - 1, r)

# 48. Write a recursive function to calculate permutations (nPr).
def nPr_recursive(n, r):
    if r == 0:
        return 1
    return n * nPr_recursive(n - 1, r - 1)

# 49. Write a recursive function to solve the Tower of Hanoi problem.
def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# 50. Write a recursive function to remove duplicates from a list.
def remove_duplicates_recursive(lst):
    
    if not lst:
        return []
    first, *rest = lst
    filtered_rest = remove_duplicates_recursive([x for x in rest if x != first])
    return [first] + filtered_rest
