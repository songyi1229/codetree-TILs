import sys
n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]
INT_MAX = sys.maxsize
ans = INT_MAX

for i in range(1, n-1):
    dis = 0
    pre_idx = 0
    for j in range(1, n):

        if j == i:
            continue

        dis += abs(arr[pre_idx][0] - arr[j][0]) + abs(arr[pre_idx][1] - arr[j][1])
        pre_idx = j

    ans = min(ans,dis)

print(ans)