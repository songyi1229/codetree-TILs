n, t = tuple(map(int, input().split()))
r, c, c_dir = input().split()
r, c = int(r)-1, int(c)-1

mapper = {
    'R':0,
    'D':1,
    'U':2,
    'L':3
}

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
move_dir = mapper[c_dir]


def in_range(x, y):
     return 0<=x and x<n and 0<=y and y<n


for _ in range(t):
    nx, ny = r + dxs[move_dir], c + dys[move_dir]
    # if not in_range(nx, ny):
    #     c_dir = 3 - c_dir
    if in_range(nx, ny):
        r, c = nx, ny
    else:
        move_dir = 3 - move_dir

print(r+1, c+1)