
from aocutils import utils
from math import prod

data = utils.loader("input.txt")

games = []

for game_draw in data:
    game = []
    for draw in game_draw.split(":")[1].split(";"):
        draws = []
        for cubes in draw.split(","):
            count, colour = cubes.lstrip(" ").split(" ")
            draws.append((colour, int(count)))
        game.append(draws)
    games.append(game)


min_cube_amounts = {}

for game_nr, game in enumerate(games):
    current_min_cubes = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for draw in game:
        for cubes in draw:
            colour, count = cubes
            if count > current_min_cubes[colour]:
                current_min_cubes[colour] = count
    min_cube_amounts[game_nr + 1] = current_min_cubes


total = 0
for game in min_cube_amounts.values():
    total += prod(game.values())

print(total)