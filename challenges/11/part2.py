
from aocutils import utils
from itertools import combinations

data = utils.loader("input.txt")




counter = 1
star_locations = {}
for x, row in enumerate(data):
    for y, char in enumerate(row):
        if char == "#":
            star_locations[counter] = (x,y)
            counter += 1

total_rows = set(range(len(data)))
total_columns = set(range(len(data[0])))

used_rows = set(location[0] for location in star_locations.values())
used_columns = set(location[1] for location in star_locations.values())

empty_rows = total_rows.difference(used_rows)
empty_columns = total_columns.difference(used_columns)

expansion_distance = 1_000_000

for star, location in star_locations.items():
    expanded_rows = sum(row <= location[0] for row in empty_rows)
    expanded_columns = sum(column <= location[1] for column in empty_columns)
    star_locations[star] = (
            location[0] + ((expansion_distance - 1) * expanded_rows),
            location[1] + ((expansion_distance - 1)* expanded_columns)
    )
    # print("star")

star_distances = {}
for start, end in combinations(star_locations.keys(),2):
    star_distances[(start, end)] = utils.manhattan_distance(star_locations[start], star_locations[end])

print(sum(star_distances.values()))
print("Done")