
from aocutils import utils
from math import pow

data = utils.loader("input_short.txt")

total_score = 0
for card in data:
    winning_numbers_str, have_numbers_str = card.split(": ")[1].split(" | ")
    winning_numbers = set(int(number) for number in winning_numbers_str.split(" ") if number.isnumeric())
    have_numbers = set(int(number) for number in have_numbers_str.split(" ") if number.isnumeric())

    successful_numbers = winning_numbers.intersection(have_numbers)

    count_successful = len(successful_numbers)
    if not count_successful:
        continue
    total_score += int(pow(2,count_successful - 1))

print(total_score)