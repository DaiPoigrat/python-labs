n, m, k = [int(value) for value in input().split(' ')]

input_str = input()
input_array = [int(number) for number in input_str.split(' ') if number != ' ' and number.endswith(str(k))]

result = 0

for number in input_array:
    if number % m != 0:
        result += number

print(result)
