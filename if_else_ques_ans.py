# Q1 Write a program that takes an integer input from the user and checks whether the number is odd or
#  even.
# n = int (input("enter number :"))
# if (n%2==0):
#     print("even nmber ")
# else:
#     print("odd number ")


# Q2 Write a program that takes three numbers as input and prints the largest of the three.
# a = int (input("enter 1st number "))
# b = int (input("enter 2nd number "))
# c = int (input("enter 3rd number "))

# if(a>b and a>c):
#     print("a is largeet number :")

# elif(b>a and b>c):
#     print("b is largest number :")

# else:
#     print("c is largest number :")


# Q3 Write a program to check if a given year is a leap year. A leap year is divisible by 4 but not by 100
# unless it is also divisible by 400.

# n = int (input ("enter year :"))
# if (n%4 == 0):
#     if (n%100!=0):
#         print("leap year :")

#     else:
#         print("leap year :")

# else:
#     print("not a leap year :")


# Q4 Write a program that takes a percentage (integer) as input and prints the corresponding grade based
# on the following criteria:
# >= 90: Grade A
# >= 80: Grade B
# >= 70: Grade C
# >= 60: Grade D
# < 60: Grade F

# n = int (input("Enter your percentage :"))

# if (n >= 90 ):
#     print("Grade A :")
# elif (n>=80 and n<90 ):
#     print("Grade B :")
# elif (n>=70 and n<80 ):
#     print("Grade c :")
# elif (n>=60 and n<70 ):
#     print("Grade D :")
# else:
#     print("Grade F :")


# Q5 Write a program that checks if a given letter is a vowel (a, e, i, o, u) or a consonant.

# n = input("Enter a character: ")  
# if (n in "aeiouAEIOU"):  
#     print("Vowel")
# else:
#     print("Consonant")


#Q6 Write a basic calculator program that takes two numbers and an operator (+, -, *, /) as input and
# performs the specified operation. Print the result based on the operation.


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# op = input("Enter operator (+, -, *, /): ")

# if (op == "+"):
#     print("Result =", a + b)
# elif (op == "-"):
#     print("Result =", a - b)
# elif (op == "*"):
#     print("Result =", a * b)
# elif (op == "/"):
#     if (b != 0):
#         print("Result =", a / b)
#     else:
#         print("Error: Division by zero not allowed!")
# else:
#     print("Invalid operator entered!")


#Q7 Write a program that takes a number as input and checks whether it is positive, negative, or zero.

# n = int (input("enter number :"))

# if (n>0):
#     print("positive number :")
# elif (n<0):
#     print("negative number :")
# else:
#     print("number is zero :")


# Q8 Write a program that checks if a username and password entered by the user match the pre-set values
# username = "admin" and password = "1234". If both match, print "Login Successful", otherwise print
# "Login Failed".

# a = input("enter your username :")
# b = input("enter your passwrod :")

# if (a == 'admin'):
#     if (b== '1234'):
#         print("login successful :")
#     else:
#         print("login faild :")
# else:
#     print("login faild :")


# Q9 Write a program that takes three sides of a triangle as input and checks if those sides form a valid
# triangle. A triangle is valid if the sum of any two sides is greater than the third side.
# Check conditions like a + b > c, b + c > a, and a + c > b.

# a = float(input("Enter side 1: "))
# b = float(input("Enter side 2: "))
# c = float(input("Enter side 3: "))

# if (a + b > c) and (b + c > a) and (a + c > b):
#     print("The sides form a valid triangle.")
# else:
#     print("invalid triangle.")


# Q11 Write a program that calculates the discount for a product based on its price:
# If price is greater than 1000, discount is 10%
# If price is between 500 and 1000, discount is 5%
# Otherwise, no discount
# Print the final price after applying the discount.

# n = int(input ("enter price :"))

# x = n*(10/100)
# y = n*(5/100)
# if(n>=1000):
#     print("discpunt is 10% : ", n - x )

# elif (n>=500 and n<1000):
#     print("discount is 5% :", n - y )

# else :
#     print("no discount :")


# Q12 Write a program that takes the name of a month as input and prints the number of days in that
# month. Consider leap years for February.

# n = input ("Enter a month name : ")

# if(n == 'january' or n == 'march' or  n =='may' or n == 'july' or n == 'september' or n == 'november'):
#     print("31 days ")

# elif(n == 'february'):
#     print("leap year")

# else:
#     print("30 days ")


#  Q13 Write a program that simulates a simple ATM. The user should be able to:
#  Check balance
#  Deposit money
#  Withdraw money (ensure the balance doesn't go negative) Use an if-else structure to handle the user's choices

# balance = 10000
# deposite = 0
# withdrawl = 0 
# print("1. check balance :")
# print("2. deposite money :")
# print("3. withdrawl money :")

# n = int(input("enter the number :"))

# if (n == 1):
#     print(balance)

# elif (n == 2 ):
#     deposite = int(input("enter the deposite money amount :"))
#     if (deposite > 0):
#         print("total balnace is : ",deposite + balance)
#     else:
#         print("invalid number :")
# elif (n == 3):
#     withdrawl = int(input("enter the withdrawl amount :")) 
#     if (withdrawl<balance):
#         print("remaining balnce is ",balance - withdrawl)
#     else:
#         print("insuficient balance :")


# Q14 Write a program that categorizes a given age into different groups:
# Infant (0-1 year)
# Toddler (2-4 years)
# Child (5-12 years)
# Teenager (13-19 years)
# Adult (20-59 years)
# Senior (60 years and above)

# n = int (input ("enter age :"))

# if (n>0 and n<=1):
#     print("infant")
# elif(n>=2 and n<=4):
#     print("toodler")
# elif(n>=5 and n<=12):
#     print("child")
# elif(n>=13 and n<=19):
#     print("tennager")
# elif(n>=20 and n<=59):
#     print("adult")
# elif (n>=60):
#     print("senior")


# Q15 Write a program that takes an integer (1-7) as input and prints the corresponding day of the week (1
# for Monday, 2 for Tuesday, etc.).

# n = int (input("enter number b/w 1 to 7 "))

# if (n == 1):
#     print("monday :")
# elif(n == 2):
#     print("tuesday :")
# elif(n == 3):
#     print("wednesday :")
# elif(n == 4):
#     print("thursday :")
# elif(n == 5):
#     print("friday :")
# elif(n == 6):
#     print("saturday :")
# elif(n == 7):
#     print("sunday :")

# else:
#     print("invalid :")


# Q10 doubt