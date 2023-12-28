h, w = input().split()
h = int(h)*0.01
w = int(w)
bmi = w/(h*h)
print(int(bmi))
if bmi>=25:
    print("Obesity")