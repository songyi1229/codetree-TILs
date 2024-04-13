m1, d1, m2, d2 = list(map(int, input().split()))
ela_day = 1
num_day = [0, 31, 28, 31, 30, 31,30,31,31,30,31, 30, 31]

while True: 
    if m1==m2 and d1==d2:
        break
    
    ela_day +=1
    d1 += 1

    if d1 > num_day[m1]:
        m1+=1
        d1=1
    
print(ela_day)