from math import prod

n = input()

n_symbols = [int(char) for char in n]

sum_of_symbols = sum(n_symbols)
mul_of_symbols = prod(n_symbols)

print(sum_of_symbols)
print(mul_of_symbols)
