import random

randomNumbers = random.choices(range(1, 50), k=7)

while True:
    userStrings = input("Please enter 7 positive integers separated by single spaces: ").split(sep=" ")

    allInts = True
    for userString in userStrings:
        if not userString.isdigit():
            allInts = False

    if len(userStrings) != 7 or not allInts:
        print("Please ensure all your 7 positive numbers are integers and are each separated by a single space.")
    else:
        break


userNumbers = map(lambda x: str(x), userStrings)

for i, (user, cpu) in enumerate(zip(userNumbers, randomNumbers)):
    if user == cpu:
        print("Number {} was correct!".format(i))
    else:
        print("Number {} was incorrect.".format(i))

print("The probability of correctly guessing all of my random numbers was 1 in {}".format(49 ** 7))
