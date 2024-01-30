sat = True
for i in range(5):
    n = int(input())
    if n%3==0:
        continue
    else:
        sat = False

if sat==True:
    print(1)
else:
    print(0)