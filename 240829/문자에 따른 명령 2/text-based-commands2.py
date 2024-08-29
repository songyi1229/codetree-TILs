dir_num = 3
x, y = 0, 0
dx, dy = [1,0,-1,0], [0,-1,0,1]
nx, ny = 0, 0

text = input()
arr = [0]*(len(text))
for i in range(len(text)):
    arr[i] = text[i]

for i in arr:
    if i == 'L':
        # 왼쪽으로 90 회전
        dir_num = (dir_num - 1 + 4)%4
    elif i == 'R':
        # 오른쪽으로 90 회전
        dir_num = (dir_num + 1)%4       
    elif i == 'F':
        nx += dx[dir_num]
        ny += dy[dir_num]

print(nx, ny)