
class Player:

    def __init__(self):
        self.name = "Sachin"
        self.age = 34

    def get_details(self):
        print(f"name is {self.name}.....")
        print(f"Age is {self.age}")


ply1= Player()
ply1.get_details()
print("-" * 40)

ply2 = Player()
ply2.name = "Rahul"
ply2.age = 32
ply2.get_details()

