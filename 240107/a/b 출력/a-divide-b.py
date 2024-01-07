a,b = map(int, input().split())

inte = a//b
print(f"{inte}.", end ="")
a%=b
for i in range(20):
    a*=10
    d=a//b
    print(d, end ="")
    a%=b