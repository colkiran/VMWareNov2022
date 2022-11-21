
for i in range(1, 11):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 15):
    # if i > 10:
    #     break               # stop or exit iteration
    if i % 2 == 1:
        continue            # skip the iteration
    print(i, end=" ")
else:
    print("\nCompleted iterating.......")

print("-" * 40)

for i in range(10, 0, -1):
    print(i, end=" ")
print()