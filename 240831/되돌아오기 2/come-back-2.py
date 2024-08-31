text = input()
dxs, dys = [0,1,0,-1], [1,0,-1,0]


x,y=0,0
dir_num =3
ans = False

for i in range(len(text)):
    if text[i] == 'R':
        dir_num = (dir_num + 1) %4
    elif text[i] == 'L':
        dir_num = (dir_num - 1+4)%4
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]
    
    if x==0 and y==0:
        print(i+1)
        ans = True

        break

if ans == False:
    print(-1)