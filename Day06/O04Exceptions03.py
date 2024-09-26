
class TooTiny(Exception):
    pass

class TooYoug(Exception):
    pass

class TooOld(Exception):
    pass

age = 25

try:
    if age <= 5:
        raise TooTiny("This person is too very tiny")
    if age < 18:
        raise TooYoug("This person is too young to vote")
    if age > 100:
        raise TooOld("This person is too old to cast the vote")
    else:
        print("You can cast your valuabe vote.....")
except TooTiny as t:
    print("Exception occured....")
    print(t)
except TooYoug as y:
    print("Exception occured....")
    print(y)
except TooOld as o:
    print("Exception occured....")
    print(o)
