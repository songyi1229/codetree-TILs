n = int(input())


for i in range(n):
    # 별
    for _ in range(n-i):
        print("*", end="")
    # 공백
    for _ in range(2*i):
        print(" ", end="")
    #별
    for _ in range(n-i):
        print("*", end="")
        
    print()