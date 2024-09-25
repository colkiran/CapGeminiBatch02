print("-" * 60)
# return
def multiplyMe(x, y):
    return x * y

print(f"The product of 5, 6 is :{multiplyMe(5, 6)}")

print("-" * 60)
# recursive calls
# def fun(x):
#     print(x)
#     fun(x - 1)
#
# fun(10)

"""
use recursive calls and find
1. factorial of a number
2. fibonacci series
"""
def arithmeticCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    mod = x % y
    return sum, diff, prod, quot, mod

res = arithmeticCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# passing argumnents
# variable length arguments

def prodAll(*numbers):
    # accept more than one value - like tuple
    print(f"numbers  :{numbers}")
    print("*numbers :", *numbers)     # unpack
    prod = 1
    for number in numbers:
        prod *= number
    return prod


res = prodAll(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extractDetails(**player):
    # accepts argument like a dictionary (**kwargs - key word arguments)
    print(f"player :{player}")
    # items function return both keys and values
    for ky, vl in player.items():
        print(ky, "=>", vl)

extractDetails(name="Jordan", age=32, goals=75, year=1994)

print("-" * 60)

def fun():
    # this is a comment
    "this is a doc string"
    print("hello world")

fun()
print(fun.__doc__)

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    ----------

    1. if x and y are integers then the result would the sum of x and y
    2. if x and y are strings then the result would be concatenated str
    3. if x and y are of two different data types then throws an error
    """
    print(x + y)

fun1(10, 20)
fun1("hello", " world")

print("-" * 60)
help(fun1)
