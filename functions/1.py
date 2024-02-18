def is_power(number):
    if number == 1:
        return True
    while number % 5 == 0 and number > 1:
        number /= 5
    return number == 1


n = int(input())

input_array = [int(number) for number in input().split(' ')]

result = 0
for number in input_array:
    if is_power(number):
        result += 1

print(result)
