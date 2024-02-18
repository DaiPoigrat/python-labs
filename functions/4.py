def matrix_replace(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] % 2 == 0:
                matrix[i][j] = 0
    return matrix


n, m = list(map(int, input().split(' ')))

input_matrix_1 = [
    [int(number) for number in input().split(' ')]
    for _ in range(n)
]

input_matrix_2 = [
    [int(number) for number in input().split(' ')]
    for _ in range(n)
]

if matrix_replace(input_matrix_1) == matrix_replace(input_matrix_2):
    print('YES')
else:
    print('NO')
