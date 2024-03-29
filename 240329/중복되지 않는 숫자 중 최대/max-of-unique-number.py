n = int(input())
arr = list(map(int, input().split()))

max_n = max(arr)
cnt = 0
for i in arr:
    if i == max_n:
        cnt += 1

if cnt == 1:
    print(max_n)
else:
    print(-1)