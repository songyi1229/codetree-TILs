n = int(input())
sum = 0
for i in range(n):
    num = int(input())
    sum += num

mean = sum/n

print(sum, end=" ")
print(mean)