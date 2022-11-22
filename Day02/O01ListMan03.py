
print("clear".center(40,"-"))
l1 = list(range(1, 11))
print(f"l1 :{l1}")

l1.clear()
print(f"l1 :{l1}")

print("-" * 40)
l1 = [1, 2, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 1, 2, 2, 2]

print(f"l1 :{l1}")

# count
print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"4 :{l1.count(4)}")

# index
print("index of 3:", l1.index(3))
print("index of 3:", l1.index(3, l1.index(3)+ 1))
print("index of 3:", l1.index(3, l1.index(3, l1.index(3)+ 1) + 1))

print("-" * 40)
l1 = list(range(1, 6))
print(f"l1 before :{l1}")
l2 = l1                 # shallow copy - copies the data with address
print(f"l2 before :{l2}")

print("-" * 40)
l2.extend([6, 7, 8, 9])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("-" * 40)
l3 = [6, 7, 8, 9, 10]
print(f"l3 before :{l3}")
l4 = l3.copy()                      # deepcopy
print(f"l4 before :{l4}")

print("-" * 40)
l4.append(11)
l4.append(12)
l4.append(13)

print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("-" * 40)

l5 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"l5 before :{l5}")
l6 = l5.copy()
print(f"l6 before :{l6}")

print("-" * 40)
l6[4].append(66)
l6[4].append(77)
l6[4].append(88)

print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("-" * 40)
l7 = [1, 2, 3, 4, 5, [10, 20, 30, 40, 50]]
print(f"l7 before :{l7}")
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

print("-" * 40)
l8[5].extend([60, 70, 80])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")
