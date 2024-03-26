arr = list(map(int, input().split()))

# 0이면 배열 속 정수 중 2의 배수의 개수 구하고 
# 합 구하기

cnt = 0
sum = 0

for i in arr:
    if i == 0:
        break
    if i%2==0:
        sum += i
        cnt += 1



print(f"{cnt} {sum}")