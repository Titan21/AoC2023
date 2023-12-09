
from aocutils import utils

from itertools import cycle

data = utils.loader("input.txt")

instructions = [char for char in data[0]]

start_location = "AAA"
finish_location = "ZZZ"

map = {}
for line in data[2:]:
    start, choices = line.split(" = ")

    map[start] = choices.lstrip("(").rstrip(")").split(", ")


def dirmap(choice):
    if choice == "R":
        return 1
    if choice == "L":
        return 0
    print("Uhh?")
    exit(2)

current = start_location
print(current)
steps = 0
for instruction in cycle(instructions):
    if current != finish_location:
        steps += 1
        current = map[current][dirmap(instruction)]
    else:
        break
    print(current)

print(f"Count: {steps}")