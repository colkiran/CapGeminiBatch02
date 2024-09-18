
st = "hello world"
print(f"st :{st}")
print(type(st))

print("-" * 60)
print(f"st[0] :{st[0]}")        # strings are stored like arrays or lists
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

print("-" * 60)
# slicing
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:]    :{st[:]}")

print("-" * 60)
# reverse indexing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 60)
# stnings are immutable
print(f"st :{st}")
print(f"st[0] :{st[0]}")

# st[0] = "H"
# check if the string is a palindrome or not using their indexes

print("-" * 60)
st="malayalam"
print(f"st :{st}")
print("Palindrome" if st[::1] == st[::-1] else "Not a Palindrome")

# if st[::1]==st[::-1]: print(f"{st} is a palindrome ")
print("-" * 60)
# we use functions to manipulate the strings
# print(dir(st))

# count, find, replace, index, split

st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print("count".center(60, "-"))
print(f"st1 :{st1}")

print("count of 'l' :", st1.count("l"))
print("count of 'o' :", st1.count("o"))

print(f"st2 :{st2}")
print("count of 'the' :", st2.count('the'))
print("count of 'fox' :", st2.count('fox'))
print("count of 'dog' :", st2.count('dog'))

print("count of 'o' :", st2.count("o"))

print("find".center(60, "-"))
print(f"st1 :{st1}")

print(st1.find("l"))
print(st1.find("l", st1.find("l")+1))
print(st1.find("l", st1.find("l", st1.find("l")+1)+1))

print("replace".center(60, "-"))
print(f"st1 :{st1}")

print(st1.replace("l", "L"))
print(st1.replace("l", "L", 2))
print(st1.replace("l", "L", 1))


