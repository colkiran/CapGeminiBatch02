# c style
print("Welcome %s, what a %s player" % ("Jordan", "superb"))
print("Welcome %s, what a %s player with a rating of %.2f" % ("Jordan", "superb", 9.76548323))

print("-" * 60)
# interpolation
gname = "Jordan"
adj = "class"
rating = 9.68903
print(f"Welcome {gname}, what a {adj} player with a rating {rating}")

print("-" * 60)
# python string formatting
print("Welcome {gname}, what a {adj} player with a rating {rating}".format(gname="Jordan", adj="class", rating=9.67645))

print("Welcome {}, what a {} player with rating {:.2f}".format("Jordan", "superb", 9.7892123))

print("-" * 60)
print("{val} {val} {val}".format(val = "A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("-" * 60)
print("{num} {num} {num}".format(num = 36))
print("{num} {num:f} {num:b}".format(num = 36))
print("{num:10} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 36))
print("{num:5} {num:f} {num:b}".format(num = 3689234168))

print("-" * 60)
# alignment
print("{}".format("Micheal Jordan"))
print("{:.7}".format("Micheal Jordan"))

print("-" * 60)
from math import pi
print(f"pi :{pi}")
print("{pi:10.2}".format(pi = pi))
print("{pi:10.3}".format(pi = pi))
print("{pi:10.4}".format(pi = pi))
print("{pi:10.5}".format(pi = pi))

print("-" * 60)
print("{val:15} Jordan".format(val = "Micheal"))
print("{val:15} Jordan".format(val = 105.276))
print("{val:015} Jordan".format(val = 105))

print("-" * 60)
print("{val:>15} Jordan".format(val = "Micheal"))
print("{val:^15} Jordan".format(val = "Micheal"))
print("{val:<15} Jordan".format(val = "Micheal"))

print("-" * 60)
print("Micheal Jordan".center(60, "-"))
print("{val:-^60}".format(val="Micheal Jordan"))