
# filter
l = list(range(1, 26))
print(F"l :{l}")

res = list(filter(lambda x : x % 3 == 0, l))
print(f"res :{res}")

sentence = "the quick brown fox jumps over the lazy dog"
res = list(filter(lambda x: x != 'the', sentence.split()))
print(f"res :{res}")

from functools import reduce
l = [8, 3, 6, 5, 1, 9, 7, 10, 4, 2]
print(f"l :{l}")

res = reduce(lambda x, y : x if x < y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")
