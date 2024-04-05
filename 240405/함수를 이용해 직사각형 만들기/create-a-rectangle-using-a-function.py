def print_star(n, m):
    for _ in range(n):
        print("1"*m)

n_num, m_num = tuple(map(int, input().split()))
print_star(n_num, m_num)