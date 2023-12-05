with open("input/day_02.txt", "r", encoding="utf-8") as file:
    games_lst = []

    for row in file:
        game_id, game = row.split(":")
        game_id = int(game_id.split()[-1])
        game_stat = {"red": 0, "green": 0, "blue": 0}

        for game_set in game.split("; "):
            for cube in game_set.split(","):
                num, color = cube.split()
                num = int(num)
                game_stat[color] = num if num >= game_stat[color] else game_stat[color]

        power = 1
        for i in game_stat.values():
            power *= i

        games_lst.append(power)

print(games_lst, sum(games_lst))
