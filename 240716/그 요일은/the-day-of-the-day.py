m1, d1, m2, d2 = tuple(map(int, input().split()))
A = input()


# 날짜 차 계산 함수

def diff_days(m, d):
    days = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    hap=0
    for i in range(1, m):
        hap += days[i]

    hap2 = hap + d

    return hap2

diff_day =diff_days(m2, d2) - diff_days(m1, d1) 

day = ["Mon", 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

# 빼주면 딱 월~일까지로 맞출수 있음
number = diff_day - day.index(A)
cnt = 0
# 7을 더하는 이유는 음수인 경우를 대비해 양수로 만들어주기 위해
cnt = (number + 7) // 7

print(cnt)