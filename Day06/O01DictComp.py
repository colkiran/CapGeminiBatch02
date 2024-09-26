
players = {
    'sachin': [350, 250, 300, 400, 385],
    'rahul': [200, 300, 450, 150, 185],
    'sehwag':[300, 350, 425, 400, 360],
    'sourav':[180, 250, 200, 350, 150],
    'laxman':[345, 300, 200, 150, 190],
    'yuvraj':[190, 150, 120, 250, 275]
}

print(f"players :{players}")
print("-" * 60)

print(f"sachin :{players['sachin']}")
print("-" * 60)

print(f"sachin :{sum(players['sachin'])}")
print("-" * 60)

points = {k: sum(v) for k, v in players.items()}
print(f"points :{points}")
print("-" * 60)

# calculate average of points for each player
points = {k: (lambda x : sum(x) / len(x)) (point)
          for k, point in players.items()}
print(f"points :{points}")
print("-" * 60)

points = [point for point in players.values()]
print(f"points :{points}")
print("-" * 60)

points = [pnt for point in players.values() for pnt in point if pnt >= 200]
print(f"points :{points}")
print("-" * 60)

points = {k: [pnt for pnt in point if pnt > 200]
          for k, point in players.items()}
print(f"points :{points}")

