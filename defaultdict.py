from collections import defaultdict
n, m = map(int, input().split())
A = defaultdict(list)
# B = defaultdict(list)

for i in range (0, n):
    input_1 = input()
    A[input_1].append(i+1)
print(A)
for i in range(0, m):
    input_2 = input()
    if input_2 in A:
        print(*A[input_2])
    else:
        print(-1)


