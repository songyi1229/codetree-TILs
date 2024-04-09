n = int(input())
arr = list(map(int, input().split()))

def absolute_val(arr):
    for i in range(n):
        arr[i] = abs(arr[i])
        print(arr[i], end=" ")
    
absolute_val(arr)