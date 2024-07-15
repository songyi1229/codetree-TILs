# 1월 1일을 기준으로 계산하여 날짜 차이를 구함
# 요일의 경우 7로 나눈 나머지를 이용해서 계산 가능
# 함수를 생성해서 문제 풀이

m1, d1, m2, d2 = tuple(map(int, input().split()))

def num_days(m, d):
    days = [0, 31, 28,31,30,31,30,31,31,30,31,30,31]
    total_days = 0

    for i in range(1, m):
        total_days += days[i]

    total_days += d

    return total_days


# 두 날짜간의 차이가 몇 일
diff_days = num_days(m2, d2) - num_days(m1, d1)

### 중요 ###
# 두 날짜간의 차이가 음수가 나오는 경우, 7을 더해서 양수로 넘겨서 계산해야지 올바른 계산이 됨
# 이 코드는 diff_days 변수의 값이 0보다 커질 때까지 diff_days에 7을 계속 더하는 코드
# 즉, diff의 값을 조정해서 0 이상의 값이 되도록 하는 데 사용됩니다.
while diff_days < 0:
    diff_days += 7


days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
print(days_of_week[diff_days % 7])

# 7로 나눠서 나온 나머지가 그 날짜에 해당하는 요일