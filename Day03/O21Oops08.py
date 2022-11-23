
from functools import total_ordering

@total_ordering
class Employee:
    """
    this is doc string
    """

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Name is {self.name}\nSalary is {self.salary}"

    # it works for not equal to also
    def __eq__(self, other):
        return self.salary == other.salary

    # it works for less than operator also
    def __gt__(self, other):
        return self.salary > other.salary

emp1 = Employee('Jack', 75000)
print(emp1)

print("-" * 40)
emp2 = Employee('Gibs', 65000)
print(emp2)

print("-" * 40)
if emp1 != emp2:
    print("{} salary of {} is NOT equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is equal to {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
if emp1 < emp2:
    print("{} salary of {} is Less than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))
else:
    print("{} salary of {} is greater than {} salary of {}".format(emp1.name, emp1.salary, emp2.name, emp2.salary))

print("-" * 40)
print(emp1 <= emp2)

print(Employee.__doc__)
print("-" * 40)

help(Employee)
