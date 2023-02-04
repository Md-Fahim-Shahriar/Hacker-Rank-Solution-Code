def solve(s):
    s = s.capitalize()
    s_2 = ''
    for i in range (0, len(s)):
        if s[i].islower() and s[i-1].isspace():
            s_2 = s_2 + s[i].upper()
        else:
            s_2 = s_2 + s[i]
    return s_2


s = input()
result = solve(s)
print(result)