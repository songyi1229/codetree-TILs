n = int(input())
arr = list(map(int, input().split()))

list = [i**2 for i in arr]

for i in range(len(list)):
    print(list[i], end=" ")