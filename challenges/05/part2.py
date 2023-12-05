import multiprocessing

from aocutils import utils
from itertools import batched


data = utils.loader("input.txt")
maps = {}
seeds_ranges = []

map_id = 0
map_name = ""
for line in data:
    if line.startswith("seeds: "):

        seeds = [int(seed) for seed in line.lstrip("seeds: ").split(" ")]
        for beginning, offset in batched(seeds, 2):
            seeds_ranges.append((beginning, beginning + offset - 1))
        continue

    if line == "":
        map_id += 1
        continue

    if line.endswith(" map:"):
        map_name = line.rstrip(" map:")
        map_name = "-".join(reversed(map_name.split("-")))
        maps[map_id] = {
            "name": map_name,
            "ranges": {}
        }
        continue


    dest_range_start, source_range_start, range_length = [int(number) for number in line.split(" ")]

    beginning = dest_range_start
    end = dest_range_start + range_length - 1
    offset = source_range_start - dest_range_start

    maps[map_id].get("ranges").update({(beginning, end): offset})


def find_seed(start, end):
    for location in range(start, end):

        # print(f"Location: {location}")

        category = location

        for map in reversed(maps.values()):
            name = map.get("name")

            # print(f"\t{category} {name} -> ", end="")

            for (beginning, end), offset in map.get("ranges").items():
                if beginning <= category <= end:
                    category = category + offset
                    break

            # print(f"{category}")

        for beginning, end in seeds_ranges:
            if beginning <= category <= end:
                print(f"Location {location} gets seed {category}")
                end("Job Done!")

        # print(f"Final: Location {location} is seed \t{category}")


if __name__ == "__main__":

    find_seed(47_000_000, 48_000_000)
    # num_workers = multiprocessing.cpu_count()  # Get the number of CPUs
    # total_elements = 1_000_000
    # start = 47_000_000
    # chunk_size = total_elements // num_workers  # Divide the work into chunks based on the number of CPUs
    #
    # # Create a list of start and end points for the chunks
    # ranges = [(i, i + chunk_size) for i in range(start, start + total_elements, chunk_size)]
    #
    # # Create a pool of worker processes
    # with multiprocessing.Pool(processes=num_workers) as pool:
    #     # Use pool.map or pool.starmap to apply 'process_chunk' to each range
    #     pool.starmap(find_seed, ranges)