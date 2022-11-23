
"""
self will have the name of the object that calls the method

"""
class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name :{self.name}")
        print(f"Age  :{self.age}")


ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 40)

ply2 = Player("Rahul", 30)
ply2.get_details()

print("-" * 40)
print(f"ply1 :{ply1.__dict__}")
print(f"ply2 :{ply2.__dict__}")

print("-" * 40)
ply2.runs = 150

print(f"ply2 :{ply2.__dict__}")
print(f"ply1 :{ply1.__dict__}")