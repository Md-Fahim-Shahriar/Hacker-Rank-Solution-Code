n_t_c = int(input())

for i in range (0, n_t_c):
    n = int(input())
    s = set(map(int, input().split()))
    n_2 = int(input())
    s_2 = set(map(int, input().split()))
    print(s.issubset(s_2))