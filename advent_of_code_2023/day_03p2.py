with open("input/day_03.txt", "r", encoding="utf-8") as file:
    gear_numbers = []
    matrix = [list(row.strip()) for row in file]

    gear_dict = {}

    len_matrix = len(matrix)
    len_temp_matrix = len_matrix + 2
    temp_matrix = [["."] * (len_temp_matrix) for _ in range(len_temp_matrix)]

    #  extended matrix
    for _row in range(len_matrix):
        for _column in range(len_matrix):
            temp_matrix[_row + 1][_column + 1] = matrix[_row][_column]

    for _row in range(1, len_matrix + 2):
        for _column in range(1, len_matrix + 2):
            if temp_matrix[_row][_column] != "*":
                continue

            nums = set()
            for r in range(-1, 2):
                for c in range(-1, 2):
                    if temp_matrix[_row - r][_column + c].isdigit():
                        temp_num = temp_matrix[_row - r][_column + c]
                        if temp_matrix[_row - r][(_column + c) - 1].isdigit():
                            i = 1
                            while temp_matrix[_row - r][(_column + c) - i].isdigit():
                                temp_num = (
                                    temp_matrix[_row - r][(_column + c) - i] + temp_num
                                )
                                i += 1
                        if temp_matrix[_row - r][(_column + c) + 1].isdigit():
                            i = 1
                            while temp_matrix[_row - r][(_column + c) + i].isdigit():
                                temp_num += temp_matrix[_row - r][(_column + c) + i]
                                i += 1
                        nums.add(int(temp_num))

            if len(nums) == 2:
                num = 1
                for i in nums:
                    num *= i
                gear_numbers.append(num)

print(gear_numbers, sum(gear_numbers))
