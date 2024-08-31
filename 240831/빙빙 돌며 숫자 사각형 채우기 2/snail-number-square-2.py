n, m = tuple(map(int, input().split()))

mapper = [
    [0]*m
    for _ in range(n)
]

a,b = 0,0
mapper[a][b] = 1

dxs, dys = [0,1,0,-1], [1,0,-1,0]
dir_num = 1

def in_range(x, y):
    return 0<=x and x<n and 0<=y and y<m

for i in range(2, n*m+1):
    na, nb = a + dxs[dir_num], b + dys[dir_num]

    if not in_range(na, nb) or mapper[na][nb]!=0:

        dir_num = (dir_num - 1 + 4)%4

    a, b = a + dxs[dir_num], b + dys[dir_num]

    mapper[a][b]=i

for i in range(n):
    for j in range(m):
        print(mapper[i][j], end=" ")
    print()