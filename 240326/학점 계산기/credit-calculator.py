n = int(input())
arr = list(map(float, input().split()))


sum = sum(arr)
mean = sum/n

if mean >= 4.0:
    print(f"{mean:.1f}")
    print('Perfect')
elif mean >= 3.0:
    print(f"{mean:.1f}")
    print('Good')
else:
    print(f"{mean:.1f}")
    print('Poor')