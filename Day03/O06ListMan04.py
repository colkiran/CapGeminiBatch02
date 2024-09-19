"""

sort  - will sort the original array
sorted  - take a copy of the list then sort it and return it

"""

l1 = [8, 4, 10, 6, 1, 3, 7, 9, 2, 5]
print(f"l1 :{l1}")

# sort these numbers
res_asc = sorted(l1)
print(f"Ascending order :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending order :{res_desc}")

print("-" * 60)
l2 = [8, 'zebra',  4, 'yellow',  10, 'blue', 6, 'xray', 1, 'green', "white", 3, 'maroon',  7, 'pink',  9, 'violet',  2, 'egg', 5, 'orange', 'cat', 'apple', 'egg', 179, 1245, 29, 265, 2134]

print(f"l2 :{l2}")

print("-" * 60)
res = sorted(l2, key=ascii)
print(f"res :{res}")

i = 0
for i in range(0, len(res)):
    if type(res[i]) == int:
        print(i)
        break

print("-" * 60)
print(res[:i] + sorted(res[i:]))

# -------------------------------------------------------

cities = ['thiruvananthapuram', 'delhi', 'ooty', 'bangalore', 'mumbai', 'vishakapatnam', 'chennai', 'hyderabad', 'pune']

# sort the cites based on their length


