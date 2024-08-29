n = int(input())

arry = [
    list(map(int, input().split()))
    for _ in range(n)
]

x, y = 0, 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def check_region(x, y):
    return 0<=x and x<n and 0<=y and y<n

cnt = 0
cnt_total = 0

def adjacent_cnt(x,y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if check_region(nx, ny) and arry[nx][ny] == 1:
            cnt += 1
    return cnt


ans = 0
for i in range(n):
    for j in range(n):
        if adjacent_cnt(i, j) >= 3:
            ans += 1


print(ans)