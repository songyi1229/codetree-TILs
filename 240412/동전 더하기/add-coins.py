n, k = tuple(map(int, input().split()))
money = [int(input())
         for _ in range(n)
]

money.sort(reverse=True)
count = [0]*n

for i in range(n):
    count[i] = k//money[i]
    k %= money[i]

cnt = sum(count)
print(cnt)