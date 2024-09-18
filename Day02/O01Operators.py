
print("Arithmetic Operators".center(60, "-"))
print(f"Add 10 + 3 = {10 + 3}")
print(f"Sub 10 - 3 = {10 - 3}")
print(f"Mul 10 * 3 = {10 * 3}")
print(f"Div 10 / 3 = {10 / 3}")
print(f"flrdiv 10 // 3 = {10 // 3}")
print(f"mod 10 % 3 = {10 % 3}")
print(f"pow 10 ** 3 = {10 ** 3}")

print("Augmentor Operator".center(60, "-"))
# =, +=, -=, /=, *=
x = 10

print(f"x :{x}")
x += 5      # x = x + 5

print(f"x :{x}")
x /= 3

print(f"x :{x}")

print("Comparison Operators".center(60, "-"))
# ==, >, <, >=, <=, !=
print(f"1 == 1 :{1 == 1}")
print(f"1 < 2 :{1 < 2}")

print(f"1 > 2 :{1 > 2}")
print(f"1 == 1 :{1 == 2}")
print(f"1 != 2 :{1 != 2}")

print("Logical Operator".center(60, "-"))
# and, or, not

print(f"1 == 1 and 1 == 1 :{1 == 1 and 1 == 1}")
print(f"1 == 1 and 1 == 2 :{1 == 1 and 1 == 2}")

print("-" * 60)
print(f"1 == 1 or 1 == 2 :{1 == 1 or 1 == 2}")
print(f"1 == 2 or 2 == 1 :{1 == 2 or 2 == 1}")

print("-" * 60)
print(f"not(1 == 1 or 1 == 2) :{not(1 == 1 or 1 == 2)}")
print(f"not(1 == 2 or 2 == 1) :{not(1 == 2 or 2 == 1)}")

print("-" * 60)
print(f"ord('a') :{ord('a')}")      # integer representation of
                                    # unicode characters
print(f"ord('z') :{ord('z')}")
print(f"ord('A') :{ord('A')}")
print(f"ord('Z') :{ord('Z')}")

print("-" * 60)
print(f"chr(65) :{chr(65)}")
print(f"chr(97) :{chr(97)}")

print("apple" > "orange")
print("orange" > "apple")

print("Bitwise Operators".center(60, "-"))

print(f"5 | 3 : {5 | 3}")
print(f"5 & 3 : {5 & 3}")
print(f"5 ^ 3 : {5 ^ 3}")

print(f"5 << 1 : {5 << 1}")
print(f"8 << 1 : {8 << 1}")
print(f"5 << 2 : {5 << 2}")
print(f"16 >> 1 : {16 >> 1}")
print(f"5 >> 1 : {5 >> 1}")

print("Ternary Operator".center(60, "-"))
age = 18
print("Eigible" if age > 17 else "Not Eligible")
