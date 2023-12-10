
from aocutils import utils
from itertools import pairwise


data = utils.loader("input.txt")

readings = []

for line in data:
    readings.append([int(x) for x in line.split()])


def get_offset(values):
    return [b-a for a, b in pairwise(values)]

new_values = []
for reading in readings:

    offsets = []
    offsets.append(reading)
    while not all(x == 0 for x in offsets[-1]):
        offsets.append(get_offset(offsets[-1]))

    new_offsets = []
    for i, offset in enumerate(reversed(offsets)):
        original_index = len(offsets) - 1 - i
        new_offsets.append(offsets[original_index])
        if i == 0:
            new_offsets[i].append(0)
            continue

        new_offsets[i].append(offsets[original_index + 1][-1] + new_offsets[i][-1])

    new_values.append(new_offsets[-1][-1])

    # print("Calculated all offsets")

print(sum(new_values))
# print("Done")