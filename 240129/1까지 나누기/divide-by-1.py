n = int(input())
value = 0
cnt = 0

for i in range(1, n+1):
    cnt += 1
    n//=cnt
    if n <= 1:
        break

print(i)