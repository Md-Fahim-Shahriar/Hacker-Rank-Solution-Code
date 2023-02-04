# n = int(input())
s = set(map(int, input().split()))
n_2 = int(input())
s_2 = set(map(int, input().split()))
count = 0
for i in range(0, n_2):
    s_2 = set(map(int, input().split()))
    if s.issuperset(s_2):
        count = count+1
if count == n_2:
    print("True")
else:
    print("False")