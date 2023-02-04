N = int(input())
list_1 = []

for i in range (0, N):
    input_1 = input()
    list_1.append(input_1)

list_1 = list(set(list_1))
print(len(list_1))