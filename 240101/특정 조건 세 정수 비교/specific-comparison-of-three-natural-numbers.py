arr = input()
a,b,c = arr.split()
a = int(a)
b = int(b)
c = int(c)

if a<=b and a<=c:
    print(1, end=" ")
else:
    print(0, end=" ")

if a==b==c:
    print(1, end=" ")
else:
    print(0, end=" ")