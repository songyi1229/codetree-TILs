n = int(input())

sum1 = 0
cnt = 0

for _ in range(n):
    arr = list(map(int, input().split()))
    sum1 = sum(arr)


    mean = sum1/4


    if mean >= 60:
        print('pass')
        cnt+=1
    else:
        print('fail')

print(cnt)