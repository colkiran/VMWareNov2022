
def addMe(x, y):
    return x + y

a = addMe
print(a(10, 20))

print("-" * 40)

b = lambda x, y: x + y
print(b(85, 65))

# lambdas are best used with :map, reduce and filter
# map =>
# filter =>
# reduce => functools

print("-" * 40)
l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

from calendar import month_name

months = ['dec', 'jul', 'aug', 'nov', 'jan', 'apr', 'oct', 'mar', 'may', 'jun', 'sep', 'feb']
print(f"Months :{months}")

res_asc = sorted(months, key=list(map(lambda mth: mth[0:3].lower(), list(month_name))).index)

print(f"Ascen :{res_asc}")




