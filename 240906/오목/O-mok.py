# 기준점 시작
# 1) 영역내 - 함수 사용
# 2) 상하좌우, 대각선으로 5개가 동일 색상인 경우 우승 
import sys

omok = [
    list(map(int, input().split()))
    for _ in range(19)
]


# 영역 내 여부 확인 함수
def in_range(a, b):
    return 0<=a and a<19 and 0<=b and b<19

dxs, dys = [1,1,1,-1,-1,-1,0,0], [-1,0,1,-1,0,1,-1,1]

#모든 좌표에서 다 확인
for i in range(19):
    for j in range(19):
        if omok[i][j]==0:
            continue

        for dx, dy in zip(dxs, dys):
            curt = 1
            curx = i
            cury = j
            while True:
                nx = curx + dx
                ny = cury + dy

                if in_range(nx, ny)==False:
                    break
                
                if omok[nx][ny] != omok[i][j]:
                    break
                
                curt += 1
                curx = nx
                cury = ny


            if curt == 5:
                print(omok[i][j])
                print(i+2*dx+1, j+2*dy+1)
                sys.exit()

print(0)