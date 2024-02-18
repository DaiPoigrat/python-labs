n = int(input())

input_array = [int(number) for number in input().split(' ') if len(number) > 1]

result_array = []

for number in input_array:
    number_repr = str(abs(number))
    number_chars = set(number_repr)

    if len(number_repr) != len(number_chars):
        result_array.append(str(number))

print(' '.join(result_array))
