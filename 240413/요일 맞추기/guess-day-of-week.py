m1, d1, m2, d2 = list(map(int, input().split()))

day = ['0', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
num_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

what_day = 1

sum_day = num_day[m1] - d1
for i in range(m1+1, m2):
    sum_day += num_day[i]

total_day = sum_day + d2 

for j in range(1, total_day + 1):
    what_day += 1
    if what_day > 7:
        what_day = 1

print(day[what_day])