arr_2d = [
    list(map(int, input().split()))
    for _ in range(2)
]

for i in range(2):
    sum_1 = sum(arr_2d[i])
    print(sum_1/4, end=" ")
print()   

sum_2 = 0   
for j in range(4):
    sum_2 = 0
    for i in range(2):
        sum_2 += arr_2d[i][j]
   
    print(sum_2/2, end=" ")
print()

sum_3 = 0
for i in range(2):
    for j in range(4):
        sum_3 += arr_2d[i][j]

print(sum_3/8)