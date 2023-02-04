n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range (0, N):
    input_1 = input().split()
    if input_1[0] == "intersection_update":
        integer_1 = set(map(int, input().split()))
        s.intersection_update(integer_1)
        # print(s)
    elif input_1[0] == "update":
        integer_2 = set(map(int, input().split()))
        s.update(integer_2)
        # print(s)
    elif input_1[0] == "symmetric_difference_update":
        integer_3 = set(map(int, input().split()))
        s.symmetric_difference_update(integer_3)
        # print(s)
    elif input_1[0] == "difference_update":
        integer_4 = set(map(int, input().split()))
        s.difference_update(integer_4)
        # print(s)
s = list(s)
total = 0

for i in range(0, len(s)):
    total = total + s[i]

print(total)
