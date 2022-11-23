
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tech = ['java', 'j2ee', 'spring', 'hibernate', 'angular']

    def __gt__(self, other):
        return self.salary > other.salary

    def __str__(self):
        return f"Name  :{self.name}\nSalary  :{self.salary}"

    def __iter__(self):
        return iter(self.tech)

    def __len__(self):
        return len(self.tech)


emp1 = Employee("Mike", 20000)
print(emp1)

print("-" * 40)

print([t for t in emp1])

print("-" * 40)

print(len(emp1))
