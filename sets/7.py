import sys

str1 = input()
str2 = input()

counter_str1 = {}

for char in str1:
    if char not in counter_str1:
        counter_str1[char] = 1
    else:
        counter_str1[char] += 1

counter_str2 = {}

for char in str2:
    if char not in counter_str2:
        counter_str2[char] = 1
    else:
        counter_str2[char] += 1

for key, value in counter_str2.items():
    if key not in counter_str1:
        print(False)
        sys.exit()

    if counter_str1[key] < value:
        print(False)
        sys.exit()

print(True)
