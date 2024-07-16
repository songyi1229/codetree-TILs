# 음수인 경우를 대비해서 offset 설정
offset = 100
max_r = 200

n = int(input())

ary = [
    tuple(map(int, input().split()))
    for _ in range(n)
    ]

zero_ary = [0]*(max_r+1)



for a, b in ary:
    a, b = a+offset, b+offset
    
    for i in range(a, b):
        zero_ary[i] += 1


max_num = max(zero_ary)

print(max_num)