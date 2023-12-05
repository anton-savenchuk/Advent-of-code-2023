with open("input/day_02.txt", "r", encoding="utf-8") as file:
    games_lst = []

    for row in file:
        game_id, game = row.split(":")
        game_id = int(game_id.split()[-1])
        flag = False

        for game_set in game.split("; "):
            _set = {"red": 0, "green": 0, "blue": 0}
            for cube in game_set.split(","):
                num, color = cube.split()
                _set[color] += int(num)

            if _set["red"] <= 12 and _set["green"] <= 13 and _set["blue"] <= 14:
                flag = True
            else:
                flag = False
                break

        if flag:
            games_lst.append(game_id)

print(games_lst, sum(games_lst))
