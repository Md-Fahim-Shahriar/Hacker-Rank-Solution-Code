n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range (0, N):
    input_1 = input().split()
    if input_1[0] == "remove":
        s.remove(int(input_1[-1]))
    elif input_1[0] == "discard":
        s.discard(int(input_1[-1]))
    else:
        s.pop()
s = list(s)
total = 0

for i in range (0, len(s)):
    total = total + s[i]

print(total)