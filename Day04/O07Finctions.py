
def greet():
    print("Greetings Mr.Micheal, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event......")

# City is called default argument and gname is called as non default arg
def greetGstCty(gname, city = "Los Angels"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event......")


greet()
print("-" * 60)

greetGst("Huges")
greetGst("Micheal")

print("-" * 60)
greetGstCty("Micheal")
greetGstCty("Huges")
greetGstCty("Keneth", "Newyork")