# count, find, replace, index, split

print("count".center(60, "-"))
# count will allow to take a count of how many times a character is repeated

st = "hello world"
print(f"st :{st}")

print("l :", st.count("l"))
print("o :", st.count("o"))

print("find".center(60, "-"))
st = "hello world"
print(f"st :{st}")

print(st.find("l"))
print(st.find("l", st.find("l") + 1))      # strart searching from 3rd pos
print(st.find("l", st.find("l", st.find("l") + 1) + 1))

print("replace".center(60, "-"))
st = "hello world"
print(f"st :{st}")

print(st.replace("l", "L"))
print(st.replace("l", "L", 2))
print(st.replace("l", "L", 1))

print("split".center(60, "-"))
# converts a string into a list
st = "the quick brown fox jumps over the lazy dog"
print(f"st :{st}")
print(type(st))

res = st.split()        # delimiter is space by default
print(f"res: {res}")
print(type(res))

print(f"res[0] :{res[0]}")
print(f"res[3] :{res[3]}")
print(f"res[7] :{res[7]}")
print(len(res))

# maketrans, translate'
print('maketrans'.center(60, "-"))
st = "hello world"
print(f"st :{st}")
# length of a and b should be the same
a = "helowrd"
b = "HELOWRD"
resTbl = st.maketrans(a, b)
print(resTbl)

print("translate".center(60, "-"))
res = st.translate(resTbl)
print(f"res :{res}")

print("-" * 60)
st = "one two new teen vote"      # => six
print(f"st :{st}")

a = "one"
b = "six"

Tbl = st.maketrans(a, b)
print(Tbl)

res = st.translate(Tbl)
print(res)
