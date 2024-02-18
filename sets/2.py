input_str = input()
result = 'YES' if len(list(set(input_str))) < len(input_str) else 'NO'
print(result)
