
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)

d2 = {'name': 'Sachin', 'runs': 85, 'oppn': 'NZL', 'venue': 'Auckland'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)

d3 = dict([('name', 'Rahul'), ('runs', 125), ('oppn', 'srilanka'), ('venue', 'gale')])
print(f"d3 : {d3}")
print(type(d3))

print("-" * 40)

d4 = dict(name='Sehwag', runs=150, oppn='Pak', venue='EdenGardens')
print(f"d4 :{d4}")
print(type(d4))

print("=" * 40)
player = {'name': 'Sachin', 'runs': 85, 'oppn': 'NZL', 'venue': 'Auckland'}
print(f"player   :{player}")
print(f"Name     :{player['name']}")
print(f"Runs     :{player['runs']}")
print(f"Opponent :{player['oppn']}")
print(f"Venue    :{player['venue']}")

print("-" * 40)

for x in player:
    # print(x, end= " ")
    print(x, "=>", player[x])
print()

print("-" * 40)
# modify / update
player['year'] = 2005
player['age'] = 34
player['name'] = "Tendulkar"
player['runs'] = 89

print(f"player   :{player}")

print("-" * 40)
# del
del player['oppn']
del player['venue']
del player['runs']
print(f"player   :{player}")

print("-" * 40)
print(dir(d1))
