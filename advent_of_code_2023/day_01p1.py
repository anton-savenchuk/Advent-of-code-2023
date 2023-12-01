with open("input/day_01.txt", "r", encoding="utf-8") as file:
    digits_lst = []
    digits_cnt = 0
    for row in file:
        digits_lst.append([])

        for i in row.strip():
            if i.isdigit():
                digits_lst[digits_cnt].append(int(i))
                continue

        digits_cnt += 1


print(digits_lst)

digits_sum = 0
for digit in digits_lst:
    if len(digit) > 0:
        digits_sum += int(str(digit[0]) + str(digit[-1]))
        print(digit[0], digit[-1])
        continue

print(digits_sum)
