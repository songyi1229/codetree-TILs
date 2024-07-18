# 좌표가 음수인 경우를 대비해서 offset을 더해야 함 -> 모든 좌표를 양수로 변경
# offset 정하는 법: 문제에서 주어지는 x값의 최소가 -1000(n=100 곱하기 x=10)이므로 offset을 1000으로 설정

offset = 1000
max_r = 2000


n = int(input())


cur = 0
bar = []

for _ in range(n):
    dis, direc = input().split()
    dis = int(dis)

    if direc == "R":
        # 오른쪽으로 이동할 경우 : cur ~ cur + dis 까지 경로 이동
        sec_L = cur
        sec_R = cur + dis
        cur += dis
    
    else: 
        # 왼쪽으로 이동할 경우 : cur - dis ~ cur까지 경로 이동
        sec_L = cur - dis
        sec_R = cur
        cur -= dis
    
    # 배열에 좌표 추가
    bar.append([sec_L, sec_R])

checked = [0] * (max_r + 1)

for x1, x2 in bar:
    # offset 더해주기
    x1, x2 = x1 + offset, x2 + offset

    # 구간 칠하기
    for i in range(x1, x2):
        checked[i] += 1

# 2번 이상 지나간 영역 크기 구하기
cnt = 0
for elem in checked:
    if elem >= 2:
        cnt += 1

print(cnt)