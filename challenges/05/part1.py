
from aocutils import utils

data = utils.loader("input.txt")
maps = {}
seeds = []

map_id = 0
map_name = ""
for line in data:
    if line.startswith("seeds: "):
        seeds = [int(seed) for seed in line.lstrip("seeds: ").split(" ")]
        continue

    if line == "":
        map_id += 1
        continue

    if line.endswith(" map:"):
        map_name = line.rstrip(" map:")
        maps[map_id] = {
            "name": map_name,
            "ranges": {}
        }
        continue


    dest_range_start, source_range_start, range_length = [int(number) for number in line.split(" ")]

    beginning = source_range_start
    end = source_range_start + range_length - 1
    offset = dest_range_start - source_range_start

    maps[map_id].get("ranges").update({(beginning, end): offset})

final_location_seeds = {}

for seed in seeds:

    # print(f"Seed: {seed}")

    category = seed

    for map in maps.values():
        name = map.get("name")

        # print(f"\t{category} {name} -> ", end="")

        for (beginning, end), offset in map.get("ranges").items():
            if beginning <= category <= end:
                category = category + offset
                break

        # print(f"{category}")
    final_location_seeds[category] = seed
    print(f"Final: Seed {seed} ends up in \t{category}")

print(f"First location is {min(final_location_seeds)} with Seed number {final_location_seeds[min(final_location_seeds)]}")