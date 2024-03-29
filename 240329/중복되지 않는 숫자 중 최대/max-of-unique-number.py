n = int(input())
arr = list(map(int, input().split()))

max_n = -1
count = 0
for i in arr:
    if i > max_n :

        for j in arr:
            if i == j:
                count += 1
        if count == 1:
            max_n = i
print(max_n)


# 최대를 -1로 정하고 모든 요소를 돌아가면서 세서 맥스를 정할거야. 맥스 함수 쓰지 않고

# 근데 만약에 지금 이 요소의 등장 빈도를 세서 만약에 처음 나왔으면 그때 맥스로 갱신하는거야