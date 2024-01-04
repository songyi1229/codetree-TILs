a,b = input().split()
a= int(a)
b=int(b)
num = b//2 + (b%2) 

for i in range(0, num):
    n = a + 2 * i
    print(n, end=" ")