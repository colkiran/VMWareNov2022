
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

    def append(self, val):
        self.tech.append(val)

    def __getitem__(self, idx):
        return self.tech[idx]

    def __setitem__(self, idx, val):
        self.tech[idx] = val


emp1 = Employee('Joe', 35000)
print(emp1)

print("-" * 40)

print([e for e in emp1])

print("-" * 40)

emp1.append("Python")

print("-" * 40)

print([e for e in emp1])

print("-" * 40)

x = emp1[1]
print(f"x :{x}")

print("-" * 40)

emp1[1] = "JSP"

print("-" * 40)
print([e for e in emp1])
