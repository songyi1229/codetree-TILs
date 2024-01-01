arr = input()
a,b,c = arr.split()
a = int(a)
b = int(b)
c = int(c)
min = min(arr)

print(int(a==min),end=" ")
print(int(a==b==c))