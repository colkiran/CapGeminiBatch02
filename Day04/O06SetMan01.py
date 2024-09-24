
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 60)
s2 = {1, 2, 3, 4, 5.1, 6.9, 7.3, 8.5, 9 + 2j, 10 - 0j, 'eleven', 'twelve', 'thirteen', 'fourteen', True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 60)
s3 = set(range(1, 6))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 60)
s1 = {1, 2}
print(f"s1 :{s1}")

print("add".center(60, "-"))
s1.add(3)
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(1)
s1.add(3)
s1.add(3)

print(f"s1 :{s1}")

print("update".center(60, "-"))
s1.update([1, 2, 3])
s1.update([4, 5, 6])
s1.update([2, 3, 4])
s1.update([6, 7, 8])
s1.update([5, 6, 7])
s1.update([8, 9, 10])

print(f"s1 :{s1}")
# pop, remove, discard
print("pop".center(60, "-"))

print(f"s1 :{s1}")

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

print('remove'.center(60, "-"))

print(f"s1 :{s1}")
s1.remove(8)
s1.remove(6)
# s1.remove(1)

print(f"s1 :{s1}")

print("discard".center(60, "-"))
s1 = set(range(1, 11))
print(f"s1 :{s1}")

s1.discard(6)
s1.discard(1)
s1.discard(5)

s1.discard(1)
print(f"s1 :{s1}")

print("-" * 60)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print(f"A | B :{A | B}")
print(f"A union B :{A.union(B)}")

print("-" * 60)
print(f"A & B :{A & B}")
print(f"A intersection B :{A.intersection(B)}")

print("-" * 60)
print(f"A differece B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 60)
print(f"A symmetric difference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

# sets are mutable

# frozenset - immutable

a = frozenset([1, 2, 3, 4, 5])
print(f"a :{a}")
print(type(a))

