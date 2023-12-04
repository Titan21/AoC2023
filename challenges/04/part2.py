
from aocutils import utils
from math import pow

data = utils.loader("input_short.txt")

card_counts = {x: 1 for x in range(1, len(data) + 1)}
for card in data:
    card_id_str, card_data = card.split(": ")
    card_id = int(card_id_str.split(" ")[-1])
    winning_numbers_str, have_numbers_str = card_data.split(" | ")
    winning_numbers = set(int(number) for number in winning_numbers_str.split(" ") if number.isnumeric())
    have_numbers = set(int(number) for number in have_numbers_str.split(" ") if number.isnumeric())

    successful_numbers = winning_numbers.intersection(have_numbers)

    count_successful = len(successful_numbers)
    if count_successful:
        won_cards = list(range(card_id + 1, card_id + 1 + count_successful))
        for winning_card in won_cards:
            card_counts[winning_card] += 1 * card_counts[card_id]

print(sum(card_counts.values()))
