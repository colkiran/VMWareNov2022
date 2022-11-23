
from multidispatch import dispatch

class Emp:

    def __init__(self, sal):
        self.sal = sal

    @dispatch(int, int)
    def __add__(self, other):
        return self.sal + other.sal

    @dispatch(int, int, int)
    def __add__(self, other, other1):
        return self.sal + other.sal + other1.sal

emp1 = Emp(100)
emp2 = Emp(200)
emp3 = Emp(300)

print(emp1 + emp2)
print(emp1 + emp2 + emp3)