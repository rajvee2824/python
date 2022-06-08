# Python program to find the sum of natural using recursive function

def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)


# change this value for a different result
num = int(input("How many terms? "))

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recur_sum(num))


# Factorial of a number using recursion

def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


num = int(input("How many terms? "))


# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
# Function to print binary number using recursion


def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end='')


# decimal number
dec = int(input("enter the number= "))


convertToBinary(dec)
print()
