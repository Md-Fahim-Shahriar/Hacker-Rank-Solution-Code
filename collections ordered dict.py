N = int(input())
list_1 = []
list_2 = []
list_3 = []
for i in range(0, N):
   input_1 = input().split()
   list_1.append(input_1)
   list_2.append(' '.join(input_1[:-1]))
   list_3.append(int(input_1[-1]))

# print(list_2)
# print(list_3)
list_4 = []
for i in range (0, N):
   count_1 = list_2.count(list_2[i])
   print(count_1)
   list_4.append(list_3[i]*count_1)

list_4 = list(map(str, list_4))
# print(list_4)

# list_5 = []

for i in range (0, N):
   list_1[i][-1] = list_4[i]
# print(list_1)
new_list = []

for l in list_1:
    if l not in new_list:
        new_list.append(l)

for item in new_list:
        print(' '.join(str(x) for x in item))