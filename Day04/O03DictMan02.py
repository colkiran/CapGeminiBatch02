
print("keys".center(60, "-"))

emp = {'empid': 1209, 'empname': 'Peter', 'age': 38, 'desig': 'Manager', 'salary': 8000}
print(f"emp :{emp}")

k = emp.keys()
print(k)

print("-" * 60)
for k in emp.keys():
    print(k + " => " + str(emp[k]))

print("values".center(60, "-"))

emp = {'empid': 1209, 'empname': 'Peter', 'age': 38, 'desig': 'Manager', 'salary': 8000}
print(f"emp :{emp}")

v = emp.values()
print(v)

print("items".center(60, "-"))

emp = {
    'emp1': {'empid': 1981, 'empname': 'Steve', 'age': 29, 'desig': 'TL', 'salary': 4500, 'dept': 'finance'},
    'emp2': {'empid': 2252, 'empname': 'Tina', 'age': 32, 'desig': 'PM', 'salary': 6600, 'dept': 'IT'},
    'emp3': {'empid': 3936, 'empname': 'Kevin', 'age': 38, 'desig': 'MGR', 'salary': 7200, 'dept': 'MKT'}
}

print(f"emp :{emp}")

print("-"  * 60)

print(f"emp1 :{emp['emp1']}")

print("-"  * 60)

print(f"emp2 :{emp['emp2']}")

print("-"  * 60)

print(f"emp3 :{emp['emp3']}")

print("-"  * 60)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 60)

print("fromkeys".center(60, "-"))
# used to convert a list to a dictionary

states = ['CA', 'SF', 'NY', 'FL', 'KY']
print(f"states :{states}")

res = dict.fromkeys(states)
print(f"res :{res}")

res = dict.fromkeys(states, 20)
print(f"res :{res}")

print('get'.center(60,  "-"))

emp1 = {'empid': 1981, 'empname': 'Steve', 'age': 29, 'desig': 'TL', 'salary': 4500, 'dept': 'finance'}

print(f"emp1 :{emp1}")

print("-" * 60)
print(f"emp1['desig] :{emp1.get('desig')}")
print(f"emp1['desig] :{emp1.get('desg', 'Invalid Key')}")

print("pop".center(60, "-"))

emp1 = {'empid': 1981, 'empname': 'Steve', 'age': 29, 'desig': 'TL', 'salary': 4500, 'dept': 'finance'}

print(f"emp1 :{emp1}")

print("-" * 60)

res = emp1.pop('age')
print(f"res:{res}")

res = emp1.pop('salary')
print(f"res:{res}")

# res = emp1.pop()
# print(f"res:{res}")

print(f"emp1 :{emp1}")

print("popitem".center(60, "-"))

emp1 = {'empid': 1981, 'empname': 'Steve', 'age': 29, 'desig': 'TL', 'salary': 4500, 'dept': 'finance'}

print(f"emp1 :{emp1}")
print("-" * 60)

res = emp1.popitem()
print(f"res:{res}")

res = emp1.popitem()
print(f"res:{res}")

print(f"emp1 :{emp1}")

