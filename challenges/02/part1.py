
from aocutils import utils

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

cube_amounts = {
    'red': 12,
    'green': 13,
    'blue': 14
}

all_games = set(range(len(games) + 1))
all_games.discard(0)
impossible_games = set()

for game_nr, game in enumerate(games):
    for draw in game:
        for cubes in draw:
            colour, count = cubes
            if count > cube_amounts[colour]:
                impossible_games.add(game_nr + 1)


possible_games = all_games - impossible_games

print(sum(possible_games))

