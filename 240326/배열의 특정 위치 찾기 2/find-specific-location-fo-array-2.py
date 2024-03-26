arr = list(map(int, input().split()))


even = 0
odd = 0

for i in range(10):
    if i%2==0:
        even += arr[i] # 짝수 번째 정수의 합
    else:
        odd += arr[i] # 홀수번째 입력받은 정수 합

# 큰수에서 작은 수 뺀 값
if even >= odd:
    sub = even - odd
else:
    sub = odd- even

print(sub)