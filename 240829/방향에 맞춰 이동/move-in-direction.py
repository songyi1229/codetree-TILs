n = int(input())
dx, dy = [1,0,-1,0], [0,-1,0,1]

x, y = 0, 0
nx, ny = 0, 0
for _ in range(n):
    direc, dir_num = input().split()
    dir_num = int(dir_num)

    if direc == 'E':
        nx += dx[0]*dir_num
        ny += dy[0]
    elif direc == 'S':
        nx += dx[1]
        ny += dy[1]*dir_num
    elif direc == 'W':
        nx += dx[2]*dir_num
        ny += dy[2] 
    elif direc == 'N':
        nx += dx[3] 
        ny += dy[3]*dir_num
print(nx, ny)