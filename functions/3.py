def list_replace(lst: list):
    min_index = lst.index(min(lst))
    tmp_list = lst.copy()

    last_index = len(lst) - 1
    tmp_list[last_index], tmp_list[min_index] = tmp_list[min_index], tmp_list[last_index]

    return tmp_list


n, m = list(map(int, input().split(' ')))

input_matrix = [
    [int(number) for number in input().split(' ')]
    for _ in range(n)
]

for j in range(m):
    column = [input_matrix[i][j] for i in range(n)]
    column = list_replace(column)
    for i in range(n):
        input_matrix[i][j] = column[i]
for row in input_matrix:
    print(' '.join(map(str, row)))
