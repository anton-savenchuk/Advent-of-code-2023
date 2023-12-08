with open("input/day_03.txt", "r", encoding="utf-8") as file:
    part_numbers = []
    matrix = [list(row.strip()) for row in file]

    len_matrix = len(matrix)
    len_temp_matrix = len_matrix + 2
    temp_matrix = [["."] * (len_temp_matrix) for _ in range(len_temp_matrix)]

    #  extended matrix
    for _row in range(len_matrix):
        for _column in range(len_matrix):
            temp_matrix[_row + 1][_column + 1] = matrix[_row][_column]

    for _row in range(1, len_matrix + 2):
        temp_num = ""
        flag = False
        for _column in range(1, len_matrix + 2):
            if temp_matrix[_row][_column].isdigit():
                temp_num += temp_matrix[_row][_column]
                for r in range(-1, 2):
                    for c in range(-1, 2):
                        if temp_matrix[_row - r][_column + c] not in ".0123456789":
                            flag = True
            elif temp_num != "" and flag:
                part_numbers.append(int(temp_num))
                temp_num = ""
                flag = False
            else:
                temp_num = ""
                flag = False

print(part_numbers, sum(part_numbers))
