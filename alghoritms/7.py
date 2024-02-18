input_str = input().split(' ')

a = int(input_str[0])
b = int(input_str[1])

chapter_one = False
chapter_two = False

count_days = 1

result1 = 0
result2 = 0

while True:
    if a >= b and not chapter_one:
        result1 = count_days
        chapter_one = True

    if a >= 1_000_000 and not chapter_two:
        result2 = count_days
        chapter_two = True

    if chapter_one and chapter_two:
        break

    count_days += 1
    a *= 3

print(result1, result2)
