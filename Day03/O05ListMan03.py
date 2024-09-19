
print("index".center(60, "-"))
l1 = [1, 1, 1, 2, 3, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print("First :", l1.index(3))
print("First :", l1.index(3 ,l1.index(3) + 1))
print("First :", l1.index(3 ,l1.index(3, l1.index(3) + 1) + 1))

print("copy".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")
# copy the list l1 to l2

l2 = l1         # shallow copy - the address is also shared with the data

print(f"l2 before :{l2}")
l2.append(6)
l2.append(7)
l2.append(8)

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)

l3 = [5, 6, 7, 8, 9]
print(f"l3 before :{l3}")

# copy the list l3 to l4

l4 = l3.copy()          # deep copy - only data gets copied

print(f"l4 before :{l4}")

l4.extend([10, 11, 12, 13])

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)

l5 = [1, 2, 3, [10, 20, 30], 4, 5]
print(f"l5 :{l5}")

# copy the list l5 to l6

l6 = l5.copy()

print(f"l6 before :{l6}")

l6[3].append(40)
l6[3].append(50)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)

l7 = [1, 2, 3, 4, 5, [5, 10, 15, 20]]
print(f"l7 before :{l7}")

# copy the list l7 to l8
from copy import deepcopy

l8 = deepcopy(l7)       # deepcopy

print(f"l8 before :{l8}")

l8[5].append(25)
l8[5].append(26)
l8[5].append(27)
l8[5].append(28)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")



