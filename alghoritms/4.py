i = int(input())

k_remains = i % 10

match k_remains:
    case 1:
        if i % 100 == 11:
            print(f'Мне {i} лет')
        else:
            print(f'Мне {i} год')
    case 2 | 3 | 4:
        if i % 100 in (12, 13, 14):
            print(f'Мне {i} лет')
        else:
            print(f'Мне {i} года')
    case 5 | 6 | 7 | 8 | 9 | 0:
        if i % 100 in (15, 16, 17, 18, 19):
            print(f'Мне {i} лет')
        else:
            print(f'Мне {i} лет')
