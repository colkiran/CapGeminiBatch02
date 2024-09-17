
"""
1. integer
2. float
3. complex
"""

a = 10
b = -10
print(f"a :{a}")
print(type(a))        # RTTI - Run Time Type Identification
print(f"b :{b}")
print(type(b))

print("-" * 60)
c = 10.2
d = -10.2
print(f"c :{c}")
print(type(c))
print(f"d :{d}")
print(type(d))

print("-" * 60)
e = +2e3        # 2 * e ** 3 => 2 * 1000 = 2000.0
f = -2e3

print(f"e :{e}")
print(type(3))
print(f"f :{f}")
print(type(f))

print("-" * 60)
g = 3 + 2j
h = 3 - 2j

print(f"g :{g}")
print(type(g))
print(f"h :{h}")
print(type(h))

print("-" * 60)
print(10, 23, 4, 8, 15, 18, 3, 5)
print(max(10, 23, 4, 8, 15, 18, 3, 5))
print(min(10, 23, 4, 8, 15, 18, 3, 5))

# i = 10
# print(dir(i))
print("-" * 60)
x = 2 + 3.5
print(f"x :{x}")
print(type(x))

print("-" * 60)
x = 3
y = 2.5
z = x + y
print("x = ", type(x))
print("y = ", type(y))
print("z = ", type(z))

print("conversion".center(60, "-"))
a = 100
print(f"{type(a)}\t\t{a}")
print(f"{type(float(a))}\t\t{float(a)}")
print(f"{type(complex(a))}\t\t{float(a)}")
print(f"{type(bool(a))}\t\t{bool(a)}")

print("Number System".center(60, "-"))
print(11)       # decimal
print(0b11)     # binary = 0b11  -     "1 * 2 ** 1 + 1 * 2 ** 0
print(0b101)    # 1 * 2 ** 2 + 0 + 1 * 2 ** 0
print(0o11)     # base 8
print(0o111)     # base 8

print(0xe)
print(0xa)      # hexa

print("Number conversions".center(60, "-"))
a = 100
print(f"binary 100 :{bin(a)}")
print(f"Octal 100 :{oct(a)}")
print(f"Hexa 100 :{hex(a)}")

