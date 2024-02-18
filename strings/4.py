input_string = input()
split_str = input_string.split(' ')
result_string = ' '.join([word for word in split_str if word != ''])

print(result_string)
