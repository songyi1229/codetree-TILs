b, a = input().split()
b = int(b)
a = int(a)

num = (b - a)//2 + 1

for i in range(b, a-1, -2):
    print(i, end =" ")