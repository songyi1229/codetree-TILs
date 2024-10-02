import sys 

int_max = sys.maxsize

a,b,x,y = tuple(map(int, input().split()))

min_dist = int_max

# case1 = a->b
min_dist = min(min_dist, abs(b-a))

# case2 = a->x->y->b
min_dist = min(min_dist, abs(a-x)+abs(b-y))

# case3 = a->y->x->b
min_dist = min(min_dist, abs(a-y)+abs(b-x))

print(min_dist)