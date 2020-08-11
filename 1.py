import random

for i, num in enumerate(random.choices(range(1, 50), k=6), start=1):
    print("Random number {} is... {}".format(i, num))

print("The bonus ball is... {}".format(random.choice(range(1, 50))))
