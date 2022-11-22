
player = {'name': 'Sachin', 'age': 32, 'runs': 98, 'oppn': 'Pak', 'venue': 'sharjah'}
print(f"player :{player}")

print("-" * 40)
print(player.get('name',"Invalid Key Please enter a valid key...."))
print(player.get('year', "Invalid Key Please enter a valid key...."))

print("-" * 40)
# setdefault
player = {'name': 'Sachin', 'runs': 98, 'oppn': 'Pak', 'venue': 'sharjah'}
print(f"player :{player}")

print("-" * 40)
player.setdefault('runs', 150)
player.setdefault('venue', 'Mohali')
player.setdefault('age', 27)
player.setdefault('year', 1997)

print(f"player :{player}")

print("=" * 40)

cities = ['blr', 'che', 'mum', 'del', 'kol', 'hyd', 'pun']
print(f"cities :{cities}")

# convert the cities into a dictionary keys

temp = dict.fromkeys(cities)
print(f"temp :{temp}")

temp = dict.fromkeys(cities, 22)
print(f"temp :{temp}")

print("-" * 40)
# keys
player = {'name': 'Sachin', 'age': 32, 'runs': 98, 'oppn': 'Pak', 'venue': 'sharjah'}
print(f"player :{player}")

k = player.keys()
print(f"k :{k}")

print("-" * 40)

for k in player:
    print(k + " => " + str(player[k]))

print("{:-^40}".format("values"))

player = {'name': 'Sachin', 'age': 32, 'runs': 98, 'oppn': 'Pak', 'venue': 'sharjah'}
print(f"player :{player}")

print("-" * 40)
vls = player.values()
print(F"values :{vls}")

print("pop".center(40, "-"))

player = {'name': 'Sachin', 'age': 32, 'runs': 98, 'oppn': 'Pak', 'venue': 'sharjah'}
print(f"player :{player}")

print("-" * 40)

res = player.pop('runs')
print(f"res :{res}")

res = player.pop('age')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(40, "-"))

player = {'name': 'Sachin', 'age': 32, 'runs': 98, 'oppn': 'Pak', 'venue': 'sharjah'}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")
