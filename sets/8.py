input_str = input()

counter_input_str = {}

for char in input_str:
    if char not in counter_input_str:
        counter_input_str[char] = 1
    else:
        counter_input_str[char] += 1

result_char_list = sorted([char for char in list(set(input_str)) if counter_input_str[char] == 1])

print(''.join(result_char_list))
