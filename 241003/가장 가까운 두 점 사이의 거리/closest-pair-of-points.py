import sys

n = int(input())

arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

min_dist = sys.maxsize
dist = 0

for i in range(n):
    for j in range(i+1, n):
        x1,y1 = arr[i]
        x2,y2 = arr[j]

        dist = abs(x1-x2)*abs(x1-x2) + abs(y1-y2)*abs(y1-y2)
        if dist < min_dist:
            min_dist = dist

            

print(min_dist)