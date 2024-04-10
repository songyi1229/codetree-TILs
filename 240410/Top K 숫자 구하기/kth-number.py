n, k = tuple(map(int, input().split()))
arr = [0]+list(map(int, input().split()))

arr.sort()
print(arr[k])