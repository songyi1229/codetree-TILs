# 각 사람의 매 초마다의 위치를 기록, 쭉 순회하며 그 중 시간과 위치가 동시에 일치하는 최초의 시점을 잡으면 됨

max_t = 1000000 
#(1 <= t <= 1000)

n, m = tuple(map(int, input().split()))
a, b = [0]*(max_t + 1) , [0]*(max_t + 1)

# A가 매 초마다 서있는 위치 기록
time_a = 1
for _ in range(n):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        a[time_a] = a[time_a - 1] + (1 if d == 'R' else -1)
        time_a += 1


time_b = 1
for _ in range(m):
    d, t = tuple(input().split())
    for _ in range(int(t)):
        b[time_b] = b[time_b - 1] + (1 if d == 'R' else -1)
        time_b += 1


# 최초로 만나는 시간
ans = -1
for i in range(1, time_a):
    if a[i] == b[i]:
        ans = i
        break

print(ans)