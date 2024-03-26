arr = list(map(float, input().split()))

sum = sum(arr)
mean = sum/len(arr)

print(f"{mean:.1f}")