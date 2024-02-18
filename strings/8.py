from math import pi, sqrt

input_data = input().split(' ')

figure, geometry_data = input_data[0], list(map(float, input_data[1:]))

if figure == 'k':
    print(f'{2 * pi * geometry_data[0]:.4f} {pi * geometry_data[0] ** 2:.4f}')

if figure == 'p':
    a, b = geometry_data
    print(f'{2 * (a + b):.4f} {a * b:.4f}')

if figure == 't':
    a, b, c = geometry_data
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    print(f'{a + b + c:.4f} {area:.4f}')
