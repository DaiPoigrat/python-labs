import numpy as np

n = int(input())

input_matrix = [
    [int(number) for number in input().split(' ')]
    for _ in range(n)
]

numpy_matrix = np.array(input_matrix)
max_elements = np.max(numpy_matrix, axis=1)
print(*max_elements)
