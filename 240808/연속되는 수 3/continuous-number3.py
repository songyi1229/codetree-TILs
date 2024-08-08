n = int(input())

a = [
    int(input())
    for _ in range(n)
]

ans, cnt = 0, 0

for i in range(n):
    # case1: 부호 +
    if (i>=1 and a[i] >=0 and a[i-1] >= 0) or (i>=1 and a[i] <=0 and a[i-1] <= 0) :
        cnt += 1
    # case 2: 부호 -
    else:
        cnt = 1

    ans = max(ans, cnt)


print(ans)