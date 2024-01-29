a,b = map(int, input().split())
sat = False

for i in range(a, b+1):
    if 1920%a ==0 and 2880%a==0:
        sat = True
    elif 1920%b ==0 and 2880%b==0:
        sat = True
if sat == True:
    print(1)
else:
    print(0)