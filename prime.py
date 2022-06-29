
num = int(input("Enter a number: "))


flag = False


if num > 1:

    for i in range(2, num):
        if (num % i) == 0:

            flag = True

            break


if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

lower = 700
upper = 800

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):

    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)
