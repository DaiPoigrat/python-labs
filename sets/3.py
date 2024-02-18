str1 = input()
str2 = input()

cnt_str1 = set(str1)
cnt_str2 = set(str2)

if cnt_str2 - cnt_str1 == set():
    print(True)
else:
    print(False)