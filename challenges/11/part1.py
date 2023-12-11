
from aocutils import utils
from itertools import combinations

data = utils.loader("input.txt")

row_stretched_data = []
for row in data:
    if all(char == "." for char in row):
        row_stretched_data.append(row)
    row_stretched_data.append(row)

column_stretched_data = [[] for _ in row_stretched_data]
for y in range(len(row_stretched_data[0])):
    stretch = False
    if all(char == "." for char in [column[y] for column in row_stretched_data]):
        stretch = True

    for x, row in enumerate(row_stretched_data):
        column_stretched_data[x].extend(row[y])
        if stretch:
            column_stretched_data[x].extend(row[y])


counter = 0
star_locations = {}
enumerated_data = [[] for _ in row_stretched_data]
for x, row in enumerate(column_stretched_data):
    for y, char in enumerate(row):
        if char == "#":
            enumerated_data[x].extend(str(counter := counter + 1))
            star_locations[counter] = (x,y)
        else:
            enumerated_data[x].extend(char)

star_distances = {}
for start, end in combinations(star_locations.keys(),2):
    star_distances[(start, end)] = utils.manhattan_distance(star_locations[start], star_locations[end])

print(sum(star_distances.values()))
print("Done")
