n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_cnt = 0

for i in range(n):
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                 # 두 격자가 겹치면 넘어가기(조건: 같은 행에 있고, 격자 시작 열 좌표 차이가 2이내)
                if i==k and abs(j-l)<=2:
                    continue
                cnt1 = arr[i][j] + arr[i][j+1]+ arr[i][j+2]
                cnt2 = arr[k][l] + arr[k][l+1]+ arr[k][l+2]
                max_cnt = max(max_cnt, cnt1 + cnt2)

print(max_cnt)