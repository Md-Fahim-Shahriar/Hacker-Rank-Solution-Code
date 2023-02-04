def Average(lst):
    return sum(lst) / len(lst)
N = int(input())
class_name = input().split()

list_1 = []

for i in range(0, N):
    list_1.append(input().split())

# print(list_1)

index = 1

for i in range (0, len(class_name)):
    if class_name[i] == 'MARKS':
        index = i
# print(index)
list_2 =[]

for i in range(0, len(list_1)):
    list_2.append(list_1[i][index])
# print(list_2)

for i in range (0, len(list_2)):
    list_2[i] = int(list_2[i])

# print(list_2)
average = Average(list_2)
print("%.2f" % average)


