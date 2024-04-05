n = int(input())

num = 0
arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1

for i in range(n):
    for j in range(n):
        arr[i][j] = num
        num +=1
        if num > 9:
            num = 1

        
for row in arr:
    for elem in row:
        print(elem, end= " ")
    print()