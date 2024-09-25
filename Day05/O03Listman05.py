
values = list(range(10, 31, 10))
print(f"values :{values}")

# upack the list
a, b, c = values
print(a, b, c, sep=", ")

print("-" * 60)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=",  ")

print("-" * 60)
a, *b, c = values
print(a, b, c, sep=",  ")

print("-" * 60)
*a, b, c = values
print(a, b, c, sep=",  ")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44 ,55]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(f"len(lst3) :{len(lst3)}")

print("-" * 60)
# unpack
lst4 = [*lst1, *lst2]
print(f"lst4 :{lst4}")
print(f"len(lst4) :{len(lst4)}")

print("-" * 60)
# enumerate

letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"letters :{letters}")

for letter in letters:
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 60)
for letter in enumerate(letters):
    print(letter[0], "\t",  letter[1])

print("-" * 60)
def fun(*names):
    print(names)

fun("John", 'Richard', "Micheal", 'Kevin', 'Peter')
