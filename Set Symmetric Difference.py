n = int(input())
s = set(map(int, input().split()))
n_2 = int(input())
s_2 = set(map(int, input().split()))

x = s.symmetric_difference(s_2)
x = list(x)
print(len(x))













