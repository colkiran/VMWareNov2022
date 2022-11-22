
# upack a list
values = list(range(10, 40, 10))
print(f"values :{values}")

a, b, c = values
print(a, b, c, sep=" : ")

print("-" * 40)

values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values
print(a, b, c, sep=", ")

print("-" * 40)

a, *b, c = values
print(a, b, c, sep=", ")

print("-" * 40)

*a, b, c = values
print(a, b, c, sep=", ")

lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst2 = [lst1]
print(f"lst2 :{lst2}")
print(len(lst2))

print("-" * 40)

lst3 = [*lst1]
print(f"lst3 :{lst3}")
print(len(lst3))

print("-" * 40)

letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 40)

for letter in letters:
    print(letter, end=' ')
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 40)
for index, letter in enumerate(letters):
    print(index, letter)

print("-" * 40)

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 40)
for lst in mylist:
    print(lst)

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(f"{ind}\t{lst}")

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")
