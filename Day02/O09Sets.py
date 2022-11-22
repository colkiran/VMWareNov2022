
# sets
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 5, 'six', 'seven', 'eight', 'nine', True, False, 11.2, 12.5, 13.8, 14+2j, 15-1j}

print(f"s2 :{s2}")

print("-" * 40)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s1 = {1, 2, 3}
# add - add, update
s1.add(1)
s1.add(4)
s1.add(2)
s1.add(5)
s1.add(6)

print(f"s1 :{s1}")

s1.update([1, 2, 3])
s1.update([5, 6, 7])
s1.update([3, 4, 5])
s1.update([8, 9, 10])

print(f"s1 :{s1}")

# del values = pop, remove, discard

res = s1.pop()
print(f"res :{res}")

res = s1.pop()
print(f"res :{res}")

print(f"s1 :{s1}")

s1.remove(8)
s1.remove(4)

print(f"s1 :{s1}")

s1.discard(10)
s1.discard(7)
s1.discard(1)
print(f"s1 :{s1}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print("-" * 40)

print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 40)

print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print("-" * 40)

print(f"A symmetric differenc B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 40)
x = frozenset({1, 2, 3, 4, 5})
print(f"x :{x}")
print(type(x))


# sets are mutable
# frozensets are immutable
