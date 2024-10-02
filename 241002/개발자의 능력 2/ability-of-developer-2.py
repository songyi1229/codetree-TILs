import sys

min_val = sys.maxsize

arr = tuple(map(int, input().split()))


def get_team(x,y,z,w):
    team1 = arr[x] + arr[y]
    team2 = arr[z] + arr[w]
    team3 = sum(arr) - team1 - team2
    
    team_arr = [team1, team2, team3]
    max_team = max(team_arr)
    min_team = min(team_arr)
    return (max_team - min_team)



#첫번째 팀원
for i in range(6):
    for j in range(i+1, 6):

        # 두번째 팀원 (처음부터 새로 시작) 하지만 첫번쨰 팀원과 겹치는 인원이 있으면 안됨
        for k in range(6):
            for l in range(k+1, 6):
                if k==i or k==j or l==i or l==j:
                    continue

                diff = get_team(i,j,k,l)

                if diff < min_val:
                    min_val = diff

                # min_val = min(min_val, get_team(i,j,k,l))


print(min_val)