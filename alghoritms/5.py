result = float(input())

while True:
    next = float(input())

    if next < 0:
        break

    result *= next

print('{:.6f}'.format(result))
