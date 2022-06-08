base = int(input("enter the number:- "))
exponent = int(input("enter the number:- "))

result = 1

while exponent != 0:
    result *= base
    exponent -= 1

print("Answer = " + str(result))
