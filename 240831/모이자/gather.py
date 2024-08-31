import sys

n = int(input())
arr = list(map(int, input().split()))

min_sum = sys.maxsize

for i in range(1, n+1):
    diff_sum = 0
    for j in range(1, n+1):

        diff_sum += abs(j - i)*arr[j-1]
        # print(diff_sum)
    min_sum = min(min_sum, diff_sum)

print(min_sum)