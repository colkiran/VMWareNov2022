
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __str__(self):
        return f"Name  :{self.name}\nSalary  :{self.salary}"

    def __add__(self, other):
        return self.salary + other.salary

    def __sub__(self, other):
        return self.salary - other.salary

    def __mul__(self, other):
        return self.salary * other.salary

    def __floordiv__(self, other):
        return self.salary // other.salary

    def __truediv__(self, other):
        return self.salary / other.salary


emp1 = Employee("Steve", 15000)
print(emp1)

print("-" * 40)

emp2 = Employee("John", 6000)
print(emp2)

print("-" * 40)

emp3 = Employee("Tina", 8000)

print("-" * 40)

print(f"Add :{emp1 + emp2}")
print(f"Subtract :{emp1 - emp2}")
print(f"Mulitply :{emp1 * emp2}")
print(f"Divide :{emp1 / emp2}")
print(f"Floor Div :{emp1 // emp2}")

