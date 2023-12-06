
from aocutils import utils

data = utils.loader("input.txt")

times = -1
distances = -1
for line in data:
    if line.startswith("Time:"):
        line = line.lstrip("Time:").replace(" ","")
        times = int(line)
        continue
    if line.startswith("Distance:"):
        line = line.lstrip("Distance:").replace(" ", "")
        distances = int(line)

race = (times, distances)

def get_distance(hold_time, total_time):
    speed = hold_time
    distance = speed * (total_time - hold_time)
    return distance

winning_races = 0

time, record_distance = race
distances = []
for times in range(time):
    race_distance = get_distance(times, time)
    if race_distance > record_distance:
        winning_races += 1

print(winning_races)




print("Done")