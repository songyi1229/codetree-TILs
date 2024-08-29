n, m = tuple(map(int, input().split()))

max_t = 1000000

pos_a = [0] * (max_t + 1)
pos_b = [0] * (max_t + 1)

time_a = 1
for _ in range(n):
    v, t = tuple(input().split())
    for _ in range(int(t)):
        pos_a[time_a] = pos_a[time_a - 1] + int(v)
        time_a += 1


time_b = 1
for _ in range(m):
    v, t = tuple(input().split())
    for _ in range(int(t)):
        pos_b[time_b] = pos_b[time_b - 1] + int(v)
        time_b += 1

#a가 리더 = 1, b가 리더 = 2, c가 리더 = 3
leader= 0
cnt = 0
for i in range(1, time_a):
    if pos_a[i] > pos_b[i]:
        if leader != 1:
            cnt += 1
        leader = 1
    elif pos_a[i] < pos_b[i]:
        if leader != 2:
            cnt += 1
        leader = 2
    elif pos_a[i] == pos_b[i]:
        if leader != 3:
            cnt += 1
        leader = 3
    
print(cnt)