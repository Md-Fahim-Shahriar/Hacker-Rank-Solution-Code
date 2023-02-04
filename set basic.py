def average(array):
    array = list(set(array))
    total = 0
    for i in range (0, len(array)):
        total = total + array[i]
    average = total/len(array)
    return average

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)