
t1 = tuple()
print(f"t1 :{t1}")
print(type(t1))

print("-" * 40)

t2 = (1, 2, 3, 4, 5)
print(f"t2 :{t2}")
print(type(t2))

print("-" * 40)

t3 = tuple(range(2, 11, 2))
print(f"t3 :{t3}")
print(type(t3))

print("-" * 40)
t4 = 1,
print(f't4 :{t4}')
print(type(t4))

print("-" * 40)
t5 = 1, 2, 3, 4, 5
print(f"t5 :{t5}")
print(type(t5))

print("-" * 40)
t1 = tuple(range(1, 11))
print(f"t1 :{t1}")

# print(f"t1[4] :{t1[4]}")
# t1[4] = 500

print("-" * 40)
# print(dir(t1))

t1 = (1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1,1, 1, 1, 2,2 ,2 ,2 ,2, 1, 2, 3)

print("count".center(40, "-"))
print(f"t1 :{t1}")

print(f"1 :{t1.count(1)}")
print(f"2 :{t1.count(2)}")
print(f"3 :{t1.count(3)}")

print("index".center(40,"-"))
t1 = (1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2, 2, 2, 1, 2, 3, 1, 1,1, 1, 1, 2,2 ,2 ,2 ,2, 1, 2, 3)

res = t1.index(3)
print(f"res :{res}")

res = t1.index(3, t1.index(3) + 1)
print(f"res :{res}")

res = t1.index(3, t1.index(3, t1.index(3) + 1) + 1)
print(f"res :{res}")

