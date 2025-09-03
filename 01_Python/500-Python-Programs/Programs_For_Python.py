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