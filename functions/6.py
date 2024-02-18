def multiply_matrix(matrix1, matrix2):
    result = [
        [0 for _ in range(len(matrix1))]
        for _ in range(len(matrix1))
    ]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix1[0])):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


n = int(input())

input_matrix = [
    [float(number) for number in input().split(' ')]
    for _ in range(n)
]

result = input_matrix
for _ in range(n - 1):
    result = multiply_matrix(result, input_matrix)
for i in range(n):
    print(' '.join(f'{value:.3f}' for value in result[i]))
