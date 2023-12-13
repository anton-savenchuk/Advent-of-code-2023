with open("input/day_04.txt", "r", encoding="utf-8") as file:
    rows = file.readlines()
    cards = [1] * len(rows)

    for game_id, row in enumerate(rows):
        temp_numbers = row.split(":")[1].split("|")
        winning_numbers = {int(i) for i in temp_numbers[0].split()}
        having_numbers = {int(i) for i in temp_numbers[1].split()}

        for i in range(1, len(having_numbers & winning_numbers) + 1):
            cards[game_id + i] += cards[game_id]

print(sorted(cards), sum(cards))
