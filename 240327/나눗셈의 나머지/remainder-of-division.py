a, b = map(int, input().split())
count = [0]*10
sum_val = 0
while True:
    if a<=1:
        break
    
    count[a%b] += 1
    a = a// b


    

for i in count:
    sum_val += i**2

print(f"{sum_val}")