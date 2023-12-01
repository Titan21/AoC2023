
from aocutils import utils

data = utils.loader("input.txt")

values = []

digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

# Parsing string left to right, ensuring no string-overlap (incorrect)
# https://www.reddit.com/r/adventofcode/comments/1884fpl/2023_day_1for_those_who_stuck_on_part_2/
for line in data:
    original_line = line
    matches = {}
    for key in digits.keys():
        index = line.find(key)
        if index >= 0:
            matches[index] = key

    matches = sorted(matches.items())

    for _, key in matches:
        line = line.replace(key, digits[key])
    numbers = [int(character) for character in line if character.isnumeric()]
    values.append(numbers[0] * 10 + numbers[-1])

    # print(".", end="")

print(sum(values))