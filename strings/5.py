n = int(input())
input_array = [int(input()) for _ in range(n)]
k = int(input())

result_array = [str(k * elem) for elem in input_array]

print(' '.join(result_array))
