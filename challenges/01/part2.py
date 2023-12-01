
from aocutils import utils

from re import finditer

data = utils.loader("input.txt")

values = []

digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

for line in data:
    original_line = line
    matches = {}
    for key in digits.keys():
        indices = [(x.start(), key) for x in list(finditer(key, line))]
        if indices:
            for index, key in indices:
                matches[index] = digits[key]

    for index, character in enumerate(line):
        if character.isnumeric():
            matches[index] = int(character)

    matches = sorted(matches.items())

    values.append(matches[0][1] * 10 + matches[-1][1])

    # print(".", end="")

print(sum(values))