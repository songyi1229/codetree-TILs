n = int(input())
arr = list(map(int, input().split()))

max_n = max(arr)
cnt = 0
new_arr = []
for i in arr:
    if i == max_n:
        cnt += 1
    else:
        new_arr.append(i)

max_s_n = max(new_arr)

if cnt == 1:
    print(max_n)
elif cnt >= 2:
    print(max_s_n)
else:
    print(-1)

# 최대르 찾아 만약에 1개만 있으면 그게 최대르
# 최대를 찾아 만약에 2개 이사이면 그거를 빼고 나머지 배열에서 최대를 찾아
# 그것도 아니면 -1 출력