import numpy as np

matrix = np.random.randint(low=1, high=10_000, size=(4, 9))
print("Исходная матрица:")
print(matrix)

print("Элемент с индексами [2, 6]:", matrix[2, 6])

print("Каждый второй элемент третьей строки:", matrix[2, ::2])

print("Элементы последнего столбца в обратном порядке:", matrix[::-1, -1])

new_matrix = matrix.reshape(6, 6)
print("Матрица 6x6:")
print(new_matrix)

powered_matrix = np.power(matrix, 2)
print("Матрица после возведения в квадрат:")
print(powered_matrix)
print()

min_diagonal = np.min(np.diag(matrix))
print("Минимум на главной диагонали:", min_diagonal)

max_pre_last_column = np.max(matrix[:, -2])
print("Максимальный элемент в предпоследнем столбце:", max_pre_last_column)

is_non_increasing = np.all(np.diff(matrix.ravel()) <= 0)
print("Образуют ли элементы невозрастающую последовательность:", is_non_increasing)

secondary_diagonal = np.diagonal(np.flip(matrix, axis=1))
non_zero_elements = secondary_diagonal[secondary_diagonal != 0]
product_non_zero = np.prod(non_zero_elements)
print("Произведение ненулевых элементов на побочной диагонали:", product_non_zero)
