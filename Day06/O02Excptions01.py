
import sys
x = 10
y = "0"
try:
    res = x / y
except:
    print("Exception raised......")
    print(sys.exc_info()[0])            # class
    print(sys.exc_info()[1])            # message

else:
    print("Exception not raised.....")
    print(f"res :{res}")
