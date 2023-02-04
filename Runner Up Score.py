n = int(input())
arr = list(map(int, input().split()))

max = -1000000
max_2 = -100000

for i in range (0, n):
    if arr[i] > max:
        max = arr[i]

for i in range (0, n):
    if arr[i] > max_2 and arr[i] < max:
        max_2 = arr[i]

print(max_2)