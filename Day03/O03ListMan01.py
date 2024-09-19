
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 60)
l2 = [1, 2, 3, 4, 5, 6.9, 7.0, 8.1, 9.5, 'ten', 'eleven', 'twelve', 'thirteen', 14+3j, 15-2j, True, False ]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
# CRUD

# create
l1 = ['Jack', 'Mike', 'Dave', 'Tina', 'Mary', 'John']
print(f"l1 :{l1}")

# read
print(f"l1[0] :{l1[0]}")
print(f"l1[4] :{l1[4]}")
print(f"l1[-1] :{l1[-1]}")

print("-" * 60)
for x in l1:
    print(x, end=" ")
print()

print("-" * 60)
# update (modify - add new value or replace the existing)
# add a new value
print(f"l1 :{l1}")
l1[2] = "Richard"
l1[5] = "Peter"

# we cannot insert new elements (arrays are static in python)
print(f"l1 :{l1}")

print("-" * 60)
# delete
print(f"l1 :{l1}")
del[l1[4]]
del[l1[0]]

print(f"l1 :{l1}")

print("-" * 60)
print(dir(l1))

