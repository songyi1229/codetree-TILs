n = input()
arr = n.split()
n = int(n)
for i in range(1, n+1):
    if i%3==0 or arr == 3 or arr ==6 or arr==9:
        print(0, end =" ")
    elif i==3 or i==6 or i==9:
        print(0, end =" ")
    elif i%10==3 or i%10==6 or i%10==9:
        print(0, end =" ")
    elif i%100==3 or i%100==6 or i%100==9:
        print(0, end =" ")
    else:
        print(i, end =" ")