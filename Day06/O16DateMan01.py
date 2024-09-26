
from datetime import datetime

dt = datetime.now()
print(f"Current Date and Time :{dt}")

print("-" * 60)
print("Day :", dt.strftime("%a"))
print("Day :", dt.strftime("%A"))

print("-" * 60)
print("Month :", dt.strftime("%b"))
print("Month :", dt.strftime("%B"))

print("-" * 60)
print("Date :", dt.strftime("%d"))
print("Date :", dt.strftime("%D"))
print("Date :", dt.strftime("%x"))

print("-" * 60)
print("Year :", dt.strftime("%y"))
print("Year :", dt.strftime("%Y"))

print("-" * 60)
print("Time :", dt.strftime("%T"))
print("Time :", dt.strftime("%X"))

print("-" * 60)
dt1 = dt.strftime("%d-%m-%y")
print(f"dt1 :{dt1}")

print("-" * 60)
dt2 = dt.strftime("%d-%m-%Y")
print(f"dt2 :{dt2}")

print("-" * 60)
dt3 = dt.strftime("%d-%b-%Y")
print(f"dt3 :{dt3}")

print("-" * 60)
dt4 = dt.strftime("%d-%B-%Y")
print(f"dt4 :{dt4}")
