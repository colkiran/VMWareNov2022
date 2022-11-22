"""

1. sort     - sorts the original list
2. sorted   - takes a copy if list sorts it and then shares that copy
"""


l1 = [10 ,8, 5, 2, 4, 1, 7, 6, 9 ]
print(f"l1 :{l1}")

# sort the list
res1_asc = sorted(l1)
print(f"Sorted Ascending ;{res1_asc}")

res1_desc = sorted(l1, reverse=True)
print(f"Sorted Ascending ;{res1_desc}")

print("-" * 40)

l1.sort()
print(f"l1 :{l1}")

print("-" * 40)

l1 = [10, 'zebra', 'apple', 8, 'yellow', 'blue', 5, 'pink', 'white', 2, 'green', 'maroon', 4, 'hen', 'dog', 1, 'fish', 'cow',7, 'king', 'queen', 6, 'jack', 'red', 9, 1024, 19, 167, 28, 231, 2154]
print(f"l1 :{l1}")

res1_asc = sorted(l1, key=ascii)
print(f"Ascending :{res1_asc}")

print("-" * 40)

cities = ['thiruvananthapuram', 'bangalore', 'chennai', 'pune', 'delhi', 'vishakapatnam', 'kanyakumari', 'ooty', 'hyderabad', 'mysore', 'mumbai']

months = ['dec', 'jul', 'aug', 'nov', 'jan', 'apr', 'oct', 'mar', 'may', 'jun', 'sep', 'feb']

print("-" * 40)

print(f"cities :{cities}")

print("-" * 40)

res_asc = sorted(cities, key=len)
print(f"Ascending :{res_asc}")

print("-" * 40)

from calendar import month_name

print(list(month_name))

print("-" * 40)

print(f"months :{months}")
from calendar import month_name

months = ['dec', 'jul', 'aug', 'nov', 'jan', 'apr', 'oct', 'mar', 'may', 'jun', 'sep', 'feb']
sortedMonth = []

print("-" * 40)

from calendar import month_name
month_names_list = [m[:3].lower() for m in list(month_name)]

def get_month_num(mon):
    return month_names_list.index(mon)

res_asc = sorted(months, key=get_month_num)
print(f"Ascending :{res_asc}")

print("-" * 40)

l1 = [10 ,8, 5, 2, 4, 1, 7, 6, 9 ]
print(f"l1 :{l1}")

res = list(reversed(l1))
print(f"res :{res}")
