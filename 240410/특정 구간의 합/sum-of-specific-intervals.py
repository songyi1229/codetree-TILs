n, m = tuple(map(int, input().split()))
arr1 = list(map(int, input().split()))
arr2 = [list(map(int, input().split()))
        for _ in range(m)
]

def sum_val(n, m):
    hap = 0
    global arr1
    for i in range(n, m+1):
        hap += arr1[i-1]
    return hap


for i in range(m):
    f = arr2[i][0]
    s = arr2[i][1]
    print(sum_val(f,s))