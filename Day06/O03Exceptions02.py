

try:
    num = int(input("Enter a number :"))
    # inv = 0
    inv = 1 / num
    print(f"The inverse is :{inv}")
# except Exception as e:
#     print("This is exception......")
#     print(e)
except ZeroDivisionError as z:
    print("Eception Occured......")
    print(z)
except TypeError as t:
    print("Exception Occured......")
    print(t)

except ValueError as v:
    print("Exception Occured......")
    print(v)

finally:
    print("Completed dividing numbers......")
