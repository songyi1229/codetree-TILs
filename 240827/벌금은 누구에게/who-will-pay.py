# n:학생수 m:벌칙에 걸린 학생 수 k:벌금 내야하는 벌칙 수


n, m, k = map(int, input().split())
lst = [0]*(n+1)

for _ in range(1, m):
    num = int(input())
    lst[num] += 1
    num = 0

ans = -1
for i in lst:
    if lst[i] >= k:
        ans = i
        break

print(ans)


ary = [
    int(input())
    for _ in range(m)
]

lst = [0]*(n+1)

ans = -1

for i in ary:
    lst[i] += 1

    if lst[i] >= k:
        ans = i
        break

print(ans)