
cities = ['thiruvananthapuram', 'delhi', 'ooty', 'bangalore', 'mumbai', 'vishakapatnam', 'chennai', 'hyderabad', 'pune']

print(f"cities :{cities}")

print("-" * 60)

res_asc = sorted(cities, key=len)
print(f"Ascending :{res_asc}")

print("-" * 60)
res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending :{res_desc}")

print("reversed".center(60, "-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")
