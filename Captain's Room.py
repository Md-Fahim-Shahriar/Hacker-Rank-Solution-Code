n = int(input())
s = map(int, input().split())
s = sorted(s)

for i in range (0, len(s)):
    if i != len(s)-1:
        if s[i] != s[i - 1] and s[i] != s[i + 1]:
            print(s[i])
            break
    else:
        print(s[i])

