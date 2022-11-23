"""
1. you can modify the class attribute

"""
class Player:

    team = "India"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def get_details(self):
        print(f"Name :{self.name}")
        print(f"Age  :{self.age}")

    @classmethod
    def change_team(cls, tm):
        cls.team = tm

    @classmethod
    def CreatePlayer(cls, fn, ln, age):
        print("factory......")
        return cls(f'Mr.{fn} {ln}', age)         # calls the constructor

ply1 = Player("Virat", 35)
ply1.get_details()

print("-" * 40)
print(f"Player :{Player.team}")

Player.change_team("RCB")
print(f"Player :{Player.team}")

print("-" * 40)
print("-" * 40)

ply2 = Player.CreatePlayer('Rohit', 'Sharma', 34)
ply2.get_details()

print("-" * 40)
print(f"ply2 :{ply2.__dict__}")

