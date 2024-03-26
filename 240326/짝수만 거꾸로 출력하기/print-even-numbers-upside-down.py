n = int(input())
arr = list(map(int, input().split()))

even = []
cnt = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])
        cnt += 1

for j in range(cnt-1, -1, -1):
    print(even[j], end=" ")



# 역순으로 짝수만 출력