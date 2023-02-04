n = int(input())
list = []

for i in range (0, n):
    elements = int(input())
    list.append(elements)

for i in range (0, n):
    print(list[i] * list[i])
