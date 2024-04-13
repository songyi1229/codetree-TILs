m1, d1, m2, d2 = list(map(int, input().split()))

def num_days(m,d):
    num_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_day = 0

    for i in range(1, m):
        sum_day += num_day[i]

    sum_day += d
    return sum_day

diff = num_days(m2,d2) - num_days(m1,d1)

while diff <0:
    diff += 7
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
print(day[diff%7])