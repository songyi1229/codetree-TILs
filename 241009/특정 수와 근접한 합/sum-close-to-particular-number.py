import sys

n, s = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

min_s = sys.maxsize

arr_sum = sum(arr)

for i in range(n):
    for j in range(i+1, n):
        two_sum = arr[i] + arr[j]
        diff_sum = abs(arr_sum - two_sum)
        diff_s = abs(s - diff_sum)

        min_s = min(min_s, diff_s)

print(min_s)