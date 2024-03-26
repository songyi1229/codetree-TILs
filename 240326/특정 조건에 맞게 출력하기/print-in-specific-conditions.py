arr = list(map(int, input().split()))

for i in arr:
    if i == 0:
        arr.pop()
        break
        
        

for j in range(len(arr)):

    if arr[j] % 2 == 1:
        odd = arr[j]+3
        print(odd, end=" ") 
    elif arr[j] % 2 == 0 :
        even = arr[j]//2
        print(even, end=" ")