n = int(input())



def bigger_num(n):
    if n == 0:
        return
    bigger_num(n-1)
    print(n, end =" ")

def smaller_num(n):
    if n == 0:
        return
    print(n, end= " ")
    smaller_num(n-1)



bigger_num(n)
print()
smaller_num(n)