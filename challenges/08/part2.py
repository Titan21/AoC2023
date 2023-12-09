
from aocutils import utils
from cProfile import Profile
from pstats import SortKey, Stats
from itertools import cycle
from math import lcm

data = utils.loader("input.txt")

instructions = [0 if char == "L" else 1 for char in data[0]]

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

starts = [x for x in map.keys() if x.endswith("A")]
total_steps = [] * len(starts)

current = starts.copy()
print(current)

with Profile() as profile:
    try:
        for start in starts:
            current = start
            steps = 0
            done = False
            while not done:
                for instruction in cycle(instructions):
                    current = map[current][instruction]
                    steps += 1
                    if current[2] == "Z":
                        done = True
                        break
                    # print(f"\t{steps}\t{current}")

            total_steps.append(steps)
    finally:
        Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()

print(f"Total: {lcm(*total_steps)}")