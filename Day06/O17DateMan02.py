from datetime import datetime
import dateutils

dt1 = "Thursday, September 26, 2024"
print(f"dt1 :{dt1}")
print(type(dt1))

print("-" * 60)
dt2 = "Wednesday, September 20, 2023"
print(f"dt2 :{dt2}")
print(type(dt2))

print("-" * 60)
actdt1 = datetime.strptime(dt1, "%A, %B %d, %Y")
print(f"actdt1 :{actdt1}")
print(type(actdt1))

print("-" * 60)
actdt2 = datetime.strptime(dt2, "%A, %B %d, %Y")
print(f"actdt2 :{actdt2}")
print(type(actdt2))

print("-" * 60)
print("Difference in no of days :", dateutils.days(actdt1, actdt2))

print("-" * 60)
print("Difference in no of weeks :", dateutils.weeks(actdt1, actdt2))

print("-" * 60)
print("Difference in no of months :", dateutils.months(actdt1, actdt2))
