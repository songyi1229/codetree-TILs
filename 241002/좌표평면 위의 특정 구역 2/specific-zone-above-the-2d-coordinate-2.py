# N개의 점들 중 하나의 점 빼기
# 남은 점들을 포함하는 직사각형의 최소 넓이는?

import sys

min_area = sys.maxsize

n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

for i in range(n):
    x_arr = []
    y_arr = []
    for j in range(n):
        if i==j:
            continue

        x, y = arr[j]
        x_arr.append(x)
        y_arr.append(y)


    min_x = min(x_arr)
    max_x = max(x_arr)
    min_y = min(y_arr)
    max_y = max(y_arr)

    garo = abs(max_x - min_x)
    sero = abs(max_y - min_y)

    area_rec = garo * sero

    min_area = min(min_area, area_rec)

print(min_area)