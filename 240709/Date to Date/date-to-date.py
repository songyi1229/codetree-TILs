m1, d1, m2, d2 = tuple(input().split())
m1, d1, m2, d2 = int(m1), int(d1), int(m2), int(d2)

months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sum_m1 = 0
sum_m2 = 0

for i in range(m1):
    sum_m1 += months[i] 
fin_m1 = sum_m1 + d1

for ii in range(m2):
    sum_m2 += months[ii] 
fin_m2 = sum_m2 + d2

print(fin_m2 - fin_m1+1)