m1,d1,m2,d2 = list(map(int, input().split()))
input_day = input()

def num_days(m,d):
    days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(1, m):
        total += days[i]
    total += d

    return total

diff = num_days(m2, d2) - num_days(m1, d1) + 1

print(diff//7 + 1)