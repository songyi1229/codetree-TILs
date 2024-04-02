n, m = map(int, input().split())

arr_1 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr_2 = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

for i in range(n):
    for j in range(m):
        if arr_1[i][j] != arr_2[i][j]:
            arr[i][j] = 1
        else:
            continue

for row in arr:
    for elem in row:
        print(elem, end= " ")
    print()