from collections import deque

d = deque()
n = int(input())
for i in range(0, n):
    input_1 = input().split()
    if input_1[0] == "append":
        d.append(int(input_1[-1]))
    elif input_1[0] == "appendleft":
        d.appendleft(int(input_1[-1]))
    elif input_1[0] == "pop":
        d.pop()
    else:
        d.popleft()
d = list(d)
print(*d)