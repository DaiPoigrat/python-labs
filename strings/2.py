input_string = input()

result = 0
for char in input_string:
    if char.isdigit():
        result += int(char)

print(result)