

def recur_sum(n):
    if n <= 1:
        return n
    else:
        return n + recur_sum(n-1)


num = int(input("How many terms? "))

if num < 0:
    print("Enter a positive number")
else:
    print("The sum is", recur_sum(num))


def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)


num = int(input("How many terms? "))


if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))


def convertToBinary(n):
    if n > 1:
        convertToBinary(n//2)
    print(n % 2, end='')


dec = int(input("enter the number= "))


convertToBinary(dec)
print()
