
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n - 1)

x = int(input("Enter the number to find its factorial :"))
print(f"The factorial of {x} is :{fact(x)}")
