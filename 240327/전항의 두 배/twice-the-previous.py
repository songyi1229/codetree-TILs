a,b = map(int, input().split())
arr = [a, b]
cnt = 1

while True:
	
    cnt+=1
    
    arr.append(arr[cnt-1]+2*arr[cnt-2])
    if cnt==9:
        break
for j in arr:
    print(j, end=" ")