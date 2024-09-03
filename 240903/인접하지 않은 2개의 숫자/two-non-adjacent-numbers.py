n = int(input())
arr = list(map(int, input().split()))

ans = 0

for i in range(n):
    
    for j in range(i+2, n):
        sum_n = 0
        sum_n = arr[i] + arr[j]
        ans = max(ans, sum_n)

print(ans)