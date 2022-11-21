
st = "hello world"
print(f"st :{st}")
print(type(st))                 # string

print("-" * 40)
print(f"st[0] :{st[0]}")
print(f"st[6] :{st[6]}")
print(f"st[10] :{st[10]}")

# slicing
print("-" * 40)
print(f"st[0:5] :{st[0:5]}")
print(f"st[6:11] :{st[6:11]}")
print(f"st[0:11] :{st[0:11]}")
print(f"st[0:]   :{st[0:]}")
print(f"st[:11]  :{st[:11]}")
print(f"st[:]    :{st[:]}")

print("-" * 40)
# reverse indexing
print(f"st :{st}")
print(f"st[-1] :{st[-1]}")
print(f"st[-5] :{st[-5]}")
print(f"st[-11] :{st[-11]}")

print("-" * 40)
#slicing
print(f"st[-1:-6:-1]  :{st[-1:-6:-1]}")
print(f"st[-7:-12:-1] :{st[-7:-12:-1]}")
print(f"st[-1:-12:-1] :{st[-1:-12:-1]}")
print(f"st[-1::-1]    :{st[-1::-1]}")
print(f"st[:-12:-1]   :{st[:-12:-1]}")
print(f"st[::-1]      :{st[::-1]}")

print("-" * 40)
st = "malayalam"
print(st[:] == st[::-1])

print("-" * 40)
# strings are immutable
# st = "hello world"
# print(f"st[0] :{st[0]}")
# st[0] = "H"
# print(dir(st))
st1 = "hello world"
st2 = "the quick brown fox jumps over the lazy dog"

print("find".center(40,"-"))
print(F"st1 :{st1}")

print(st1.find("l"))
print(st1.find("l", st1.find("l", st1.find("l")+1)+1))

print(f"st2 :{st2}")
print(st2.find("the"))
print(st2.find("the", st2.find("the")+1))

print("-" * 40)
print(f"st1 :{st1}")
res = st1.replace("l", "L")
print(f"res :{res}")
res = st1.replace("l", "L", 1)
print(f"res :{res}")

print("-" * 40)
print(f"st2 :{st2}")
res = st2.replace("the", "The")
print(f"res :{res}")
res = st2.replace("the", "The",1)
print(f"res :{res}")
