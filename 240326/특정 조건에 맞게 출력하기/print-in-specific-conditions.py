array = list(map(int, input().split()))
arr=[]
for i in array:
    if i == 0:
        break
    arr.append(i)
        
        

for j in range(len(arr)):

    if arr[j] % 2 == 1:
        odd = arr[j]+3
        print(odd, end=" ") 
    elif arr[j] % 2 == 0 :
        even = arr[j]//2
        print(even, end=" ")