
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 60)

t2 = (1, 2, 3, 4, 'five', 'six', 'seven', 'eight', True, False, 11.5, 12.7, 13.4, 14+2j, 15-8j)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 60)
t3 = tuple(range(1, 11))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 60)
t4 = 1,
print(f"t4 :{t4}")
print(type(t4))

print("-" * 60)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 60)
t1= (1, 2, 3, 4, 5)
print(f"t1[2] :{t1[2]}")

# t1[2] = 300  => tuples are immutable

print("-" * 60)
# print(dir(t1))

print(f"t1 :{t1}")

l1 = list(t1)
print(f"l1 :{l1}")

l1.extend([6, 7, 8, 9, 10])
print(f"l1 :{l1}")
print(type(l1))

t1 =tuple(l1)
print(f"t1 :{t1}")
