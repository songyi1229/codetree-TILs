n, m = map(int, input().split())

num = 0

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]


# i,j
# 0,0
# 1,0
# 2,0
# 3,0

# 3,1
# 2,1
# 1,1
# 0,1

# 0,2
# 1,2
# 2,2
# 3,2

for i in range(m):
    if i % 2 != 0:
        for j in range(n-1, -1, -1):
            arr[j][i] = num
            num += 1
    else:
        for j in range(n):
            arr[j][i] = num
            num += 1
    
        
for row in arr:
    for elem in row:
        print(elem, end=" ")
    print()