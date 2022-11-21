
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 6.3, 7.8, 9j, 10-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
# read list
l1 = [1, 2, 3, 4, 'five', 'six', 'seven', 8+1j, 9-0j, True, False]
print(f"l1 :{l1}")
print(f"l1[5] :{l1[5]}")
print(f"l1[10] :{l1[10]}")

for i in l1:
    print(i, end=" ")
print()

print("-" * 40)
# memory allocation is not contigious
print(f"id(l1[0]) :{id(l1[0])}")
print(f"id(l1[1]) :{id(l1[1])}")
print(f"id(l1[2]) :{id(l1[2])}")
print(f"id(l1[3]) :{id(l1[3])}")
print(f"id(l1[4]) :{id(l1[4])}")

print("-" * 40)
# update the list
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

# to insert a number between 3 and 4
l1[3] = 100
print(f"l1 :{l1}")

# l1[5] = 500
# print(f"l1 :{l1}")

print("-" * 40)
# delete elements from a list
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

del l1[1]
del l1[3]

print(f"l1 :{l1}")

print("-" * 40)
print(dir(l1))
