
# Magic Method
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor......")

    def __str__(self):              # dunder str
        return f"Name :{self.name}\nAge :{self.age}"

ply1 = Player("Sachin", 30)
# ply1.get_details()

print("-" * 40)
print(str(ply1))

print("-" * 40)
print(ply1)                # implicitly call __str__()