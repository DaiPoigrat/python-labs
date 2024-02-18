import numpy as np

n = int(input())

input_matrix = [
    [float(number) for number in input().split(' ')]
    for _ in range(n)
]

numpy_matrix = np.array(input_matrix)
max_elements = np.linalg.det(numpy_matrix)
print(f'{max_elements:.8f}')
