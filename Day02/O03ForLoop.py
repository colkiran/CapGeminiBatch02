
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(3, 31, 3):
    print(i, end = " ")
print()

print("-" * 60)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 60)

for i in range(1, 36):
    # if i > 25:
    #     break           # stop the iteration
    if i % 2 == 1:
        continue        # skip the iteration
    print(i, end = " ")
else:
    print("\nCompleted the iteration.....")

print()

print("-" * 60)

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

