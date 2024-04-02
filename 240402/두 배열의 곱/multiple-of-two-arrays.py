arr_1 = [
    list(map(int, input().split()))
    for _ in range(3)
]
empty = list(input().split())
arr_2 = [
    list(map(int, input().split()))
    for _ in range(3)
]

arr = [
    [0 for _ in range(3)]
    for _ in range(3)
]

for i in range(3):
    for j in range(3):
        arr[i][j] = arr_1[i][j] * arr_2[i][j]

for ii in arr:
    for jj in ii:
        print(jj, end=" ")
    print()