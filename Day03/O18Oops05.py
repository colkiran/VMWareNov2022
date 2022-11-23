# class Attribute - can be accessed only with class name

class Player:

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name :{self.name}")
        print(f"Age  :{self.age}")

ply1 = Player('Virat', 35)
ply1.get_details()

print("-" * 40)

ply2 = Player("Rohit", 34)
ply2.get_details()

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1   :{ply1.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
ply1.team = "RCB"
print(f"ply1 :{ply1.team}")
print(f"Player :{Player.team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
print(f"ply1 :{ply1.__dict__}")