def get_fibonachi_number(k):
    if k == 1 or k == 2:
        return 1

    return get_fibonachi_number(k - 1) + get_fibonachi_number(k - 2)


k = int(input())

print(get_fibonachi_number(k))
