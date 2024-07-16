# 끝점에서 닿는 경우에도 겹치는 것으로 보기 때문에 x1~x2

n = int(input())

ary = [
    tuple(map(int, input().split()))
    for _ in range(n)
    ]
max_val = max(max(ary))
zero_ary = [0] * (max_val+1)

for a, b in ary:
    for i in range(a, b+1):
        zero_ary[i] += 1

print(max(zero_ary))