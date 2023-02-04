def swap_case(s):
    s2 = ""
    for i in s:
        if i.isupper() == True:
            s2 = s2+i.lower()
        elif i.islower() == True:
            s2 = s2+i.upper()
        elif i.isspace() == True:
            s2 = s2+i
        else:
            s2 = s2+i
    return s2

s = input()
# print(s)
result = swap_case(s)
print(result)