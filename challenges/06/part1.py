
from aocutils import utils

data = utils.loader("input.txt")

times = []
distances = []
for line in data:
    if line.startswith("Time:"):
        line = line.lstrip("Time:")
        times = [int(time) for time in line.split(" ") if time.isnumeric()]
        continue
    if line.startswith("Distance:"):
        line = line.lstrip("Distance:")
        distances = [int(distance) for distance in line.split(" ") if distance.isnumeric()]

races = list(zip(times, distances))

def get_distance(hold_time, total_time):
    speed = hold_time
    distance = speed * (total_time - hold_time)
    return distance

winning_races = 1

for race in races:
    time, record_distance = race
    distances = []
    for times in range(time):
        distances.append(get_distance(times, time))

    winning_races *= sum(distance > record_distance for distance in distances)

print(winning_races)




print("Done")