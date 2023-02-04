s = input()
count = 0

for i in range (0, len(s)):
    if s[i].isalnum() == True:
        print(True)
        break
    else:
        count = count+1
if count == len(s):
    print(False)

count = 0

for i in range (0, len(s)):
    if s[i].isalpha() == True:
        print(True)
        break
    else:
        count = count+1
if count == len(s):
    print(False)

count = 0

for i in range (0, len(s)):
    if s[i].isdigit() == True:
        print(True)
        break
    else:
        count = count+1
if count == len(s):
    print(False)

count = 0

for i in range (0, len(s)):
    if s[i].islower() == True:
        print(True)
        break
    else:
        count = count+1
if count == len(s):
    print(False)

count = 0

for i in range (0, len(s)):
    if s[i].isupper() == True:
        print(True)
        break
    else:
        count = count+1
if count == len(s):
    print(False)
