n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
ans = [0] * (n+1)
a.sort()
b.sort()

for i in range(n):
    if a[i] == b[i]:
        ans[i] = True

ans.sort()
if ans[1] == 0:
    print('No')
else:
    print('Yes')