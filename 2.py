import random

words = ["hot", "summer", "hard", "dry", "simple", "light", "weak", "male", "sad", "win", "small", "ignore", "buy", "succeed", "reject", "prevent", "exclude", "active", "above", "after"]
opposites = ["cold", "winter", "soft", "wet", "complex", "darkness", "strong", "female", "happy", "lose", "big", "pay attention", "sell", "fail", "accept", "allow", "include", "lazy", "below", "before"]

score = 0
correctAnswers = []

for i in range(10):
    exampleWord = random.choice(words)
    exampleOpposite = opposites[words.index(exampleWord)]
    words.remove(exampleWord)
    opposites.remove(exampleOpposite)

    questionWord = random.choice(words)
    questionOpposite = opposites[words.index(questionWord)]
    words.remove(questionWord)
    opposites.remove(questionOpposite)

    answer = input("{} is to {} as {} is to ______? ".format(exampleWord, exampleOpposite, questionWord)).lower()

    newCorrectAnswer = questionOpposite

    if answer == questionOpposite:
        score += 1
        newCorrectAnswer += " (you got this question correct)"

    correctAnswers.append(newCorrectAnswer)

print("\nYour final score was {}".format(score))

for i, answer in enumerate(correctAnswers):
    print("The correct answer for question {} was: {}".format(i, answer))
