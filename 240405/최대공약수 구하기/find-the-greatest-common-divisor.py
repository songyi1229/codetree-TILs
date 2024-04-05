def find_max(n,m):

    max_val = 0

    for i in range(1,101):
        if n%i==0 and m%i==0:
            max_val = i
        
    print(max_val)

n_num, m_num = tuple(map(int, input().split()))
find_max(n_num, m_num)