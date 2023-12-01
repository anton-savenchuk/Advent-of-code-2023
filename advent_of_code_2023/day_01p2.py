digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

with open("input/day_01.txt", "r", encoding="utf-8") as file:
    digits_lst = []
    digits_cnt = 0
    for row in file:
        digits_lst.append([])

        while row:
            cnt = 0
            flag = False
            if row[cnt].isdigit():
                digits_lst[digits_cnt].append(int(row[cnt]))
                row = row.strip()[1:]
                continue

            for digit in digits:
                if row.startswith(digit):
                    digits_lst[digits_cnt].append(digits[digit])
                    cnt += len(digit)
                    row = row.strip()[cnt - 1 :]
                    flag = True
                    break
            if not flag:
                row = row.strip()[1:]

        digits_cnt += 1


print(digits_lst)

digits_sum = 0
for digit in digits_lst:
    if len(digit) > 0:
        digits_sum += int(str(digit[0]) + str(digit[-1]))
        print(digit[0], digit[-1])
        continue

print(digits_sum)
