
from aocutils import utils
from cProfile import Profile
from pstats import SortKey, Stats
from itertools import cycle
from concurrent.futures import ThreadPoolExecutor

data = utils.loader("input_part2.txt")

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

current = starts.copy()
print(current)
steps = 0

with Profile() as profile:
    try:
        for instruction in cycle(instructions):
            # print(instruction)
            done = True
            for i, location in enumerate(current):
                with ThreadPoolExecutor(max_workers=len(current)) as executor:
                    futures = {executor.submit(lambda i, location: map[location][instruction], i, location)
                               for i, location in enumerate(current)}

                    for future in futures:
                        result = future.result()
                        current[i] = result
                        if result[2] != "Z":
                            done = False

            steps += 1
            if done:
                break
    finally:
        Stats(profile).strip_dirs().sort_stats(SortKey.CALLS).print_stats()

print(f"Count: {steps}")