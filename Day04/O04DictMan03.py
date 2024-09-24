
print("setdefault".center(60, "-"))
# will only add new key value into the dictionary - it will not modify the existing

emp1 = {'empid': 1981, 'empname': 'Steve',  'desig': 'TL', 'dept': 'finance'}
print(f"emp1 :{emp1}")

print("-" * 60)
emp1.setdefault('empid', 1000)
emp1.setdefault('age', 34)
emp1.setdefault('dept', "IT")
emp1.setdefault('salary', 8000)

print(f"emp1 :{emp1}")

print("update".center(60, "-"))
emp1 = {'empid': 1981, 'empname': 'Steve', 'age': 29, 'desig': 'TL', 'dept': 'finance'}

print(f"emp1 :{emp1}")

emp2 = {'empid': 2252, 'empname': 'Tina', 'age': 32, 'desig': 'PM', 'salary': 6600}

print(f"emp2 :{emp2}")

# update emp1 with emp2's values

print("-" * 60)

emp1.update(emp2)

print(f"emp1 :{emp1}")

print("clear".center(60, "-"))
emp2 = {'empid': 2252, 'empname': 'Tina', 'age': 32, 'desig': 'PM', 'salary': 6600}

print(f"emp2 :{emp2}")
emp2.clear()

print(f"emp2 :{emp2}")

print("copy".center(60, "-"))
emp1 = {'empid': 2252, 'empname': 'Tina', 'age': 32, 'desig': 'PM', 'salary': 6600}

print(f"emp1 before :{emp1}")

# copy emp1 to emp2

emp2 = emp1     # shallow copy - copying the address with the data

print(f"emp2 before :{emp2}")

emp2['dept'] = "MKT"
emp2['location'] = 'CA'

print(f"emp2 after :{emp2}")
print(f"emp1 after :{emp1}")

print("=" * 60)
print("=" * 60)

emp3 = {'empid': 5345, 'empname': 'Kevin', 'age': 41, 'desig': 'GM', 'salary': 8600}
print(f"emp3 before :{emp3}")

# copy emp3 to emp4

emp4  = emp3.copy()

print(f"emp4 before :{emp4}")

print("-" * 60)
emp4['dept'] = "Finance"
emp4['location'] = "LA"

print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("=" * 60)
print("=" * 60)

emp5 = {'empid': 3253, 'empname': 'Ruben', 'age': 35, 'desig': {'HP': 'SE', 'IBM': 'TL', 'TCS': 'MGR'}, 'salary': 6000}
print(f"emp5 before :{emp5}")

# copy emp5 to emp6

emp6 = emp5.copy()

print(f"emp6 before :{emp6}")

emp6['desig']['cts'] = 'AGM'
emp6['desig']['dell'] = "GM"

print("-" * 60)

print(f"emp6 after :{emp6}")
print(f"emp5 after :{emp5}")

print("=" * 60)
print("=" * 60)

emp7 = {'empid': 4434, 'empname': 'David', 'age': 46, 'desig': {'HP': 'SE', 'IBM': 'TL', 'TCS': 'MGR'}, 'salary': 6000}

print(f"emp7 before :{emp7}")

# copy emp7 to emp8
from copy import deepcopy
emp8 = deepcopy(emp7)

print(f"emp8 before :{emp8}")

emp8['desig']['cts'] = 'AGM'
emp8['desig']['dell'] = "GM"

print("-" * 60)

print(f"emp8 after :{emp8}")
print(f"emp7 after :{emp7}")


