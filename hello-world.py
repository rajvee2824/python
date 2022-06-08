print("hello")
a = "32323233"
a = int(a)
print(type(a))
print(a)
print(a+5)

r = "yashraj"
print(r[0:5])
print(r[0::5])


def my_function():
    print("Hello from a function")


my_function()
def x(a, b, c): return a + b + c


print(x(5, 6, 2))


def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
