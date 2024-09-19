
print("append".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

# add new elements into the list - we can add only one element
l1.append(6)
l1.append(7)
l1.append(8)
l1.append(9)

print(f"l1 :{l1}")

l1.append([10, 11, 12, 13, 14, 15])

print(f"l1 :{l1}")
print(f"l1[9][2:5] :{l1[9][2:5]}")

print("Extend".center(60, "-"))
l2 = [6, 7, 8, 9, 10]
print(f"l2 :{l2}")

l2.extend([11, 12, 13, 14])
print(f"l2 :{l2}")

l2.extend([15])
print(f"l2 :{l2}")

print("insert".center(60, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(10, 100)
print(f"l1 :{l1}")

print("pop".center(60, "-"))

l1 = list(range(10, 101, 10))
print(f"l1 :{l1}")

res = l1.pop(7)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")

res = l1.pop()
print(f"res :{res}")

print(f"l1 :{l1}")

print("remove".center(60, "-"))
l1 = [1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

print(l1.count(3))

l1.remove(3)
print(f"l1 :{l1}")
print(l1.count(3))

l1.remove(3)
print(f"l1 :{l1}")
print(l1.count(3))

l1.remove(3)
print(f"l1 :{l1}")
print(l1.count(3))

print("1 :", l1.count(1))
print("2 :", l1.count(2))

print("-" * 60)
l1 = [1, 1, 1, 1, 1, 2, 3, 1, 1, 2, 1, 2, 2, 2, 2, 2, 2, 1, 2, 3, 1, 2, 1, 2, 2, 1, 1, 1, 2, 3, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print(f"l1 :{l1}")

while(l1.count(2)):
    l1.remove(2)

print(f"l1 :{l1}")

print("clear".center(60, "-"))

l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")
