n, m = tuple(map(int, input().split()))

dxs, dys = [0,1,0,-1], [1,0,-1,0]

paint = [
    [0]*n
    for _ in range(n)
]

# 격자를 벗어나는지 확인
def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<n

for _ in range(m):
    cnt = 0
    r, c = tuple(map(int, input().split()))
    r, c = r-1, c-1
    paint[r][c] = 1

    for i in range(4):
        r,c = r + dxs[i], c+dys[i]
        if in_range(r,c) and paint[r][c] == 1:
            cnt += 1 
        r,c = r - dxs[i], c-dys[i]
        #r, c를 원상 복구


    if cnt == 3:
        print(1)
    else:
        print(0)