a, b = map(int, input().split())
count = [0]*10
sum_val = 0
while True:
    a = a//b
    
    count[a%b] += 1
    if a<=1:
        break

for i in count:
    sum_val += i**2
    
print(sum_val)