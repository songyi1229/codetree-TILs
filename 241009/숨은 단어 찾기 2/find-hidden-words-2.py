n, m = map(int, input().split())

arr = [
    input()
    for _ in range(n)
]

# 영역 내 여부 확인 함수
def in_range(a, b):
    return 0<=a and a<n and 0<=b and b<m

#좌우상하 대각선
dxs = [1,1,1,-1,-1,-1,0,0]
dys = [-1,0,1,-1,0,1,-1,1]

#LEE 총 개수
cnt_total = 0

for i in range(n):
    for j in range(m):
        # L이 아니면 넘어가기
        if arr[i][j] != 'L':
            continue
        
        # L이면 탐색 시작
        for dx, dy in zip(dxs, dys):
            # 현위치
            cnt = 1
            curx = i
            cury = j

            while True:
                # 현위치 기준 상하좌우대각선 탐색 위치
                nx = curx + dx
                ny = cury + dy

                # 영역안에 있는지 확인 -> 바깥에 있으면 While문 탈출
                if in_range(nx, ny) == False:
                    break 
                
                # L 다음이 E가 아니면 While문 탈출
                if arr[nx][ny] != 'E':
                    break
                
                # E라면 실행
                cnt += 1
                curx = nx
                cury = ny

                if cnt == 3:
                    cnt_total += 1

print(cnt_total)