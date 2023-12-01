
from aocutils import utils

data = utils.loader("input.txt")

values = []
for line in data:
    numbers = [int(character) for character in line if character.isnumeric()]
    values.append(numbers[0] * 10 + numbers[-1])

print(sum(values))