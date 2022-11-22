
from collections import namedtuple

nmdTpl = namedtuple('Employee', "empname age desig salary")
emp = nmdTpl(empname="Mike Tyson", age=54, desig='Ironman', salary=78000)

print(emp)
print("-" * 40)

print(f"Name        :{emp.empname}")
print(f"Age         :{emp.age}")
print(f"Designation :{emp.desig}")
print(f"Salary      :{emp.salary}")

# emp.empname = "Roger Fedrer"
