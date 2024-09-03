import sys

n = int(input())

arr = [
    int(input())
    for _ in range(n)
]

INT_MAX = sys.maxsize
min_dist = INT_MAX

for i in range(n):
    sum_dist = 0
    for j in range(n):
        dist = (j + n - i) % n
        sum_dist += dist * arr[j]

    min_dist = min(min_dist, sum_dist)

print(min_dist)