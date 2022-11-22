
# fromkeys -> keys + values

emp = {
    'emp1': {'empid': 'EMP001', 'empname': 'Jack', 'age': 34, 'desig': 'MGR', 'dept': 'Finance', 'location': 'Bangalore'},

    'emp2': {'empid': 'EMP002', 'empname': 'Jill', 'age': 31, 'desig': 'BDM', 'dept': 'Marketting', 'location': 'Hyderabad'},

    'emp3': {'empid': 'EMP003', 'empname': 'Roger', 'age': 30, 'desig': 'Analyst', 'dept': 'IT', 'location': 'Chennai'}
}

print(f"emp :{emp}")

print("=" * 40)

print(f"emp1 :{emp['emp1']}")

print("=" * 40)

print(f"emp2 :{emp['emp2']}")

print("=" * 40)

print(f"emp :{emp['emp3']}")

print("=" * 40)

for ky, info in emp.items():
    print(ky)
    print("-" * len(ky))
    for k, v in info.items():
        print(k, " => ", v)
    print("-" * 40)

print("update".center(40, "-"))

emp1 = {'empid': 'EMP001', 'empname': 'Jack', 'age': 34, 'desig': 'MGR',  'location': 'Bangalore'}

emp2 = {'empid': 'EMP002', 'empname': 'Jill', 'age': 31, 'desig': 'BDM', 'dept': 'Marketting'}

emp1.update(emp2)
print(f"emp1 after :{emp1}")
print(f"emp2 after :{emp2}")

print("clear".center(40, "-"))
emp1 = {'empid': 'EMP001', 'empname': 'Jack', 'age': 34, 'desig': 'MGR',  'location': 'Bangalore'}
print(f"emp1 before :{emp1}")
emp1.clear()
print(f"emp1 after :{emp1}")

print("copy".center(40, "-"))
d1 = {'plyname': 'Sachin', 'runs': 79, 'oppn': 'aus', 'venue': 'perth'}
print(f"d1 before :{d1}")
d2 = d1
print(f"d2 before :{d2}")

print("-" * 40)

d2['age'] = 30
d2['year'] = 1999
print(f"d2 after :{d2}")
print(f"d1 after :{d1}")

print("=" * 40)
d3 = {'plyname': 'Sachin', 'runs': 79, 'oppn': 'aus', 'venue': 'perth'}
print(f"d3 before :{d3}")
d4 = d3.copy()
print(f"d4 before :{d4}")

print("-" * 40)
d4['age'] = 32
d4['year'] = 2003
print(f"d4 after {d4}")
print(f"d3 after {d3}")

print("-" * 40)

d5 = {'plyname': 'Sachin', 'runs': {'perth': 79, 'gabba': 105, 'melbourne': 45}, 'oppn': 'aus'}
print(f"d5 before :{d5}")
d6 = d5.copy()
print(f"d6 before :{d6}")

print("-" * 40)
d6['runs']['scg'] = 135
d6['runs']['adelaide'] = 98
print(f"d6 after :{d6}")
print(f"d5 after :{d5}")

print("-" * 40)
d7 = {'plyname': 'Sachin', 'runs': {'perth': 79, 'gabba': 105, 'melbourne': 45}, 'oppn': 'aus'}
print(f"d7 before :{d7}")
from copy import deepcopy
d8 = deepcopy(d7)
print(f"d8 before :{d8}")

print("-" * 40)
d8['runs']['scg'] = 135
d8['runs']['adelaide'] = 98
print(f"d8 after :{d8}")
print(f"d7 after :{d7}")

