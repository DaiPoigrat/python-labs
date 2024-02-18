n = int(input())

numbers = [abs(int(input())) for i in range(n)]

max_number = max(numbers)

index = numbers[::-1].index(max_number)

print(n - index)
