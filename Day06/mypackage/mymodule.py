
gname = "Micheal Jordan"

sports = ['baseball', 'soccer', 'tennis', 'basketball', 'swimming']

goals = {1993: 128, 1994: 180, 1995: 168, 1996: 225}

def greet(gst):
    print(f"Greetings Mr.{gst}, Welcome to the event.....")


class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

# print(__name__)

if __name__ == '__main__':
    greet("Shaquille")
    print("-" * 60)

    ply1 = Player("Messi", 37)
    ply1.get_details()
