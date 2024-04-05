def find_min(n,m):
    min_val = n*m+1
    for i in range(1, n*m+1):
        if i%n==0 and i%m==0:
            if i < min_val:
                min_val = i
        
    print(min_val)


n_num, m_num = tuple(map(int, input().split()))
find_min(n_num,m_num)