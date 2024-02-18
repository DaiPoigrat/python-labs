import numpy as np

n = int(input())

input_matrix = [
    [float(number) for number in input().split(' ')]
    for _ in range(n)
]

numpy_matrix = np.array(input_matrix)
max_elements = np.linalg.inv(numpy_matrix)

for row in max_elements:
    print(' '.join([f'{numbers:.8f}' for numbers in row]))
