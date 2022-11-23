
fruits = [
    ('apple', 285),
    ('orange', 65),
    ('grapes', 145),
    ('pineapple', 85),
    ('gauva', 110),
    ('watermelon', 65),
    ('banana', 70),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-" * 40)

prices = ['fruit' for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit for fruit in fruits]
print(prices)
print("-" * 40)

prices = [fruit[0] for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] for fruit in fruits]
print(prices)

print("-" * 40)

prices = [fruit[1] * 0.9 for fruit in fruits]
print(prices)

print("-" * 40)
prices = [fruit[1] * 0.75 for fruit in fruits]
print(prices)

print("-" * 40)
expnsProd = [(fruit[0], fruit[1]) for fruit in fruits if fruit[1] >= 100]
print(f"Expensive Froots :{expnsProd}")

print("-" * 40)
expnsProd = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits]
print(expnsProd)

print("-" * 40)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = [word for word in sentence.split()]
print(words)

print("-" * 40)

words = [word for word in sentence.split() if word != 'the']
print(words)

print("-" * 40)
squares = [x ** 2 for x in range(1, 11)]
print(squares)

print("-" * 40)
res = [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)]
print(res)
