n = int(input())
input_str = input()
input_array = [int(number) for number in input_str.split(' ') if number != ' ']

max_index = input_array.index(max(input_array))

input_array[max_index] *= -1

result_array = [str(number) for number in input_array]

print(' '.join(result_array))
