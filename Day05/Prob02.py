
def fibo(n):
    if n == 1 or n == 0:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

x = int(input("Enter the no of fibonacci numbers to be generated :"))
for i in range(0, x):
    print(fibo(i), end=" ")

