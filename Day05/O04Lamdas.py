
def add(x, y):
    return x + y

a = add
res = a(35, 87)
print(f"res :{res}")

print("-" * 60)

b = lambda x, y : x + y
res = b(43, 67)

print(f"res :{res}")

print("-" * 60)
# lambdas are best used with - map, reduce and filter
"""
map - expression is written in lambdas, this expression is mapped to a list 
"""
l1 = list(range(1, 11))
print(f"l1 :{l1}")

squares = list(map(lambda x : x ** 2, l1))
print(f"squares :{squares}")

print("-" * 60)
months = ['dec', 'oct', 'aug', 'nov', 'sep', 'jan', 'apr', 'feb', 'may', 'jun', 'mar', 'jul']

print(f"Unsorted Months :{months}")

print("-" * 60)
from calendar import month_abbr
print(list(month_abbr))


print("-" * 60)
sorted_months = sorted(months, key=list(map(lambda mth: mth.lower(), list(month_abbr))).index)

print(f"sorted_months :{sorted_months}")

print("-" * 60)
# filters - expression should return a True or a false

l1 = list(range(1, 31))
print(f"l1 :{l1}")

print("-" * 60)
multiple_three = list(filter(lambda x : x % 3 == 0, l1))
print(multiple_three)

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

res = list(filter(lambda x : x != 'the', sentence.split()))
print(f"res :{res}")

print("-" * 60)
# reduce - list gets reduced into a single value

l1 = [9, 7, 3, 5, 10, 8, 6]
print(f"l1 :{l1}")

from functools import reduce
res = reduce(lambda x, y : x if x < y else y, l1)
print(f"res :{res}")

res = reduce(lambda x, y : x + y, l1)
print(f"res :{res}")

