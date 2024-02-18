def transpose_matrix(matrix, n, m):
    transposed_matrix = [
        ['' for _ in range(n)]
        for _ in range(m)
    ]
    for i in range(n):
        for j in range(m):
            transposed_matrix[j][i] = matrix[i][j]
    return transposed_matrix


n, m = list(map(int, input().split(' ')))

input_matrix = [
    [int(number) for number in input().split(' ')]
    for _ in range(n)
]

result = transpose_matrix(input_matrix, n, m)

for row in result:
    print(' '.join(map(str, row)))
