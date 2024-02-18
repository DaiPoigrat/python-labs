import sys


def is_prime(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    else:
        return True


input_number = int(input())

for i in range(2, input_number):
    tmp_result = input_number - i
    if is_prime(i) and is_prime(tmp_result):
        print(f'{i} {tmp_result}')
        sys.exit()
