
fruits = [
    ('apple', 15),
    ('orange', 12),
    ('grapes', 10),
    ('pineapple', 7),
    ('watermelon', 8),
    ('gauva', 11),
    ('banana', 3.5),
    ('strawberry', 13.5)
]

print(f"fruits :{fruits}")
print("-" * 60)

prices = ["fruits" for friut in fruits]
print(prices)
print("-" * 60)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[0] for fruit in fruits]
print(f"prices : {prices}")
print("-" * 60)

prices = [fruit[1] for fruit in fruits]
print(f"prices : {prices}")
print("-" * 60)

prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")
print("-" * 60)

expensive_fruits = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75] for fruit in fruits if fruit[1] >= 10]
print(expensive_fruits)

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 60)
words = [word for word in sentence.split()]
print(words)

print("-" * 60)
words = [word for word in sentence.split() if word != 'the']
print(words)
