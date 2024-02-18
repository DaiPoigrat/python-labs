def remove_brackets_with_data(str: str):
    while '(' in str:
        start = str.find('(')
        stop = str.find(')')
        str = str[:start] + str[stop + 1:]

    return str


n = int(input())

for _ in range(n):
    print(remove_brackets_with_data(input()))
