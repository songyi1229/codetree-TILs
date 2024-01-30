a,b,c = map(int, input().split())

sat = True
for i in range(a, b+1):
    if i%c == 0:
        sat=False

if sat==True:
    print('YES')
else:
    print('NO')