import random
import re


class Word:
    def __init__(self, key, synonyms, antonyms):
        self.key = key
        self.synonyms = synonyms
        self.antonyms = antonyms


print("Processing file...")

with open("file.txt", "r") as file:
    text = file.read()

text = text.replace("_", " ")
text = text.replace(".", "")
text = re.sub(r"(, )?{[^\n,]*}", "", text)  # remove words in {}
text = re.sub(r"(, )?\[[^\n,]*\]", "", text)  # remove words in []
text = re.sub(r" \\\w+\\", "", text)  # remove verb/noun identifies e.g. \v.\ (the dot is removed already by code above)

lines = text.split("\n\n")

# split list on "="
wordsAsStrings = []
currentWord = []
for line in lines:
    if line == "=":
        wordsAsStrings.append(currentWord)
        currentWord = []
    else:
        currentWord.append(line)

# parse the strings into Word objects
words = []
for wordAsString in wordsAsStrings:
    ke = None
    syn = []
    ant = []

    for wordLine in wordAsString:
        if wordLine.startswith("KEY"):
            ke = wordLine[5:].lower()
        elif wordLine.startswith("SYN"):
            syn = wordLine[5:].lower().split(", ")
        elif wordLine.startswith("ANT"):
            ant = wordLine[5:].lower().split(", ")

    if not ant or ke is None or ke == "":
        continue

    words.append(Word(ke, syn, ant))


# print(["({})({})({})".format(word.key, word.synonyms, word.antonyms) for word in words])

print("Done!\n")


# --- THE GAME ---

score = 0
correctAnswers = []

for i in range(10):
    example = random.choice(words)
    words.remove(example)

    question = random.choice(words)
    words.remove(question)

    answer = input("Q{}: {} is to {} as {} is to ______? ".format(i+1, example.key, random.choice(example.antonyms), question.key)).lower()

    if answer in question.antonyms:
        score += 1
        correctAnswers.append("[you got this question correct]")
    else:
        correctAnswers.append(question.antonyms[0])

print("\nYour final score was {}\n".format(score))

for i, answer in enumerate(correctAnswers):
    print("The correct answer for question {} was: {}".format(i+1, answer))
