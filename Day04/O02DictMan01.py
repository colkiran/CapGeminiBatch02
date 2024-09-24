
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)
d2 = {'name': 'lionel Messi', 'goals': 3, 'oppn': "Real madrid", 'venue': 'Lluis Companys'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 60)
d3 = dict([('empname', 'Mike'), ('age', 28), ('desig', "SE"), ('location', 'CA')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)
d4 = dict(name='Cristiano Ronaldo', age=32, goals=2, oppn= 'Barcelona')
print(f"d4 :{d4}")
print(type(d4))

# CRUD

# create
player = {'name': 'messi', 'age': 34, 'goals' : 23 , 'tournament' : 'Champions League'}
print(f"player :{player}")

print("-" * 60)
#read
print(f"Name        :{player['name']}")
print(f"Goals       :{player['goals']}")
print(f"Tournament   :{player['tournament']}")

print("-" * 60)
for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# update - changing the current value, adding a new key value

player['name'] = "Lionel Messi"
player['year'] = 2017

for i in player:
    print(i, "=>", player[i])

print("-" * 60)
# delete
del player['age']
del player['year']
print(f"player :{player}")

print("-" * 60)
print(dir(d1))



