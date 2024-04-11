n = int(input())
arr = [0]+list(map(int, input().split()))
range_list = [0]*(n+1)

# 각 집에 모이는 상황에 따라 거리의 합 저장 거기에서 최소인 인덱스 찾기


for i in range(1, n+1):
    range_sum = 0
    for j in range(1, n+1):
        range_sum += abs(j-i)*arr[j]

        range_list[i] = range_sum
    

min_sum = min(range_list[1:])
print(min_sum)