m, d = tuple(map(int, input().split()))
date_31 = []
date_30 = []
date_28 = []
for i in range(1, 32):
    date_31.append(i)
for i in range(1, 31):
    date_30.append(i)
for i in range(1, 29):
    date_28.append(i)


def judge_day(m, d):
    if m in [1,3,5,7,8,10,12]:
        if d in date_31:
            return True
    if m in [4, 6, 9, 11]:
        if d in date_30:
            return True
    if m == 2:
        if d in date_28:
            return True


if judge_day(m,d):
    print("Yes")
else:
    print('No')