# n = int(input())
# string = [list(input())
#     for _ in range(n)
# ]

# string.sort()
# for i in range(n):

#     new = ''.join(string[i])
#     print(new)



n = int(input())
string = [list(input())
    for _ in range(n)
]

string.sort()

for i in range(n):
    print(''.join(string[i]))