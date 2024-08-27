# n:학생수 m:벌칙에 걸린 학생 수 k:벌금 내야하는 벌칙 수


n, m, k = map(int, input().split())
lst = [0]*(n+1)

for _ in range(1, m):
    num = int(input())
    lst[num] += 1
    num = 0

max_val = 0
for a,b in enumerate(lst):
    if b == k:
        print(a)
    elif b > k:
        print(-1)