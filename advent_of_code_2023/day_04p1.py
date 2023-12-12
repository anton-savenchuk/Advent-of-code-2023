with open("input/day_04.txt", "r", encoding="utf-8") as file:
    cards_points = []
    for row in file:
        card = row.split(":")[0]
        temp_numbers = row.split(":")[1].split("|")
        winning_numbers = [int(i) for i in temp_numbers[0].split()]
        numbers = [int(i) for i in temp_numbers[1].split()]

        points = 0
        for number in numbers:
            if number in winning_numbers:
                points = 1 if points == 0 else points * 2
        cards_points.append(points)

print(cards_points, sum(cards_points))
