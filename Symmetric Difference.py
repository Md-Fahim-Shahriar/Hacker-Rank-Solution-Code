M = int(input())
x = list(map(int, input().split()))
myset_1 = set(x)
# print(myset_1)

N = int(input())
y = list(map(int, input().split()))
myset_2 = set(y)

list_1 = myset_1.difference(myset_2)
list_2 = myset_2.difference(myset_1)
list_result = list_1.union(list_2)
list_result = sorted(list_result)
print(*list_result, sep='\n')